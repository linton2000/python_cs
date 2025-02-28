# Given a list, take the current element (1st element of unsorted sublist & after iteration, last element of sorted sublist) 
# and insert it at the appropriate position of the list (sorted sublist), adjusting the list every time you insert.
from tester import Tester


def insertion_sort(arr: list):
    i = 0
    while i < len(arr) - 1:
        j = i

        # Insert in correct position in sorted sublist
        while j >= 0 and arr[j+1] < arr[j]:
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp
            j -= 1
        i += 1
    return arr


if __name__ == '__main__':
    tester = Tester()
    tester.test(insertion_sort, "Insertion Sort")
    