# Go through each element in unsorted lst, increasing their associated count while dynamically resizing the array 
# if an element with size larger than the counts array is found. Use the calculated counts to create a new sorted lst.
from tester import Tester


def bucket_sort(arr: list) -> list:
    """ Bucket sort implementation with dynamically resizing counts array.
    """
    res = []
    counts = [0] * (arr[0] + 1)  # Initial guess for max_element

    for e in arr:
        if e > len(counts):
            counts += (e + 1) * [0]  # Ensuring e has an initialized element in arr
        counts[e] += 1

    for i in range(len(counts)):
        for _ in range(counts[i]):
            res.append(i)

    return res


if __name__ == '__main__':
    tester = Tester()
    tester.test(bucket_sort, "Bucket Sort")
