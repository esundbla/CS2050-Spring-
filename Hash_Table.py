import unittest


class HashTable:
    """
    A class implementing a basic hash table / hash map / associative array / etc.
    This is essentially the same as a Python dict(tionary) but by implementing
    our own version we will better understand how hash tables work internally.

    A note to resolve the issues with deleting and item and not being able to find
    a second item that was moved due to a collision -1 is assigned to any deleted item and
    is no longer a valid key value
    """

    def __init__(self, size):
        """ Constructor initiates the lists of "keys" and "data" and its size along with counters and a prime list
        for resizing """
        self.size = size
        # any table size smaller than 11 will automatically be resized to 11 upon first resizing
        self.next_largest = 11
        self.primes = [2, 3, 5, 7, 9, 11]
        self.item_count = 0
        self.key_slots = [None] * self.size
        self.data_slots = [None] * self.size

    def resize(self):
        """ Resizes our hashtable to the next largest prime number and then rehashes already entered key/data pairs """
        not_found = True
        not_prime = True

        while not_found:
            # checks to not mistakenly resize to smaller table then if valid rehashes into new larger table
            if self.next_largest > self.size:
                self.size = self.next_largest
                temp_keys = self.key_slots
                temp_data = self.data_slots
                self.key_slots = [None] * self.size
                self.data_slots = [None] * self.size
                self.item_count = 0
                for i in range(0, len(temp_keys)):
                    if temp_keys[i] is not None:
                        self.put(temp_keys[i], temp_data[i])
                not_found = False
            else:
                # code to find next prime for resizing
                while not_prime:
                    self.next_largest += 1
                    for n in self.primes:
                        if self.next_largest % n == 0:
                            break
                        else:
                            self.primes.append(self.next_largest)
                            not_prime = False

    def put(self, key, data):
        """ Insert data at assigned key location if key already exists replace corresponding data  """
        # Needed the value -1 for deletion entry so no longer valid key value
        if key == -1:
            print("Invalid key entry")
            return
        self.item_count += 1
        hashvalue = self.hash(key)

        # an empty slot, so go ahead and add key and data
        if self.key_slots[hashvalue] == None or self.key_slots[hashvalue] == -1:
            self.key_slots[hashvalue] = key
            self.data_slots[hashvalue] = data
        # slot was occupied, so figure out what to do next
        else:
            # key is same as the key currently in this slot, so
            # replace data with the new data that was passed in
            if self.key_slots[hashvalue] == key:
                self.data_slots[hashvalue] = data
            # there was a collision with a different key, so use linear probing
            else:
                nextslot = self.rehash(hashvalue)
                while self.key_slots[nextslot] != None and self.key_slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.key_slots[nextslot] == None:
                    self.key_slots[nextslot] = key
                    self.data_slots[nextslot] = data
                else:
                    self.data_slots[nextslot] = data
        # after every addition check for load factor if load is excess 50% then resize the table
        if self.item_count > (self.size // 2):
            self.resize()

    def hash(self, key):
        """ Hash function utilizing simple modular logic """
        return key % self.size

    def rehash(self, oldhash):
        """ Rehash for instances of collisions inside hash table """
        return (oldhash + 3) % self.size

    def get(self, key):
        """ get function to return the data for a given key or None if not found uses comparison for collisoin
        handling """
        startslot = self.hash(key)

        data = None
        stop = False
        found = False
        position = startslot
        while self.key_slots[position] != None and not found and not stop:
            if self.key_slots[position] == key:
                found = True
                data = self.data_slots[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        """ Overrides the [] get operator with our get function """
        return self.get(key)

    def __setitem__(self, key, data):
        """ Overrides our [] set operator with our put function  """
        self.put(key, data)

    def __len__(self):
        """ Overrides len function to return number of key pairs stored """
        return self.item_count

    def __contains__(self, key):
        """ Checks our table for the existence of a given key and returns boolean """
        test = self.get(key)
        if test == None:
            return False
        else:
            return True

    def __delitem__(self, key):
        """ Overrides delete operator to remove key,data pair of given key returns boolean of successful deletion """
        # Tests validity of key for deletion and returns a Exception when invalid key given
        if key not in self.key_slots:
            raise Exception("Error Invalid key for deletion")

        hashvalue = self.hash(key)
        found = False
        # Code to check that the correct key/data pair has been found to delete and if not rehash till found
        while not found:
            if self.key_slots[hashvalue] == key:
                self.key_slots[hashvalue] = -1
                self.data_slots[hashvalue] = None
                self.item_count -= 1
                found = True
            else:
                hashvalue = self.rehash(hashvalue)

    def loadFactor(self):
        """ Returns a float value (too 2 places) of the current % load of our table"""
        return round(self.item_count/self.size, 2)




class TestHashTable(unittest.TestCase):
    """ Extend unittest.TestCase and add methods to test HashTable """

    def testKeysAfterPuts(self):
        """ Check that hashtable keys are as expected for a simple case """
        h = HashTable(7)
        h[6] = 'cat'
        h[29] = 'dog'
        expected = [None, 29, None, None, None, None, 6]
        self.assertEqual(h.key_slots, expected)

    def testLenOverride(self):
        """ Tests the correct return length value """
        h = HashTable(11)
        h[5] = ''
        h[7] = ''
        h[22] = ''
        self.assertEqual(len(h), 3)

    def testReSize(self):
        """ Tests that the resize produces the appropriate size hash """
        h = HashTable(5)
        h[3] = ''
        h[5] = ''
        h[37] = ''
        self.assertEqual(len(h.key_slots), 11)


def main():
    """ run any example/demo you want to when running as standalone program """
    h = HashTable(7)
    h[7] = 'cat'
    h[14] = 'dog'
    h[21] = 'bird'
    h[49] = 'snake'
    h[28] = 'man'
    # testing invalid key entry
    h[-1] = 'eagle'
    print(3 in h)
    print(55 in h)

    print("-" * 26, "keys and values:", "-" * 26)
    print(h.key_slots)
    print(h.data_slots)
    print(len(h))
    print(h.loadFactor())
    del h[7]
    #print(h.get(22))
    #del h[12] testing the Exception for invalid deletion
    print(h.key_slots)
    print(h.data_slots)
    print(len(h))
    print(h.loadFactor())
    print(h[16] == 'cat')


def unittest_main():
    """ run unittest's main, which will run TestHashTable's methods """
    print("-" * 25, "running unit tests", "-" * 25)
    unittest.main()


# evaluates to true if run as standalone program (e.g. $ python hashtable.py)
if __name__ == '__main__':
    main()
    unittest_main()
