# Given a list, take the current element (1st element on unsorted sublist & after iteration, last element on sorted sublist)
# and exchange it with the smallest element on the right hand side of the current element (in unsorted sublist).
from tester import Tester


def selection_sort(arr: list) -> list:
    i = 0
    while i < len(arr):
        j = i
        min_j = j

        # Select min element from unsorted sublist
        while j < len(arr):
            if arr[j] < arr[min_j]:
                min_j = j
            j += 1

        tmp = arr[min_j]
        arr[min_j] = arr[i]
        arr[i] = tmp
        i += 1
    return arr


if __name__ == '__main__':
    tester = Tester()
    tester.test(selection_sort, "Selection Sort")
