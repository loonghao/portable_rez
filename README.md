# portable rez

A portable rez (Windows only)

## setup dev env
```shell
pip install -r requirements-dev.txt
```

## build portable rez
```shell
nox -s build-exe
```

## build portable rez release
```shell
nox -s build-exe -- --release
```
