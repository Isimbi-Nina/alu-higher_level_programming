# python-data_structures

Higher Level Programming project on Python data structures: lists, tuples,
and how they map to concepts learned in C (indexing, bounds checking,
copies vs. references).

## Description

This project covers the basics of working with lists and tuples in Python,
with an emphasis on doing things "the C way" — manual bounds checking, no
`try`/`except`, no built-ins that trivialize the task — to build intuition
for what Python is doing under the hood.

## Requirements

- Editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3+)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should follow the `pycodestyle` style guide (version 2.8.*)
- All files must be executable
- All modules should have a documentation string
- All functions should have a documentation string
- All files must have exactly one function or class (unless noted otherwise)

## Files

| File | Description |
| --- | --- |
| `0-print_list_integer.py` | Prints all integers of a list, one per line |
| `1-element_at.py` | Retrieves an element from a list like in C (bounds-checked) |
| `2-replace_in_list.py` | Replaces an element of a list at a given position |
| `3-print_reversed_list_integer.py` | Prints all integers of a list in reverse order |
| `4-new_in_list.py` | Replaces an element in a list without modifying the original |
| `5-no_c.py` | Removes all `c` and `C` characters from a string |
| `6-print_matrix_integer.py` | Prints a matrix of integers |
| `7-add_tuple.py` | Adds two tuples together |
| `8-multiple_returns.py` | Returns the length and first character of a string |
| `9-max_integer.py` | Finds the biggest integer in a list |
| `10-divisible_by_2.py` | Finds all multiples of 2 in a list |
| `11-delete_at.py` | Deletes the item at a specific position in a list |
| `12-switch.py` | Switches the values of two variables |

Each `N-*.py` task file has a matching `N-main.py` test script (tasks 0-11)
demonstrating expected usage and output
