import unittest


class binary_search_tree:
    def __init__(self, init=None):
        self.__value = self.__left = self.__right = None

        if init:
            for i in init:
                self.add(i)

    def __iter__(self):
        if self.__left:
            for node in self.__left:
                yield (node)

        yield (self.__value)

        if self.__right:
            for node in self.__right:
                yield (node)

    def __str__(self):
        return (','.join(str(node) for node in self))

    def add(self, value):
        if self.__value is None:
            self.__value = value

        elif value < self.__value:
            if self.__left:
                self.__left.add(value)
            else:
                self.__left = binary_search_tree([value])

        else:
            if self.__right:
                self.__right.add(value)
            else:
                self.__right = binary_search_tree([value])

        # if this is the first value for this node, just set to node's value
        # if the value is less than this node's value
        # if there isn't a left
        # create a new tree and have left refer to it
        # else
        # make a recursive call
        # else
        # if there isn't a right...

    def preorder(self):
        queue = []
        queue += [self.__value]
        if self.__left:
            queue += self.__left.preorder()
        if self.__right:
            queue += self.__right.preorder()
        return queue

    def inorder(self):
        Q = []
        if self.__left:
            Q += self.__left.inorder()
        Q += [self.__value]
        if self.__right:
            Q += self.__right.inorder()
        return Q

    def postorder(self):
        Q = []
        if self.__left:
            Q += self.__left.postorder()
        if self.__right:
            Q += self.__right.postorder()
        Q += [self.__value]
        return Q

    def BFS(self):
        if self.__value is None:
            return [None]
        else:
            Q = [self]
            resultlist = []
            while Q:
                node = Q.pop(0)
                resultlist += [node.__value]
                if node.__left is not None:
                    Q += [node.__left]
                if node.__right is not None:
                    Q += [node.__right]
            return resultlist

        # create a Q with the root element, and an empty list
        # while there are nodes in the Q
        # grab the first one and add it to the result list
        # if there is a node to the left, add that to the Q
        # if there is a node to the right, add that to the Q


        # if self is the value to delete
        # if this is a leaf, remove reference to self in parent
        # if there isn't a left, replace self in the parent with the right
        # if there isn't a right, replace self in the parent with the left
        # tricky bit. first, find the right-most of the left hand tree
        # and do a recursive call to remove it
        # else if the value passed in is smaller, recurse to the left
        # else recurse to the right


class test_binary_search_tree(unittest.TestCase):
    '''
           20
          /  \
        10   30
            /  \
           25  35
    '''

    # C level
    def test_empty(self):
        self.assertEqual(str(binary_search_tree()), 'None')

    def test_one(self):
        self.assertEqual(str(binary_search_tree([1])), '1')

    def test_add(self):
        bt = binary_search_tree()
        bt.add(20)
        bt.add(10)
        bt.add(30)
        bt.add(25)
        bt.add(35)
        self.assertEqual(str(bt), '10,20,25,30,35')

    def test_init(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(str(bt), '10,20,25,30,35')

    # B level

    def test_empty_inorder(self):
        self.assertEqual(binary_search_tree().inorder(), [None])

    def test_inorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.inorder(), [10, 20, 25, 30, 35])

    def test_preorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(list(bt.preorder()), [20, 10, 30, 25, 35])

    def test_postorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.postorder(), [10, 25, 35, 30, 20])

    # A level

    def test_empty_BFS(self):
        self.assertEqual(binary_search_tree().BFS(), [None])
    def test_BFS(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.BFS(), [20, 10, 30, 25, 35])


if '__main__' == __name__:
    unittest.main()