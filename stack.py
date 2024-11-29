class Stack():
    """
    The Last in First out (LIFO) Implementation Using an Array
    """
    def __init__(self, capacity=5):
        """
        Initialize an empty stack array with default capacity of 5
        """
        self.data = [None] * capacity
        self.capacity = capacity
        self.pointer = 0
        
    def push(self, item):
        """
        Add an Item to the Top of the Stack
        """
        if self.pointer == self.capacity:
            raise IndexError('Stack Over Flow!')
        else:
            self.data[self.pointer] = item
            self.pointer += 1
            