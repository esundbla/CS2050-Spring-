import unittest
import time


class Mammal:
    """ A Mammal class to further populate our animal kingdom """

    def __init__(self, species):
        """ mammal constructor can initialize class attributes """
        self.species = species
        self.name = None

    def eat(self, food):
        """ a method that will 'eat' in O(n) time """
        i = food
        print(self.name, "the", self.species, "is about to eat")
        while i >= 1:
            time.sleep(0.1)
            print('.')
            i = i // 2
        print("    ", self.name, "is done eating!")

    def makeNoise(self):
        """ a method that should be implemented by children classes """
        raise NotImplementedError("this method should be implemented by child class")

    def getName(self):
        """getter for animals name"""
        return self.name

    def __eq__(self, other):
        """ overiding the equals opperator """
        if(self.name == other.name):
            return True
        else:
            return False


class Hippo(Mammal):
    """  a specific child class of Mammal """
    def __init__(self, species):
        super().__init__(species)
        self.name = "Hippo"

    def makeNoise(self):
        return ("YYAAWWWNNNN")


class Elephant(Mammal):
    """  a specific child class of Mammal """
    def __init__(self, species):
        super().__init__(species)
        self.name = "Elephant"

    def makeNoise(self):
        return ("MUNCH MUNCH")


class TestMammals(unittest.TestCase):
    """ a class that is derived from TestCase to allow for unit tests to run """

    def testInheritance(self):
        """ confirm that Elephant and Hippo are children classes of Mammal """
        self.assertTrue(issubclass(Elephant, Mammal) and issubclass(Hippo, Mammal))

    def testNotEqual(self):
        """ testing that Elephant and Hippo aren't equal """
        self.assertTrue(Elephant != Hippo)

    def testDifferentMakeNoise(self):
        """ testing that the makeNoise of each function has a different output """
        self.assertFalse(Elephant.makeNoise(self) == Hippo.makeNoise(self))

def main():
    """ a 'main' function to keep program clean and organized """
    print("-------------------- start main --------------------")

    # create instances of child classes
    e = Elephant("Ellie")
    h = Hippo("Henry")

    # compare classes with overriden == operator, and call accessor method
    if (e == h):
        print(e.getName(), "and", h.getName(), "are of the same species")
    else:
        print(e.getName(), "and", h.getName(), "are *not* of the same species")

    # a function to help demonstrate polymorphism
    def listenToMammal(Mammal):
        print(Mammal.makeNoise())

    # polymorphism in action: treating different classes in the same way
    listenToMammal(e)
    listenToMammal(h)

    # feed Ellie 10 bites of food (and see how long it takes!)
    e.eat(10)

    print("--------------------- end main ---------------------")


# this will run when the file is called as a standalone program (ex: python assign1.py)
if __name__ == "__main__":
    main()
    unittest.main()