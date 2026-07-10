#!/usr/bin/python3
"""Module that divides two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element two lists.

    Args:
        my_list_1 (list): the list of numerators.
        my_list_2 (list): the list of denominators.
        list_length (int): the length of the resulting list.

    Returns:
        A new list of length list_length, where each element is the
        division of the corresponding elements of my_list_1 and
        my_list_2, or 0 if the division could not be performed.
    """
    new_list = []

    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)

    return new_list
