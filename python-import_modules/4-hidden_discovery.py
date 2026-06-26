#!/usr/bin/python3
"""Prints all names in hidden_4 module that don't start with __"""
import hidden_4

if __name__ == "__main__":
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
