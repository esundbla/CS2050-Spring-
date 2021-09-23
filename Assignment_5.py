from binarytree import BinaryTree  # binarytree.py on github
from stack import Stack            # stacks.py also on github
import operator
import unittest
import random


def buildParseTree(fpexp):
    """
    Builds a binary tree from an input string
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

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i.isnumeric():
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent

        elif i == ')':
            currentTree = pStack.pop()

        else:
            print("token '{}' is not a valid integer".format(i))
            return None

    return eTree


def evaluate(parseTree):
    """
    Evaluates the contents of the tree
    """
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()


def printExpression(tree):
    """
    Prints the tree as a string close to the original
    """
    sVal = ""
    if tree:
        sVal = '(' + printExpression(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printExpression(tree.getRightChild())+')'
    return sVal


def buildProbLogicParseTree(s):
    """
    Builds a binary tree from an input string
    """
    fplist = s.split()
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

        elif 'L' in i:
            temp = i.split('_')
            currentTree.setRootVal(temp[0])
            if float(temp[1]) >= 0.5:
                currentTree.insertRight(temp[1])
            elif float(temp[1]) < 0.5:
                print("token '{}' is not a valid integer".format(i))
            parent = pStack.pop()
            currentTree = parent

        elif 'U' in i:
            temp = i.split('_')
            currentTree.setRootVal(temp[0])
            if float(temp[1]) < 0.5:
                currentTree.insertLeft(temp[1])
            elif float(temp[1]) >= 0.5:
                print("token '{}' is not a valid integer".format(i))
            parent = pStack.pop()
            currentTree = parent

        elif i == ')':
            currentTree = pStack.pop()

        else:
            print("token '{}' is not a valid integer".format(i))
            return None

    return eTree


def evaluateProbLogicParseTree(t):
    """
    Evaluates the contents of the tree
    """
    opers = {'AND':operator.and_, 'OR':operator.or_}

    leftC = t.getLeftChild()
    rightC = t.getRightChild()

    # Converts 'T' and 'F' nodes to be True and False respectively
    if t.getRootVal() == 'T':
        t.setRootVal(True)
    elif t.getRootVal() == 'F':
        t.setRootVal(False)

    # Handles 'L' nodes
    if not leftC and rightC:
        temp = t.getRightChild()
        chance = float(temp.getRootVal())
        r = random.random()
        if r <= chance:
            return True
        else:
            return False

    # Handles 'U' nodes
    elif leftC and not rightC:
        temp = t.getLeftChild()
        chance = float(temp.getRootVal())
        r = random.random()
        if r <= chance:
            return True
        else:
            return False

    # Handles operator nodes
    if leftC and rightC:
        fn = opers[t.getRootVal()]
        return fn(evaluateProbLogicParseTree(leftC), evaluateProbLogicParseTree(rightC))
    else:
        return t.getRootVal()


def printProbLogicExpression(t):
    """
    Prints the tree as a string close to the original
    """
    sVal = ""
    if t:
        # Handles proper formatting of 'T' and 'F'
        if str(t.getRootVal()) == 'True':
            sVal = '(T)'
        elif str(t.getRootVal()) == 'False':
            sVal = '(F)'

        # Handles of L_x and U_x tokens
        elif not t.getLeftChild() and t.getRightChild():
            prob = t.getRightChild()
            sVal = '(' + str(t.getRootVal()) + '_' + str(prob.getRootVal()) + ')'
        elif t.getLeftChild() and not t.getRightChild():
            prob = t.getLeftChild()
            sVal = '(' + str(t.getRootVal()) + '_' + str(prob.getRootVal()) + ')'

        else:
            sVal = '( ' + printProbLogicExpression(t.getLeftChild())
            sVal = sVal + ' ' + str(t.getRootVal()) + ' '
            sVal = sVal + printProbLogicExpression(t.getRightChild()) + ' )'
    return sVal


class TestParseTreeFunctions(unittest.TestCase):

    def testEval(self):
        """ Tests the evaluateProbLogicParseTree function """
        input_str = "( ( T AND F ) OR T )"
        pt = buildProbLogicParseTree(input_str)
        result = evaluateProbLogicParseTree(pt)
        self.assertEqual(result, True)

    def testPrint(self):
        """ Tests the printProbLogicExpression function """
        input_str = '( ( U_0.4 AND L_0.8 ) OR U_0.1 )'
        pt = buildProbLogicParseTree(input_str)
        result = printProbLogicExpression(pt)
        self.assertEqual(result, '( ( (U_0.4) AND (L_0.8) ) OR (U_0.1) )')


def main():
    input_str = '( ( T AND F ) OR U_0.3 )'
    pt = buildProbLogicParseTree(input_str)
    print("Evaluating parse tree...", evaluateProbLogicParseTree(pt))
    print(printProbLogicExpression(pt))


# unittest_main() - run unittest's main, which runs TestParseTreeFunctions's methods
def unittest_main():
    print("-"*25, "running unit tests", "-"*25)
    unittest.main()


# evaluates to true if run as standalone program (e.g. $ python hashtable.py)
if __name__ == '__main__':
    main()
    unittest_main()
