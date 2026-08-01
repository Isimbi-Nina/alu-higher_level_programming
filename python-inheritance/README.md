# python-inheritance

A collection of Python scripts exploring inheritance concepts: base
classes, subclasses, attribute discovery, `isinstance`/`issubclass`/
`type`/`super`, and building a small class hierarchy of geometric
shapes.

## Learning Objectives

- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type`
  and `super` built-in functions

## Requirements

- Editors: `vi`, `vim`, `emacs`
- All files interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files end with a new line
- The first line of every file is exactly `#!/usr/bin/python3`
- Code follows `pycodestyle` (version 2.7.*)
- All files are executable
- Every module, class, and function has real, descriptive documentation
- Test files live in the `tests/` folder as `.txt` files and are run with:
  ```
  python3 -m doctest ./tests/*
  ```

## Files

| File | Description |
| --- | --- |
| `0-lookup.py` | `lookup(obj)` — returns the list of available attributes and methods of an object |
| `1-my_list.py` | `MyList` — inherits from `list`; adds `print_sorted()` |
| `2-is_same_class.py` | `is_same_class(obj, a_class)` — True if `obj` is exactly an instance of `a_class` |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)` — True if `obj` is an instance of `a_class` or a subclass of it |
| `4-inherits_from.py` | `inherits_from(obj, a_class)` — True if `obj` is an instance of a class that inherited from `a_class` |
| `5-base_geometry.py` | `BaseGeometry` — empty base class |
| `6-base_geometry.py` | `BaseGeometry` — adds `area()`, which raises `Exception` |
| `7-base_geometry.py` | `BaseGeometry` — adds `integer_validator(name, value)` |
| `8-rectangle.py` | `Rectangle` — inherits from `BaseGeometry`; private `width`/`height` validated on init |
| `9-rectangle.py` | `Rectangle` — adds `area()` and `__str__()` |
| `10-square.py` | `Square` — inherits from `Rectangle`; private `size` |
| `11-square.py` | `Square` — adds `__str__()` |

## Usage

Each file can be run directly, or imported and tested via the
corresponding `X-main.py` style script, e.g.:

```
$ ./9-main.py
[Rectangle] 3/5
15
```

## Author

Higher Level Programming — Inheritance project.
