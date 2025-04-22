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


class ArrayHeap(Heap):
    """ An array-based implementation of the Heap ADT.
    """
    def __init__(self, heap_type):
        super().__init__(heap_type)
        self.array = [0]

    def push(self, new_val: T) -> None:
        self.array.append(new_val)
        self.size += 1

        if len(self.array) == 2:  # Only 1 element in heap
            return

        # Percolate new value up
        i = len(self.array) - 1
        while self._compare(self.array[i], self.array[i//2]):
            self.array[i//2], self.array[i] = self.array[i], self.array[i//2]  # Swap parent & child
            i = i//2  # Move up heap
    
    def pop(self) -> T:
        pass

    def peek(self) -> T:
        return self.array[1]

    def __str__(self):
        res = ''
        def _pretty_str(node_i: int, prefix: str = "", is_left: bool = True) -> str:
            nonlocal res

            if (2*node_i + 1) < len(self.array):  # If right child exists
                _pretty_str(2*node_i + 1, prefix + ("│   " if is_left else "    "), False)

            res += prefix + ("└── " if is_left else "┌── ") + str(self.array[node_i]) + '\n'

            if (2*node_i) < len(self.array):  # If left child exists
                _pretty_str(2*node_i, prefix + ("    " if is_left else "│   "), True)
        
        _pretty_str(1)  # Root node index
        return res


if __name__ == '__main__':
    heap = ArrayHeap(HeapType.MIN_HEAP)
    for i in range(21, 0, -2):
        heap.push(i)
    print(heap)
