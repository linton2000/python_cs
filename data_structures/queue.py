from abc import abstractmethod
from typing import TypeVar
from .node import ListNode

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


class LinkedListQueue(Queue):
    """ A linked list-based implementation of the Queue ADT.
    """
    def __init__(self) -> None:
        Queue.__init__(self)
        self.head = None  # front of queue
        self.tail = None  # back of queue

    def enqueue(self, element) -> None:
        new_node = ListNode(element)
        
        if self.tail:
            self.tail.next = new_node  # Add to the end
            self.tail = new_node
        else:
            # Queue is empty
            self.head = new_node
            self.tail = new_node
            
        self.size += 1

    def dequeue(self) -> T:
        if not self.head:
            return None
            
        tmp = self.head
        self.head = self.head.next
        
        # If we removed the last element, update tail
        if not self.head:
            self.tail = None
            
        self.size -= 1
        return tmp.val  # Return data, not the node

    def peek(self) -> T:
        if not self.head:
            return None
        return self.head.val  # Return data, not the node


if __name__ == '__main__':
    def test_str_order(queue: Queue):
        inStr = 'Hello, my name is Linton Charles!'
        for c in inStr:
            queue.enqueue(c)
        for _ in range(queue.size):
            print(queue.dequeue(), end='')
        print()
        
    test_str_order(LinkedListQueue())
