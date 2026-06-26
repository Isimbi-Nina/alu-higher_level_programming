# python-hello_world

This project is part of the **alu-higher_level_programming** repository.
It contains beginner and advanced exercises that introduce the basics of
Python scripting, Shell scripting, string manipulation, bytecode, and
compiling Python files.

## Description

The goal of this project is to get comfortable with:

- Writing and executing Python scripts from the shell
- Using environment variables inside shell and Python scripts
- String slicing, formatting, and concatenation without loops or conditionals
- Printing to `stdout` and `stderr`
- Exit status codes
- Compiling Python source files into bytecode (`.pyc`)
- Reading and reproducing Python bytecode in source form

## Requirements

- All scripts are written in **Python 3** (Ubuntu 20.04 LTS, `python3` interpreter)
- Shell scripts are written in **Bash**
- All files end with a new line
- The first line of all Python files is exactly `#!/usr/bin/python3`
- The first line of all Bash scripts is exactly `#!/bin/bash`
- All files are executable (`chmod +x`)
- Code follows `pycodestyle` (version 2.x) style guidelines where applicable

## Files

| File | Description |
| --- | --- |
| `0-run` | Shell script that runs a Python file named in `$PYFILE` |
| `1-run_inline` | Shell script that runs inline Python code stored in `$PYCODE` |
| `2-print.py` | Prints a fixed string using `print` |
| `3-print_number.py` | Prints an integer using an f-string (no casting) |
| `4-print_float.py` | Prints a float with 2-digit precision using an f-string |
| `5-print_string.py` | Prints a string 3 times, then its first 9 characters, without loops/conditionals |
| `6-concat.py` | Builds and prints a sentence by combining `str1` and `str2` |
| `7-edges.py` | Extracts substrings (first 3 letters, last 2 letters, middle) using slicing |
| `8-concat_edges.py` | Builds a sentence purely through slicing of an existing string variable (no literals) |
| `9-easter_egg.py` | Prints "The Zen of Python" using `import this` |
| `100-write.py` | Prints a message to `stderr` using `sys.write`, exits with status `1` |
| `101-compile` | Shell script that compiles a Python file named in `$PYFILE` into `$PYFILE` + `c` |
| `102-magic_calculation.py` | Python function reconstructed from given Python bytecode |

## Usage

Each script can be run directly once made executable:

```bash
chmod +x <filename>
./<filename>
```

For scripts that depend on environment variables, export the variable first:

```bash
export PYFILE=main.py
./0-run
```

```bash
export PYCODE='print(f"Best School: {88+10}")'
./1-run_inline
```


