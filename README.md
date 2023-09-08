# mini-analysis-wrapper

This is an example analysis wrapper for running multi-threading jobs using python multiprocessing module.

This patch branch bypasses priority setting using `/bin/nice`.

## Command
```
$ git clone -b patch-example-01 git@github.com:ywkao/mini-analysis-wrapper.git
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

| File                         | Description                                                      |
| ---------------------------- | ---------------------------------------------------------------- |
| `run.py`                     | Top-level script steering the analysis flow                      |
| `bin/dummyTester.py`         | A script to be replaced by a c++ executable                      |
| `interface/__init__.py`      | A file turning the directory as a regular package ([more](https://docs.python.org/3/reference/import.html#regular-packages)) |
| `interface/config.py`        | Placeholder for config parameters specific to an anlaysis        |
| `interface/parallel_utils.py`| Utility for running jobs parallelly using multiprocessing module |
