# importing copy module
import copy


class Stack(object):
    """
    class variables
    """
    items = []
    sp = -1

    def __init__(self):
        self.sp = -1
        self.items = [0] * 10

    def __del__(self):
        pass

    def push(self, item):
        self.sp += 1
        self.items[self.sp] = item

    def pop(self):
        self.sp -= 1
        return self.items[self.sp]

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.sp == -1

    def createIterator(self):
        return object.__new__(StackIter)

    """
        overloaded '==' operator
    """

    def __eq__(self, other):

        """// 3. Clients ask the container object to create an iterator object"""
        # itl = StackIter()
        # itr = StackIter()
        itl = self.createIterator()
        itr = other.createIterator()

        """
        Print values for debugging purposes
        """
        print("Left Values:")
        print("itl.first()", itl.first())
        print("itl.isDone()", itl.isDone())
        print("not itl.isDone()", not itl.isDone())
        print("itl.next()", itl.next())
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        print("Right Values:")
        print("itr.first()", itr.first())
        print("itr.isDone()", itr.isDone())
        print("not itr.isDone()", not itr.isDone())
        print("itr.next()", itr.next())
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        print("rngl", range(itl.first(), (not itl.isDone()), itl.next()))
        print("rngr", range(itr.first(), (not itr.isDone()), itr.next()))

        """// 4. Clients use the first(), isDone(), next(), and currentItem() protocol"""
        """for i, j in zip(range(x), range(y)):   simultaneous loop"""
        for i, j in zip(range(itl.first(), (not itl.isDone()), itl.next()),
                        range(itr.first(), (not itr.isDone()), itr.next())):
            print("============================================================")
            print(itl.first(), (not itl.isDone()), itl.next())
            print(itr.first(), (not itr.isDone()), itr.next())
            print("============================================================")
            b = itr.currentItem()
            a = itl.currentItem()

            if itl.currentItem() != itr.currentItem():
                pass
        ans = (itl.isDone() & itr.isDone())
        del itl
        del itr
        return ans


class StackIter(object):
    """
    class variables
    """
    __stk = Stack()
    __index = -1

    """
    class constructor
    """

    def __init__(self):
        self.__stk = self
        self._index = -1

    def __del__(self):
        pass

    """
    class methods
    """

    def first(self):
        self.__index = 0
        return self.__index

    def next(self):
        return self.__index + 1

    def isDone(self):
        self.__stk.sp += 1
        var = self.__stk.sp == self.__index
        return var

    def currentItem(self):
        i = self.__index
        s = self.__stk.size()
        return self.__stk.items[self.__index]


def createIterator():
    return object.__new__(StackIter)


if __name__ == '__main__':

    s1 = Stack()
    # for i in range(2, 5, 1):
    for i in range(2, 5):
        s1.push(i)

    """
        s3-s5 same as s1
    """
    s2 = copy.deepcopy(s1)
    s3 = copy.deepcopy(s1)
    s4 = copy.deepcopy(s1)
    s5 = copy.deepcopy(s1)
    """
        test the stack operations
    """
    s3.pop()
    s5.pop()
    s4.push(2)
    s5.push(9)

    """
        Demonstrate overloaded operator
    """
    print("1 == 2", (s1 == s2))
    print("1 == 3", (s1 == s3))
    print("1 == 4", (s1 == s4))
    print("1 == 5", (s1 == s5))
