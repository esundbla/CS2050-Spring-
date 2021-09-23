import unittest


class Node:
    """ this class will act as the container/node class for our linked list """

    def __init__(self, data):
        """ initialize fields of the Node object """
        self.data = data
        self.next = None

    def getData(self):
        """ accessor for data field """
        return self.data

    def setData(self, data):
        """ mutator to modify data field from the value initially set by the constructor """
        self.data = data

    def getNext(self):
        """ accessor for 'next' field """
        return self.next

    def setNext(self, next):
        """ modify 'next' field (it was initially set to None by the constructor) """
        self.next = next


class UnorderedList:
    """ An unordered linked list class definition using Node objects as list nodes """

    def __init__(self):
        """ constructor initializes the list to be empty """
        self.head = None

    def __str__(self):
        """ print the  current linked list in its entirety """
        current = self.head
        output = "head -> "
        while current != None:
            output = "".join((output, "[" + str(current.getData()) + "]", " -> "))
            current = current.getNext()
        output = "".join((output, "None"))
        return output

    def convert2List(self):
        """ convert the current linked list to a python list (i.e. array) """
        current = self.head
        l = list()
        while current != None:
            l.append(current.getData())
            current = current.getNext()
        return l

    def isEmpty(self):
        """ return True is the list is empty, False otherwise """
        return self.head == None

    def size(self):
        """ return the number of Nodes currently in the list """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def index(self, data):
        """ return index of the node with node.data == data if it exists, otherwise -1 """
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
                index += 1
        if found:
            return index
        else:
            return -1

    def search(self, data):
        """ return True if data exists in the list, False otherwise """
        index = self.index(data)
        if index >= 0:
            return True
        else:
            return False

    def add(self, data_to_add):
        """ add an item to the beginning of the list """
        temp_node = Node(data_to_add)
        temp_node.setNext(self.head)
        self.head = temp_node

    def append(self, data_to_append):
        """ add a node with its contents equal to data to the back of the list """
        current = self.head
        temp_node = Node(data_to_append)
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(temp_node)

    def insert(self, pos, data_to_insert):
        """ insert a node with data_to_insert into position pos in the list """

        # if data_to_insert is to be added at front of list then use add()
        if pos == 0:
            self.add(data_to_insert)

        # if it is to be added to back of the list then use append()
        elif pos == self.size():
            self.append(data_to_insert)

        # if it's to be added somewhere in between then there's a little work to do
        elif pos > 0 and pos < self.size():
            current = self.head
            previous = None
            index = 0
            temp_node = Node(data_to_insert)
            while index < pos:
                previous = current
                current = current.getNext()
                index += 1
            previous.setNext(temp_node)
            temp_node.setNext(current)

        # not a valid position to add a node
        else:
            print("not a valid position in the current list for insertion")

    def pop(self, pos=None):
        """ remove and return the node at position pos, or at the last position if pos is not given """

        # if position is not given when this method is called, then pop the last node in the list
        if pos == None:
            pos = self.size() - 1

        # check that pos given is a valid position in the list
        if 0 <= pos and pos < self.size():
            current = self.head
            previous = None
            index = 0

            # traverse list until index == pos and current == (item at that position)
            while index < pos:
                previous = current
                current = current.getNext()
                index += 1

            # bypass the current node to remove it from the list then return current
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return current.getData()

        else:
            print("not a valid position in the current list to pop from ")
            return None

    def remove(self, data_to_remove):
        """ remove node from the list that has data == data_to_remove """
        index_to_remove = self.index(data_to_remove)

        if index_to_remove >= 0:
            self.pop(index_to_remove)
        else:
            print("item, '" + str(data_to_remove) + "', not removed because it does not exist")


class OrderedList(UnorderedList):
    """ An ordered linked list class (in ascending order) that inherits from UnorderedList """

    def add(self, data_to_add):
        """
        SHOULD OVERRIDE PARENT add() METHOD TO INSERT A NEW NODE WITH data=data_to_add IN THE
        CORRECT POSITION OF THE LINKED LIST SO THAT ALL ITEMS IN THE LIST ARE STILL IN ASCENDING ORDER
        """
        super().add(data_to_add)  # DELETE THIS LINE AND ADD CORRECT OrderedList IMPLEMENTATION

    def append(self, data):
        """ add should be the only way to an insert a new item in an OrderedList object """
        print("cannot use append(data) with OrderedList")

    def insert(self, pos, data):
        """ add should be the only way to an insert a new item in an OrderedList object """
        print("cannot use insert(pos, data) with OrderedList")

    def index(self, data):
        """
        SHOULD OVERRIDE PARENT index() METHOD TO STOP EARLY WHEN ENCOUNTERING A NODE WITH
        DATA/KEY THAT IS LARGER THAN 'DATA' PARAMETER (NOTE: update these comments when done)
        """
        super().index(data)  # DELETE THIS LINE AND ADD CORRECT OrderedList IMPLEMENTATION


class TestUnorderedList(unittest.TestCase):
    """ TestCase class to hold individual unittests for our UnorderedList """

    def testAddAndAppend(self):
        self.l1 = UnorderedList()
        self.l1.add(7)
        self.l1.add(5)
        self.l1.add(15)
        self.assertEqual(self.l1.convert2List(), [5, 7, 15])

    def testInsertFront(self):
        self.l1 = UnorderedList()
        self.l1.add(7)
        self.l1.add(5)
        self.l1.append(15)
        self.l1.insert(0, 1)
        self.assertEqual(self.l1.convert2List(), [1, 5, 7, 15])

    def testInsertNearBack(self):
        self.l1 = UnorderedList()
        self.l1.add(7)
        self.l1.add(5)
        self.l1.append(15)
        # ADD NECESSARY LINE(S) TO MAKE THIS TEST PASS
        self.assertEqual(self.l1.convert2List(), [5, 7, 2, 15])

    def testInsertMiddle(self):
        self.l1 = UnorderedList()
        self.l1.add(7)
        self.l1.add(5)
        self.l1.append(15)
        self.l1.insert(1, 2)
        self.assertEqual(self.l1.convert2List(), [5, 2, 7, 15])

    def testRemoveFromFront(self):
        self.l1 = UnorderedList()
        self.l1.add(7)
        self.l1.add(5)
        self.l1.append(15)
        # ADD NECESSARY LINE(S) TO MAKE THIS TEST PASS
        self.assertEqual(self.l1.convert2List(), [7, 15])

    def testRemoveFromBack(self):
        self.l1 = UnorderedList()
        self.l1.add(7)
        self.l1.add(5)
        self.l1.append(15)
        self.l1.pop()
        self.assertEqual(self.l1.convert2List(), [5, 7])

    def testRemoveFromMiddle(self):
        self.l1 = UnorderedList()
        self.l1.add(7)
        self.l1.add(5)
        self.l1.append(15)
        self.l1.pop(1)
        self.assertEqual(self.l1.convert2List(), [5, 15])

    def testRemoveSpecificData(self):
        self.l1 = UnorderedList()
        self.l1.add(7)
        self.l1.add(5)
        self.l1.append(15)
        self.l1.remove(7)
        self.assertEqual(self.l1.convert2List(), [5, 15])


class TestOrderedList(unittest.TestCase):
    """ TestCase class to hold individual unittests for our OrderedList """

    def testAdd(self):
        self.l1 = OrderedList()
        self.l1.add(7)
        self.l1.add(5)
        self.l1.add(6)
        self.assertEqual(self.l1.convert2List(), [5, 6, 7])


if __name__ == '__main__':
    unittest.main()