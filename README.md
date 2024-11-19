# minimalPythonPackage

Example of a minimal python package

## Installation

To install the package editable, run

```
pip install -e PATH/TO/PACKAGE
```

where path/to/package is the folder containing the `setup.py` file

## Package managers

`pip` installs packages from the Python Package Index (PyPI) by default. Can install source and binary distributions, depending on what is available.
To speed it up, use `uv` and substitute `pip` with `uv pip` in any command.

`conda` is a package manager that installs packages from the Anaconda repository, other channels can be added. Install `conda` by downloading and installing `miniforge` from
here: https://github.com/conda-forge/miniforge#download. This has the `conda-forge` channel enabled by default.
The directory can take up a lot of space, put it in a data directory, not your home folder (usually).
To speed up everything, use `mamba` instead of `conda` (it is a drop-in replacement).

## Usage

Always create a virtual environment! Best is to use `conda`/`mamba` for this (do not use the base env, this can be deactivate by default).

```bash
mamba create -n myenv311 python=3.11 uv
```

This install Python 3.11 and uv.

To install more packages, first activate the environment

```bash
conda activate myenv311
```

and then install packages with `mamba` or `pip`. First install only with `mamba`, if not available, use `pip` and then don't go back.

```bash
mamba install numpy
```
