# nested-dataclasses

This repository is for my python learning from the following site.
https://stackoverflow.com/questions/51564841/creating-nested-dataclass-objects-in-python

## Getting Started

```shell
pip install git+https://github.com/mububoki/nested-dataclasses.git
```

## Sample

```shell
python ./sample/main.py
```

You can confirm that the output is not
```shell
b: B(bb='str_bb', ba={'aa': 1, 'ab': 'str_ab'})
```
but
```shell
b: B(bb='str_bb', ba=A(aa=1, ab='str_ab'))
```
