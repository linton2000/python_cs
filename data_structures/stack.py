from abc import abstractmethod
from typing import TypeVar

T = TypeVar('T')

class Stack:
    """ Abstract class for various stack implementations.
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


if __name__ == '__main__':
    
    # Test string reversal using ArrayStack
    inStr = '!selrahC notniL si eman ym ,olleH'
    stack = ArrayStack()
    for c in inStr:
        stack.push(c)
    
    for _ in inStr:
        print(stack.pop(), end='') # The `end` param ensures same line print.
    print()
    