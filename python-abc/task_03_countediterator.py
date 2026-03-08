#!/usr/bin/python3
"""
This module defines the CountedIterator class which extends the
behavior of a standard iterator by keeping track of the count
of items iterated.
"""


class CountedIterator:
    """
    Iterator class that counts the number of items fetched.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and the counter.

        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the number of items that have been iterated so far.
        """
        return self.count

    def __next__(self):
        """
        Fetches the next item and increments the counter.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
