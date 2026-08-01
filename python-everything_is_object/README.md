# Python - Everything is Object

## Description

This project is a deep dive into how Python actually represents variables,
objects, and identity under the hood — `id`, `type`, mutable vs. immutable
objects, aliasing, and how arguments are passed to functions. Rather than
building a program, most tasks are short, single-line answers to
"what does this print / are these the same object" style questions, meant
to expose the subtleties of references vs. values in Python.

## Requirements

* Ubuntu 20.04 LTS, Python 3.8.5
* `.py` files start with `#!/usr/bin/python3`, are executable, and follow
  `pycodestyle` (version 2.7.*)
* `.txt` answer files contain no shebang, are exactly one line long, with
  no leading or trailing spaces, and end with a newline

## Files

| File | Description |
| --- | --- |
| `0-answer.txt` | Function used to print the type of an object |
| `1-answer.txt` | Function used to get an object's identifier |
| `2-answer.txt` – `5-answer.txt` | Whether two integer variables share the same object |
| `6-answer.txt` – `13-answer.txt` | `==` vs `is` for strings and lists |
| `14-answer.txt` – `18-answer.txt` | Effects of mutation, reassignment, and function calls on lists/ints |
| `19-copy_list.py` | `copy_list(l)` — returns a shallow copy of a list |
| `20-answer.txt` – `23-answer.txt` | What actually makes a tuple a tuple |
| `24-answer.txt` – `26-answer.txt` | Object identity for tuples, evaluated interactively |
| `27-answer.txt`, `28-answer.txt` | Whether `+` vs `+=` on a list changes its identity |

## Notes

* A number of the "is"-based answers (tasks 6–13, using `print(... is ...)`)
  were verified by running each snippet as a standalone script, since
  CPython's compiler folds identical constant literals within a single
  code object.
* Tasks 24–26 use bare expressions with no `print()`, matching genuine
  interactive REPL usage — where each line is compiled separately, so
  constant folding does *not* apply across statements the way it does in
  a script. This is why, for example, two identical two-element tuple
  literals are **not** the same object in the REPL (task 25) even though
  they would appear to be if pasted into a single script file.
* `19-copy_list.py`'s parameter is named `l` per the required function
  signature (`def copy_list(l):`), which triggers pycodestyle's E741
  ("ambiguous variable name") warning — this is a known, unavoidable
  side effect of the task's fixed signature, not a style oversight.

## Author

ALU Higher Level Programming - python-everything_is_object project
