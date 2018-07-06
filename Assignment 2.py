import unittest

'''
Description: 
Author: Luis Ruiz   
Version: like 20
Help provided to: piper
Help received from: andrew and Z
'''

'''
    Implement a dictionary using chaining.
    You may assume every key has a hash() method, e.g.:
    >>> hash(1)
    1
    >>> hash('hello world')
    -2324238377118044897
'''


class Dictionary:
    def __init__(self, init=None):
        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0

        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        return self.__count

    def flattened(self):
        return [item for inner in self.__items for item in inner]

    def __iter__(self):
        return iter(self.flattened())

    def __str__(self):
        return str(self.flattened())

    def size(self):
        return self.__limit

    def __setitem__(self, key, value):
        # ''' Add to the dictionary.'''
        page = hash(key) % self.__limit
        if self.__items[page] == []:
            self.__items[page].append([key, value])
            self.__count += 1
        else:
            for i in self.__items[page]:
                if i[0] == key:
                    i[1] = value
                    return

            self.__items[page].append([key, value])
            self.__count += 1

        if self.__count / self.__limit > 0.75:
            oldhash = self.flattened()
            self.__limit *= 2
            self.__items = [[] for _ in range(self.__limit)]
            self.__count = 0
            for i in oldhash:
                self.__setitem__(i[0], i[1])

    def __getitem__(self, key):
        # ''' Retrieve from the dictionary. '''
        page = hash(key) % self.__limit

        for i in self.__items[page]:
            if i[0] == key:
                return i[1]

    def __contains__(self, key):
        # ''' Implements the 'in' operator. '''
        page = hash(key) % self.__limit
        for i in self.__items[page]:
            if i[0] == key:
                return True
        return False

    def __delete__(self, key):

        page = hash(key) % self.__limit

        for i in self.__items[page]:
            x = 0
            if i[0] == key:
                self.__count -= 1
                self.__items[page].pop(x)

        if self.__limit > 10 and self.__count / float(self.__limit) < 0.25:
            oldhash = self.flattened()
            self.__limit /= 2
            self.__items = [[] for _ in range(self.__limit)]
            self.__count = 0
            for i in oldhash:
                self.__setitem__(i[0], i[1])

    def keys(self):
        newlist = self.flattened()
        keylist = []
        for i in newlist:
            keylist.append(i[0])
        return keylist

    def values(self):
        newlist = self.flattened()
        valuelist = []
        for i in newlist:
            valuelist.append(i[1])
        return valuelist

    def items(self):
        newlist = self.flattened()
        itemlist = []
        for i in newlist:
            itemlist.append((i[0], i[1]))
        return itemlist

    def eq(self, other):
        keylist = self.keys()
        valuelist = self.values()
        klist = other.keys()
        vlist = other.values()
        if len(keylist) != len(klist):
            return False
        if len(valuelist) != len(vlist):
            return False

        while i != len(klist):
            if keylist[i] != klist[i]:
                return False
            if valuelist[i] != vlist[i]:
                return False
            i += 1
        return True
    ''' C-level work '''


class test_add_two(unittest.TestCase):
    def test(self):
        s = Dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")


class test_add_twice(unittest.TestCase):
    def test(self):
        s = Dictionary()
        s[1] = "one"
        s[1] = "one"
        self.assertEqual(len(s), 1)
        self.assertEqual(s[1], "one")


class test_store_false(unittest.TestCase):
    def test(self):
        s = Dictionary()
        s[1] = False
        self.assertTrue(1 in s)
        self.assertFalse(s[1])


class test_store_none(unittest.TestCase):
    def test(self):
        s = Dictionary()
        s[1] = None
        self.assertTrue(1 in s)
        self.assertEqual(s[1], None)


class test_none_key(unittest.TestCase):
    def test(self):
        s = Dictionary()
        s[None] = 1
        self.assertTrue(None in s)
        self.assertEqual(s[None], 1)


class test_False_key(unittest.TestCase):
    def test(self):
        s = Dictionary()
        s[False] = 1
        self.assertTrue(False in s)
        self.assertEqual(s[False], 1)


class test_collide(unittest.TestCase):
    def test(self):
        s = Dictionary()
        s[0] = "zero"
        s[10] = "ten"
        self.assertEqual(len(s), 2)
        self.assertTrue(0 in s)
        self.assertTrue(10 in s)

class test_size(unittest.TestCase):
    def test(self):
        s = Dictionary(
            [[0, "a"], [1, "b"], [2, "c"], [3, "d"],
            [4, "e"], [5, "f"], [6, "g"], [7, "h"], [8, "i"],
            [9, "j"], [10, "k"], [11, "l"], [12, "m"], [13, "n"],
            [14, "o"], [15, "p"], [16, "q"], [17, "r"],
            [18, "s"], [19, "t"]])
        self.assertTrue(3 in s)
        self.assertEqual(s[5], "f")
        self.assertEqual(s.size(), 40)

class test_remove(unittest.TestCase):
    def test(self):
        s = Dictionary(
            [[0, "a"], [1, "b"], [2, "c"], [3, "d"],
             [4, "e"], [5, "f"], [6, "g"], [7, "h"], [8, "i"],
             [9, "j"], [10, "k"], [11, "l"], [12, "m"], [13, "n"],
             [14, "o"], [15, "p"], [16, "q"], [17, "r"],
             [18, "s"], [19, "t"]])
        self.assertTrue(4 in s)
        s.__delete__(4)
        self.assertFalse(4 in s)
        self.assertEqual(len(s), 19)

class test__halve(unittest.TestCase):
    def test(self):
        s = Dictionary(
            [[0, "a"], [1, "b"], [2, "c"], [3, "d"],
             [4, "e"], [5, "f"], [6, "g"], [7, "h"], [8, "i"],
             [9, "j"]])
        self.assertTrue(6 in s)
        self.assertEqual(s[5], 'f')
        self.assertEqual(s.size(), 20)
        s.__delete__(1)
        s.__delete__(2)
        s.__delete__(3)
        s.__delete__(4)
        s.__delete__(5)
        s.__delete__(6)
        s.__delete__(7)
        self.assertEqual(len(s), 3)
        self.assertEqual(s.size(), 10)

class test_keys(unittest.TestCase):
    def test(self):
        s = Dictionary([[0, "a"], [1, "b"], [2, "c"], [3, "d"], [4, "e"]])
        self.assertEqual(s.keys(), [0, 1, 2, 3, 4])

class test_values(unittest.TestCase):
    def test(self):
        s = Dictionary([[0, "a"], [1, "b"], [2, "c"], [3, "d"], [4, "e"]])
        self.assertEqual(s.values(), ["a", "b", "c", "d", "e"])

class test_eq(unittest.TestCase):
    def test(self):
        s = Dictionary([[0, "a"], [1, "b"], [2, "c"], [3, "d"], [4, "e"]])
        a = Dictionary([[0, "a"], [1, "b"], [2, "c"], [3, "d"], [4, "e"]])
        self.assertTrue(s == a)
        a.__delete__(3)
        self.assertFalse(s == a)

class test_items(unittest.TestCase):
    def test(self):
        s = Dictionary([[0, "a"], [1, "b"], [2, "c"], [3, "d"], [4, "e"]])
        self.assertEqual(s.items(), [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e")])

if __name__ == '__main__':
    unittest.main()

