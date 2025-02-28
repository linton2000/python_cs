# Recursively divide the unsorted list into two equally sized sublists until sublists are of size 1.
# Then merge the sublists back together until the entire list is sorted.
from tester import Tester


def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(arr1: list, arr2: list):
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    # Append rest of the elements
    if i < len(arr1):   
        res += arr1[i:]     # Elements left in arr1
    else:
        res += arr2[j:]     # Elements left in arr2
    return res


if __name__ == '__main__':
    tester = Tester()
    tester.test(merge_sort, "Merge Sort")
