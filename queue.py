import unittest

class Queue():
    """ a queue data structure implementation """

    def __init__(self):
        """ instantiate the single field/attribute of our queue """
        self.queueList = []

    def __str__(self):
        """ override string method """
        return str(self.queueList)

    def isEmpty(self):
        """ return True if empty or False if not """
        return self.queueList == []

    def enqueue(self, new_item):
        """ add new item to the queue <-- """
        self.queueList.insert(0, new_item)

    def dequeue(self):
        """ remove item from queue --> """
        return self.queueList.pop()

    def peek(self):
        """ look at oldest item in queue"""
        return self.queueList[-1]

    def size(self):
        """ return the length """
        return len(self.queueList)


q = Queue()

q.enqueue(5)
q.enqueue(18)
q.enqueue(8)
q.enqueue(2)
q.enqueue(1)
q.enqueue(7)

print(q.dequeue())
print(q)
print(q.peek())
print(q.size())
