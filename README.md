# Python project service solver

This project has been made in the context of a recruiting process for behavox.

## Install

The installation procedure is quite simple:
```
git clone https://github.com/mrjk/btr.git && cd btr
virtualenv -p python3 venv && . venv/bin/activate
pip install .
```

For development version, use `pip install -e .` instead.

## Usage

There is how to use the program:
```
btr start fullhouse
btr stop fullhouse
```

You can choose your own dataset, with the `--config` flag. You can also tweak verbosity output with `-v` and the time services take to load with the `--timer` flag. To get the full help:

```
$ btr --help
Usage: btr [OPTIONS] COMMAND [ARGS]...

Options:
  -c, --config PATH  Yaml config to use
  -t, --timer FLOAT  Time service need to start in seconds (1s)
  -v, --verbose
  --help             Show this message and exit.

Commands:
  start  Start a service
  stop   Stop a service
```

## Example

There is an output example, with the [default yaml dataset](tests/data.yml):
```
btr start dashboard
[23.049] INFO: Starting service "dashboard" ...
[23.049] INFO: Sequential services order: mysql, elasticsearch, zookeeper, hadoop-namenode, hbase-master, fullhouse, dashboard
[24.051] INFO: Service Started: mysql
[24.051] INFO: Service Started: elasticsearch
[24.052] INFO: Service Started: zookeeper
[25.053] INFO: Service Started: hadoop-namenode
[26.554] INFO: Service Started: hbase-master
[27.556] INFO: Service Started: fullhouse
[29.057] INFO: Service Started: dashboard
[29.058] INFO: Service "dashboard" has been started!
```

## Todo

* Implement code coverage and extended data set tests
* Make output a bit easier to read
* Allow to switch between sequential or threaded service processing
* Document yaml file format

## Licence (MIT)

Copyright 2020, Robin Cordier

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
