# portable rez
[![Windows](https://img.shields.io/badge/OS-Winodws-green)](https://img.shields.io/badge/OS-Winodws-green)
[![Mac](https://img.shields.io/badge/OS-Mac-green)](https://img.shields.io/badge/OS-Mac-green)
[![Linux](https://img.shields.io/badge/OS-Linux-green)](https://img.shields.io/badge/OS-Linux-green)

A Portable [rez](https://github.com/AcademySoftwareFoundation/rez) base on [PyOxidizer](https://github.com/indygreg/PyOxidizer)


`PyOxidizer` is a utility for producing binaries that embed Python.
The over-arching goal of PyOxidizer is to make complex packaging and distribution problems simple so
application maintainers can focus on building applications instead of toiling with build systems and packaging tools.

[PyOxidizer Comparisons to Other Tools](https://pyoxidizer.readthedocs.io/en/stable/pyoxidizer_comparisons.html?highlight=comparisons)

## Setup dev env
```shell
pip install -r requirements-dev.txt
```

## Build portable rez
```shell
nox -s build-exe
```

## Build portable rez release
```shell
nox -s build-exe -- --release
```
