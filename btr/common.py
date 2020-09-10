#!/bin/env python3

# Imports
# -------------------------------------------
import yaml
import threading
import time

import logging
logger = logging.getLogger(__name__)


# Main classes
# -------------------------------------------
class Controller():
    """This object hold the whole resolving logic"""

    timer = 1
    nodes = {}
    process_order = []
    process_done = []


    # Initialization methods
    # -------------------------------------------
    def __init__(self, config, timer=1):
        self.load_conf(config)
        self.timer = timer


    def load_conf(self, config):
        """Load yaml conf, and load nodes with deps and parents"""

        # Import yaml config
        with open(config) as file:
            raw_conf = yaml.load(file, Loader=yaml.FullLoader)

        # Insert nodes into service dict
        for name, spec in raw_conf.items():
            self.nodes[name] = Node(name)

        # Add dependencies references for each service
        for name, spec in raw_conf.items():

            if 'deps' in spec:
                for dep in spec['deps']:

                    # Check referenced service exists
                    if not dep in self.nodes:
                        raise Exception (f'Missing "{dep}" dependency declaration for {name}')

                    # Do the association
                    parent = self.nodes[name]
                    child = self.nodes[dep]
                    parent.addDep(child)
                    child.addParent(parent)


    # Runtime functions
    # -------------------------------------------
    def dump(self):
        """Display the content of raw data"""
        logger.debug(f'Nodes list:')
        for n, i in self.nodes.items():
            logger.debug(f'- {n}:')
            logger.debug(f'    Depends:')
            for j in i.depends:
                logger.debug(f'    - {j.name}')
            logger.debug(f'    Parents:')
            for j in i.parents:
                logger.debug(f'    - {j.name}')


    def srv_change(self, name, action):
        """Start or stop a service"""

        # Safety checks
        assert action in ['start', 'stop']
        try:
            srv = self.nodes[name]
        except Exception as e:
            raise Exception(f"Can't find service '{name}'\n{e}")

        # Resolve the service order
        # BUG: This is basically pointless as everythong is threadedd now ...
        self.process_order = []
        self.process_done = []
        if action == 'start':
            self.resolve_start(srv)
        else:
            self.resolve_stop(srv)

        # Log infos
        self.process_done = []
        str_list = ", ".join([i.name for i in self.process_order])
        logger.info(f'Sequential services order: {str_list}')

        # Start services threads
        threads = {}
        for node in self.process_order:
            threads[node.name] = threading.Thread(target=getattr(node, action), args=(self,))
            threads[node.name].start()

        # Wait for all threads to be finished
        for name, t in threads.items():
            t.join()

        # Cleanup
        self.process_order = []
        self.process_done = []
        if action == 'start':
            logger.info (f'Service "{srv.name}" has been started!')
        else:
            logger.info (f'Service "{srv.name}" has been stopped!')


    # Resolution algorithms
    # -------------------------------------------
    def resolve_start(self, node):
        """This static method to create the start resolution order"""

        if not node in self.process_done:
            self.process_done.append(node)

        for i in node.depends:
            if not i in self.process_done:
                self.resolve_start(i)
            else:
                raise Exception (f'Infinite loop has been detected: "{node.name}" <=> "{i.name}"')
        self.process_order.append(node)


    def resolve_stop(self, node):
        """This static method to create the stop resolution order"""

        if not node in self.process_done:
            self.process_done.append(node)

        self.process_order.append(node)
        for i in node.depends:
            if not i in self.process_done:
                self.resolve_stop(i)
            else:
                raise Exception (f'Infinite loop has been detected: "{node.name}" <=> "{i.name}"')


class Node():
    """This class represent a service and its dependedncies"""

    name = ''
    depends = []
    parents = []


    # Initialization
    # -------------------------------------------
    def __init__(self, name):
        self.name = name
        self.depends = []
        self.parents = []

    def addDep(self, node):
        """Add a child dependency"""
        self.depends.append(node)

    def addParent(self, node):
        """Add a parent requirement"""
        self.parents.append(node)


    # Start and Stop logic
    # -------------------------------------------
    def start(self, controller):
        """Start the service but wait its deps"""
        logger.debug (f'Service Start: {self.name}')

        # Check dependencies are available
        for dep in self.depends:
            if not dep in controller.process_order:
                logger.debug (f"  Service Skip: {self.name} ignore {dep.name}")
                continue
            while not dep.name in controller.process_done :
                logger.debug (f"Service Wait: {self.name} is waiting service {dep.name}")
                time.sleep(0.5)

        # Fake load the service
        time.sleep(controller.timer)
        logger.info (f'Service Started: {self.name}')
        controller.process_done.append(self.name)

    def stop(self, controller):
        """Stop the service but wait its deps"""
        logger.debug (f'Service Stop: {self.name}')

        # Check dependencies are available
        for dep in self.parents:
            if not dep in controller.process_order:
                logger.debug (f"  Service Skip: {self.name} ignore {dep.name}")
                continue
            while not dep.name in controller.process_done :
                logger.debug (f"  Service Wait: {self.name} is waiting service {dep.name}")
                time.sleep(0.5)

        # Fake load the service
        time.sleep(controller.timer)
        logger.info (f'Service Stopped: {self.name}')
        controller.process_done.append(self.name)



