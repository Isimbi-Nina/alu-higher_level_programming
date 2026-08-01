# python-input_output

A collection of Python scripts exploring file input/output and JSON
serialization: reading and writing text files, converting Python data
structures to and from JSON, persisting objects to disk, and a classic
whiteboard warm-up (Pascal's triangle).

## Learning Objectives

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Requirements

- Editors: `vi`, `vim`, `emacs`
- All files interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files end with a new line
- The first line of every file is exactly `#!/usr/bin/python3`
- Code follows `pycodestyle` (version 2.7.*)
- All files are executable
- Every module, class, and function has real, descriptive documentation

## Files

| File | Description |
| --- | --- |
| `0-read_file.py` | `read_file(filename="")` — reads a UTF8 text file and prints it to stdout |
| `1-write_file.py` | `write_file(filename="", text="")` — writes/overwrites a UTF8 text file, returns chars written |
| `2-append_write.py` | `append_write(filename="", text="")` — appends to a UTF8 text file, returns chars added |
| `3-to_json_string.py` | `to_json_string(my_obj)` — returns the JSON string representation of an object |
| `4-from_json_string.py` | `from_json_string(my_str)` — returns the Python object represented by a JSON string |
| `5-save_to_json_file.py` | `save_to_json_file(my_obj, filename)` — writes an object's JSON representation to a file |
| `6-load_from_json_file.py` | `load_from_json_file(filename)` — creates an object from a JSON file |
| `7-add_item.py` | Script that appends CLI arguments to a list stored in `add_item.json` |
| `8-class_to_json.py` | `class_to_json(obj)` — returns a JSON-serializable dict of an object's attributes |
| `9-student.py` | `Student` — `first_name`, `last_name`, `age`, and `to_json()` |
| `10-student.py` | `Student` — adds `to_json(attrs=None)` attribute filtering |
| `11-student.py` | `Student` — adds `reload_from_json(json)` to restore attributes from a dict |
| `12-pascal_triangle.py` | `pascal_triangle(n)` — returns a list of lists representing Pascal's triangle |

## Usage

Each file can be run directly or imported and exercised via a
corresponding `X-main.py` style script, e.g.:

```
$ ./7-add_item.py Best School
$ cat add_item.json
["Best", "School"]
```

## Author

Higher Level Programming — Input/Output project.
