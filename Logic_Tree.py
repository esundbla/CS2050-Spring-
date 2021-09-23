from binarytree import BinaryTree  # binarytree.py on github
from stack import Stack            # stacks.py also on github
import unittest
import random


def buildProbParseTree(fpexp):
    """ This Function constructs a binary logic tree utilizing the binary tree class and stack class
    The combination of classes functions as structure and navigation for the tree.
    The logical expression use 4 inputs (T:True, F:False, U_x:Unlikely, L_x:Likely) and two operator
    (AND, OR) parenthesis are used to denote order of opp and that an operator will be present in equation
    """
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:

        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['AND', 'OR']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i in ['T', 'F']:
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent

        # Testing for valid x for Likely and Unlikely values
        elif i[0] == 'U':
            num = float(i[2:])
            if num > 0.5:
                print(num, "Is greater than 0.5 invalid for U icon")
                exit(1)
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent

        elif i[0] == 'L':
            num = float(i[2:])
            if num < 0.5:
                print(num, "Is less than 0.5 invalid for L icon")
                exit(1)
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent

        elif i == ')':
            currentTree = pStack.pop()

        else:
            print("token '{}' is not a valid input".format(i))
            return None

    return eTree


def returnValue(instring):
    """ Uses the 4 possible inputs and returns the probability of that given input """
    if isinstance(instring, float):
        return instring
    elif instring == 'T':
        return 1.0
    elif instring == 'F':
        return 0.0
    elif instring[0] == 'U':
        num = float(instring[2:])
        return num
    elif instring[0] == 'L':
        num = float(instring[2:])
        return num


def AND(p1, p2):
    """ probability calculator for AND operator """
    val1 = returnValue(p1)
    val2 = returnValue(p2)
    return val1 * val2


def OR(p1, p2):
    """ probability calculator for OR operator """
    val1 = returnValue(p1)
    val2 = returnValue(p2)
    return (val1 + val2) - (val1 * val2)


def evaluateProb(parseTree):
    """ recursively evaluates the probability from tree and returns it as a decimal number """
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        if parseTree.getRootVal() == 'AND':
            return AND(evaluateProb(leftC), evaluateProb(rightC))
        elif parseTree.getRootVal() == 'OR':
            return OR(evaluateProb(leftC), evaluateProb(rightC))
    else:
        return parseTree.getRootVal()


def evaluateProbLogicParseTree(parseTree):
    """ Uses evaluated probability and random to generate True or False"""
    prob = 100 * evaluateProb(parseTree)
    rand = random.randint(0, 100)
    if rand <= prob:
        return True
    else:
        return False


def printProbLogicExpression(tree):
    """ Recursively calls down Tree and creates output string to represent given equation """
    sVal = ""
    if tree:
        sVal = '(' + printProbLogicExpression(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printProbLogicExpression(tree.getRightChild())+')'
    return sVal


class TestParseTreeFunctions(unittest.TestCase):
    # testing basic logic
    def testEval(self):
        input_str = "( T OR F )"
        pt = buildProbParseTree(input_str)
        result = evaluateProbLogicParseTree(pt)
        self.assertEqual(result, True)

    def testEvalProb(self):
        # testing probability calculation
        input_str = "( T AND L_0.8 )"
        pt = buildProbParseTree(input_str)
        result = evaluateProb(pt)
        self.assertEqual(result, 0.80)

    def testOutput(self):
        # testing print function
        input_str = "( T AND L_0.8 )"
        pt = buildProbParseTree(input_str)
        result = printProbLogicExpression(pt)
        self.assertEqual(result, "((T)AND(L_0.8))")


def main():
    """ Testing two possible inputs and there function results """
    input_str = "( U_0.5 OR ( L_0.8 AND T ) )"
    pt = buildProbParseTree(input_str)
    print("Evaluating parse tree...", evaluateProbLogicParseTree(pt))
    print(printProbLogicExpression(pt))
    input_str2 = "( ( ( L_0.8 AND T ) OR U_0.25 ) OR ( U_0.3 AND F ) )"
    pt2 = buildProbParseTree(input_str2)
    print("Evaluating parse tree...", evaluateProbLogicParseTree(pt2))
    print(printProbLogicExpression(pt2))


# unittest_main() - run unittest's main, which runs TestParseTreeFunctions's methods
def unittest_main():
    print("-"*25, "running unit tests", "-"*25)
    unittest.main()


# evaluates to true if run as standalone program (e.g. $ python hashtable.py)
if __name__ == '__main__':
    main()
    unittest_main()
