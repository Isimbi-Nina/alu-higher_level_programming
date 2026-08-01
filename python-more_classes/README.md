# Python - More Classes and Objects

## Description

This project builds on the basics of Object-Oriented Programming in
Python 3, going deeper into `__str__`/`__repr__`, the `__del__`
destructor, class attributes vs. instance attributes, class methods,
and static methods.

Each task builds incrementally on a `Rectangle` class, starting from an
empty class and progressively adding validated `width`/`height`
properties, `area`/`perimeter` methods, string representations, a
destructor, an instance counter, a configurable print symbol, an
instance comparator, and a `square` factory class method.

## Requirements

* Ubuntu 20.04 LTS, Python 3.8.5
* All files end with a new line
* All files start with `#!/usr/bin/python3`
* Code follows `pycodestyle` (version 2.7.*)
* All files are executable

## Files

| File | Description |
| --- | --- |
| `0-rectangle.py` | Empty `Rectangle` class |
| `1-rectangle.py` | `Rectangle` with validated `width`/`height` properties |
| `2-rectangle.py` | `Rectangle` with `area` and `perimeter` methods |
| `3-rectangle.py` | `Rectangle` printable with `#` via `__str__` |
| `4-rectangle.py` | `Rectangle` with an eval-friendly `__repr__` |
| `5-rectangle.py` | `Rectangle` that prints `Bye rectangle...` on deletion |
| `6-rectangle.py` | `Rectangle` with a `number_of_instances` class attribute |
| `7-rectangle.py` | `Rectangle` with a configurable `print_symbol` class attribute |
| `8-rectangle.py` | `Rectangle` with a `bigger_or_equal` static method |
| `9-rectangle.py` | `Rectangle` with a `square` class method |

## Usage

Each file can be imported and used independently, e.g.:

```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
```

## Author

ALU Higher Level Programming - python-more_classes project
