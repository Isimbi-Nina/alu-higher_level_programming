# python-exceptions

This project covers Python errors and exceptions: how to catch them with
`try`/`except`/`finally`, and how to raise built-in exceptions.

## Learning Objectives

At the end of this project, you should be able to explain:

- Why Python programming is awesome
- The difference between errors and exceptions
- What exceptions are and how to use them
- When exceptions are needed
- How to correctly handle an exception
- The purpose of catching exceptions
- How to raise a built-in exception
- When a clean-up action is needed after an exception

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files end with a new line
- The first line of every file is exactly `#!/usr/bin/python3`
- Code follows `pycodestyle` (version 2.7.*)
- All files are executable
- No modules are imported unless explicitly permitted

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-safe_print_list.py` | Print x elements of a list, catching `IndexError` |
| 1 | `1-safe_print_integer.py` | Print a value as an integer, catching `ValueError`/`TypeError` |
| 2 | `2-safe_print_list_integers.py` | Print and count only integers in a list |
| 3 | `3-safe_print_division.py` | Divide two integers, printing the result in `finally` |
| 4 | `4-list_division.py` | Divide two lists element by element |
| 5 | `5-raise_exception.py` | Raise a `TypeError` exception |
| 6 | `6-raise_exception_msg.py` | Raise a `NameError` exception with a message |
| 7 | `100-safe_print_integer_err.py` | Print a value as an integer, reporting errors to stderr |
| 8 | `101-safe_function.py` | Execute a function safely, catching any exception it raises |
| 9 | `102-magic_calculation.py` | Reproduce a given Python bytecode as a function |

## Usage

Each task has a corresponding `N-main.py` file demonstrating usage, e.g.:

```
./0-main.py
```
