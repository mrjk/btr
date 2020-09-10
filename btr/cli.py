#!/bin/env python3


# Imports
# -------------------------------------------
import click
import click_log
from btr.common import Controller


# Configure logging
# -------------------------------------------
import logging
log = logging.getLogger(__name__)
consolehandler = logging.StreamHandler()
consoleformatter = logging.Formatter('[%(name)s] %(levelname)s: %(message)s')
consoleformatter = logging.Formatter(fmt='[%(asctime)s.%(msecs)03d] %(levelname)s: %(message)s',
        datefmt='%S')
consolehandler.setFormatter(consoleformatter)


# Default command groups, usually display help
# -------------------------------------------

@click.group()
@click_log.simple_verbosity_option(log)
@click.option('-c', '--config', 
        default='tests/data.yml', 
        help='Yaml config to use', 
        type=click.Path(exists=True))
@click.option('-t', '--timer', 
        default=1, 
        help='Time service need to start in seconds (1s)', 
        type=float)
@click.option('-v', '--verbose', count=True)
@click.pass_context
def cli(ctx, config, verbose, timer):

    # Prepare logging
    for lib in ['btr.cli', 'btr.common']:
        lib = logging.getLogger(lib)
        lib.addHandler(consolehandler)
        if verbose > 0:
            lib.setLevel(logging.DEBUG)
        else:
            lib.setLevel(logging.INFO)


    # Prepare config and controller
    ctx.ensure_object(dict)
    try:
        ctx.obj['ctrl'] = Controller(config, timer=timer)
    except Exception as e:
        raise click.ClickException(e)


# Start and stop cli
# -------------------------------------------

@cli.command()
@click.argument('service')
@click.pass_context
def start(ctx, service):
    """Start a service"""
    log.info(f'Starting service "{service}" ...')
    o = ctx.obj['ctrl']

    try:
        o.dump()
        o.srv_change(service, 'start')
    except Exception as e:
        log.error(f'An error occured: {e}')


@cli.command()
@click.argument('service')
@click.pass_context
def stop(ctx, service):
    """Stop a service"""
    log.info(f'Stopping service "{service}" ...')
    o = ctx.obj['ctrl']

    try:
        o.dump()
        o.srv_change(service, 'stop')
    except Exception as e:
        log.error(f'An error occured: {e}')


if __name__ == "__main__":
    cli()

