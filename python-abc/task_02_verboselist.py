"""
New class Verboselist
"""


class VerboseList(list):
    """
    A custom list class tha prints when items get added and deleted
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, iterable):
        super().extend(iterable)
        num_items = len(iterable)
        print("Extended the list with [{}] items".format(num_items))

    def remove(self, item):
        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            popped_item = super().pop()
            print("Popped [{}] from the list".format(popped_item))
            return popped_item
        else:
            popped_item = super().pop(index)
            print("Poppped [{}] from the list".format(popped_item))
            return popped_item
