# Python - Object-Oriented Programming

## Description

This project is an introduction to Object-Oriented Programming (OOP) in
Python 3. It covers classes, objects, instances, attributes, methods,
`self`, the `__init__` method, data abstraction/encapsulation/information
hiding, public/protected/private attributes, and the Pythonic way of
writing getters and setters using properties.

Each task builds incrementally on a `Square` class, starting from an
empty class and progressively adding a private `size` attribute, input
validation, an `area` method, property-based getters/setters, a
`my_print` method, and finally a `position` attribute.

## Requirements

* Ubuntu 20.04 LTS, Python 3.8.5
* All files end with a new line
* All files start with `#!/usr/bin/python3`
* Code follows `pycodestyle` (version 2.7.*)
* All files are executable
* Every module, class, and method has a documentation string

## Files

| File | Description |
| --- | --- |
| `0-square.py` | Empty `Square` class |
| `1-square.py` | `Square` with a private instance attribute `size` |
| `2-square.py` | `Square` with `size` validation (type and value) |
| `3-square.py` | `Square` with an `area` method |
| `4-square.py` | `Square` with `size` as a property (getter/setter) |
| `5-square.py` | `Square` with a `my_print` method |
| `6-square.py` | `Square` with a `position` property affecting `my_print` |

## Usage

Each file can be imported and used independently, e.g.:

```
$ ./6-square.py
```

or imported in another script:

```python
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square = Square(3, (1, 1))
my_square.my_print()
```

## Author

ALU Higher Level Programming - python-classes project
