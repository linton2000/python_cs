from abc import abstractmethod
from typing import TypeVar
from linked_list import ListNode

T = TypeVar('T')


class Queue:
    """ Abstract class for various Queue ADT implementations.
    """

    def __init__(self) -> None:
        self.size = 0
    
    @abstractmethod
    def enqueue(self, element) -> None:
        """ Append element to end of queue.
        """
        pass
    
    @abstractmethod
    def dequeue(self) -> T:
        """ Remove element from start of queue (FIFO order).
        """
        pass
    
    @abstractmethod
    def peek(self) -> T:
        """ Read element at front of queue without modifications.
        """
        pass
