import random

class RandomizedSet(object):

    def __init__(self):
        self.map = {}    # value -> its index in self.values
        self.values = []   # the values, so we can pick one by index

    def insert(self, val):
        if val in self.map:
            return False
        self.values.append(val)
        self.map[val] = len(self.values) - 1
        return True

    def remove(self, val):
        if val not in self.map:
            return False

        index = self.map[val]    # where val sits in the list
        last_val = self.values[-1]     # the element we will move into its place

        self.values[index] = last_val   # overwrite val with the last element
        self.map[last_val] = index    # the moved element has a new index
        self.values.pop()         # drop the now-duplicate last slot
        del self.map[val]      # forget val
        return True

    def getRandom(self):
        return random.choice(self.values)