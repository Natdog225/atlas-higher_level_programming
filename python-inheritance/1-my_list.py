#!/usr/bin/python3
"""Defines the MyList class, inheriting from list.

Example:
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]
    >>> print(my_list)
    [1, 4, 2, 3, 5]

"""


class MyList(list):
    """A subclass of list that has a print_sorted method.

    Example:
        >>> my_list = MyList()
        >>> my_list.extend([3, 1, 4, 2])
        >>> my_list.print_sorted()
        [1, 2, 3, 4]

    """

    def print_sorted(self):
        """Prints the list elements in ascending sorted order.

        Example:
            >>> my_list = MyList()
            >>> my_list.extend([3, 1, 4, 2])
            >>> my_list.print_sorted()
            [1, 2, 3, 4]

        """
        print(sorted(self))