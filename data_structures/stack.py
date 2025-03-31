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
        Stack.__init__()
        self.array = [None]  # Will be superceded by first pushed element.
    
    def push(self, element) -> None:
        self.array[self.size] = element
        self.size += 1
    
    def pop(self) -> T:
        return self.array.pop()

    def peek(self) -> T:
        return self.array[-1]
    