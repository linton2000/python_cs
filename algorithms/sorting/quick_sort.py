# Recursively pick a pivot (as close to median as possible) and move all smaller elements to its left
# and all larger elements to its right. 
from tester import Tester


def quick_sort(arr: list) -> list:
    # Recursion Base Case
    if len(arr) <= 1:
        return arr

    # Ensures all elements left of pvt are smaller, and all elements to the right are greater than pvt.
    less, equal, greater = partition_naive(arr)
    
    left = quick_sort(less)
    right = quick_sort(greater)
    return left + equal + right

def partition_naive(arr: list) -> list:
    """ 
    1. Iterates through full input arr.
        a. Appends all elements smaller than pvt to `less` array.
        b. Appends all elements larger than pvt to `greater` array.
        c. Appends all elements equal to pvt to `equal` array (to handle duplicates).
    """
    pvt_i = _median_of_three(arr, 0, len(arr) - 1)

    i = 0
    less, greater, equal = [], [], []
    while i < len(arr):
        if arr[i] < arr[pvt_i]:
            less.append(arr[i])
        elif arr[i] > arr[pvt_i]:
            greater.append(arr[i])
        else:
            equal.append(arr[i])
        i += 1
    
    return less, equal, greater

def _median_of_three(arr: list, lo: int, hi: int) -> int:
    """ Sort 1st, mid and last element of arr. Mid element is median of three and 
    will be chosen as pivot.
    """
    mid = (lo + hi) // 2
    if arr[lo] > arr[hi]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    if arr[mid] > arr[hi]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
    if arr[lo] > arr[mid]:
        arr[lo], arr[mid] = arr[mid], arr[lo]
    return mid

if __name__ == '__main__':
    tester = Tester()
    tester.test(quick_sort, "Quick Sort")
