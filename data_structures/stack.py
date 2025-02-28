from abc import abstractmethod
from typing import TypeVar

T = TypeVar('T')

class Stack:

    def __init__(self) -> None:
        self.size = 0
    
    @abstractmethod
    def push(self, element) -> None:
        pass
    
    @abstractmethod
    def pop(self) -> T:
        pass
    
    @abstractmethod
    def peek(self) -> T:
        pass

    @abstractmethod
    def is_full() -> bool:
        pass

    @abstractmethod
    def is_empty() -> bool:
        pass

class ArrayStack(Stack):
    def __init__(self) -> None:
        Stack.__init__()
        self.array = [None]
    
    def push(self, element):
        self.array[self.size] = element
        self.size += 1
    
    def pop(self):
        pass

# Implement later