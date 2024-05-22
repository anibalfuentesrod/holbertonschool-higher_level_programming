#!/usr/bin/python3

class MyList(list):
    """A list that includes a method to print the list in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
