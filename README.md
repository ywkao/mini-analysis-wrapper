# mini-analysis-wrapper

This is an example analysis wrapper for running multi-threading jobs using python multiprocessing module.

## Command
```
$ git clone -b branch-example-01 git@github.com:ywkao/mini-analysis-wrapper.git
$ cd mini-analysis-wrapper/
$ ./run.py --dryRun
$ ./run.py # execute with python multiprocessing module
```

## Overview
```
|-- README.md
|-- bin
|   `-- dummyTester.py
|-- interface
|   |-- __init__.py
|   |-- config.py
|   `-- parallel_utils.py
`-- run.py
```

| File                        | Description                                                      |
| --------------------------- | ---------------------------------------------------------------- |
| bin/dummyTester.py          | A script to be replaced by a c++ executable                      |
| interface/config.py         | Placeholder for config parameters specific to an anlaysis        |
| interface/parallel_utils.py | Utility for running jobs parallelly using multiprocessing module |
| run.py                      | Top-level script steering the analysis flow                      |
