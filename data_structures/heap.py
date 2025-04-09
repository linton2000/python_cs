from abc import abstractmethod
from typing import TypeVar
from enum import Enum, auto

T = TypeVar('T')


class HeapType(Enum):
    """ Specifying the heap type (min or max). This enum allows switching
    the comparison function in the Heap ADT implementations.
    """
    MIN_HEAP = auto()
    MAX_HEAP = auto()


class Heap:
    """ Abstract class for Heap (aka. Priority Queue) ADT implementations.
    """
    def __init__(self, heap_type: HeapType) -> None:
        self.size = 0
        self.heap_type = heap_type
    
    def _compare(self, val1: T, val2: T) -> bool:
        """ Performs comparison in order to generate & maintain heap based on 
        priority order specified by `heap_type`, 
        i.e. less than (<) for min-heaps & greater than (>) for max-heaps.
        """
        if self.heap_type == HeapType.MIN_HEAP:
            return val1 < val2
        if self.heap_type == HeapType.MAX_HEAP:
            return val1 > val2
        else:
            raise f'Error: Invalid heap_type `{self.heap_type}` in Heap instance.'

    @abstractmethod
    def push(self, new_val: T) -> None:
        """ Add a new element to the heap while maintaining the structure
        and order properties of the heap.
        """
        pass

    @abstractmethod
    def pop(self) -> T:
        """ Remove & return the highest priority element (min/max) from the heap.
        Fix any disruptions to the structure & order properties of the heap.
        """
        pass

    @abstractmethod
    def peek(self) -> T:
        """ Return the highest priority element (min/max) without modifying the heap.
        """
        pass

    @abstractmethod
    def heapify(self, in_vals: list[T], heap_type: HeapType) -> None:
        """ Take a list of values and build a heap from it according to specified heap type.
        """
        pass

    @abstractmethod
    def __str__(self):
        """ Return a string representation of the heap instance.
        """
        pass
