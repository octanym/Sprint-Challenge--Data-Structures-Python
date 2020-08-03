'''
static storage size
does not grow
when full and inserted upon the oldest element is removed to allow the inserted value
how should we determine the storage size?
the tests indicate that elements begin overwriting after e which has an index of 4
the first element is the first to be overwritten and subsequent letters are overwritten by the elemtns you wish to append that exceed
    -we will need a while loop
'''


class RingBuffer:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.storage = []
        self.length = len(self.storage)

    def append(self, item):
        # if the array isnt full append the item
        if self.length is not self.capacity:
            self.storage.append(item)
        # overwrite the item if the array is full
        # while loop to iterate over old values overwriting them

    def get(self):
        return self.storage
