# Recursively pick a pivot (as close to median as possible) and move all smaller elements to its left
# and all larger elements to its right. 

def quicksort(arr: list, lo: int = None, hi: int = None) -> list:
    if not lo and not hi:
        lo = 0
        hi = len(arr) - 1

    while lo < hi:
        pivot = _median_of_three(arr, lo, hi)
        

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
