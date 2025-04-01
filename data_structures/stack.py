from abc import abstractmethod
from typing import TypeVar
from linked_list import ListNode

T = TypeVar('T')


class Stack:
    """ Abstract class for various Stack ADT implementations.
    """

    def __init__(self) -> None:
        self.size = 0
    
    @abstractmethod
    def push(self, element) -> None:
        """ Add element to top of stack.
        """
        pass
    
    @abstractmethod
    def pop(self) -> T:
        """ Remove element from top of stack (in LIFO order).
        """
        pass
    
    @abstractmethod
    def peek(self) -> T:
        """ Read element at top of stack without modifications.
        """
        pass


class ArrayStack(Stack):
    """ A dynamic array-based (Python list) stack implementation.
    """

    def __init__(self) -> None:
        Stack.__init__(self)
        self.array = [None]  # Will be superceded by first pushed element.
    
    def push(self, element) -> None:
        self.array.append(element)
        self.size += 1
    
    def pop(self) -> T:
        return self.array.pop()

    def peek(self) -> T:
        return self.array[-1]


class LinkedListStack(Stack):
    """ A linked list-based stack implementation.
    """

    def __init__(self):
        Stack.__init__(self)
        self.root = None
    
    def push(self, element) -> None:
        # Set root ptr to new node & update next ptr to prev root.
        self.root, self.root.next = ListNode(element), self.root
    
    def pop(self) -> T:
        tmp = self.root
        self.root = self.root.next  # Simply update ref to root & let garbage collection handle previous root.
        return tmp
    
    def peek(self) -> T:
        return self.root


if __name__ == '__main__':
    
    def test_str_reversal(stack: Stack):
        inStr = '!selrahC notniL si eman ym ,olleH'
        for c in inStr:
            stack.push(c)
        
        for _ in inStr:
            print(stack.pop(), end='') # The `end` param ensures same line print.
        print()

    test_str_reversal(LinkedListStack())
