from abc import abstractmethod
from typing import TypeVar, Optional
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
    def __init__(self, heap_type, in_vals: Optional[list] = None):
        super().__init__(heap_type)
        self.array = [0]
        if in_vals:
            for val in in_vals: 
                self.push(val)

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
        self.size -= 1
        if len(self.array) == 1:
            return  # No elements to pop
        if len(self.array) == 2:
            return self.array.pop()  # Only 1 element to pop
        
        res = self.array[1]  # Save root node
        self.array[1] = self.array.pop()  # Move last node to root

        # Percolate/sink new root down to right place
        i = 1
        while 2*i < len(self.array):  # Left child exists
            # Check if there's a need to sink
            if self._compare(self.array[2*i], self.array[i]) \
            or (2*i+1 < len(self.array) and self._compare(self.array[2*i + 1], self.array[i])):
                
                # Figure out which child to swap with
                swap_i = 2*i
                if (2*i+1 < len(self.array)) and self._compare(self.array[2*i + 1], self.array[2*i]):
                    swap_i = 2*i + 1  # Need to swap with right child instead

                self.array[i], self.array[swap_i] = self.array[swap_i], self.array[i]
                i = swap_i
            else:
                break  # Node in right place
        return res

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
    heap = ArrayHeap(
        heap_type=HeapType.MIN_HEAP, 
        in_vals=[17, 65, 19, 21, 19, 14, 16, 26, 68, 30])
    print(heap)
    res = []
    while heap.size > 0:
        res.append(heap.pop())
    print(res)
