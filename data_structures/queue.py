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


class LinkedListQueue:
    """ A linked list-based implementation of the Queue ADT.
    """

    def __init__(self) -> None:
        self.size = 0
        self.root = None
    
    def enqueue(self, element) -> None:
        if self.root:
            self.root.next = ListNode(element)
        else:
            self.root = ListNode(element)
        self.size += 1
    
    def dequeue(self) -> T:
        if not self.root:
            self.root = None
        tmp = self.root
        self.root = self.root.next
        self.size -= 1
        return tmp
    
    def peek(self) -> T:
        return self.root


if __name__ == '__main__':

    def test_str_order(queue: Queue):
        inStr = 'Hello, my name is Linton Charles!'
        for c in inStr:
            queue.enqueue(c)
        
        for _ in range(queue.size):
            print(queue.dequeue(), end='')
        print()
    
    test_str_order(LinkedListQueue())
