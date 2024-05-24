"""
New class CountedIterator
"""


class CountedIterator:
    """
    This class extends the built in iterator obtained from the iter
    function. And keeps track of the number of items iterated over.
    """
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        return self.count
