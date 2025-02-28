# 2.2-2 Non-increasing Insertion Sort
def non_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr

# 2.2-3 Linear Search
"""
for i = 0 to A.length
    if A[i] == v
        return i
return NIL

Invariant: A[0...i-1] does not contain v 

Initialization: At the start of the loop, i = 0 therefore A[0...-1] does
not contain v trivially

Maintenance: At each iteration, if A[i] == v then loop terminates.
Otherwise, i = i + 1 and A[0...i-1] will not contain v.

Termination: Loop exits either when A[i] == v or when i == A.length == n + 1
where A[n] is the last element. This means that A[0...n] does not contain 
v and hence NIL is returned.

Therefore the algorithm is correct
"""

# 2.2-4 Binary integer sum
"""
Input: Arrays A = [a1, a2, ... , an] and B = [b1, b2, ..., bn]
where all values of a and b are from the set [0, 1]

Output:n Array C = [c1, c2, ..., cn, cn+1] where C is the sum
of A and B

Will revisit later
"""

# 2.3-2 Merge Procedure Rewritten
"""
MERGE(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    Let L and R be new arrays L[p...q] and R[q+1...r]
    for i = 1 to n1
        L[i] = A[p + i - 1]
    for i = 1 to n2
        R[i] = A[q + i]
    i, j = 1, 1
    for k = p to r
        if i > n1
            A[k] = R[j]
            j += 1
        elseif j > n2
            A[k] = L[i]
            i += 1
        elseif L[i] <= R[j]
            A[k] = L[i]
            i += 1
        else
            A[k] = R[j]
            j += 1
"""

# 2.3-4 Insertion Sort Recurrence
"""
T(n) = a, n = 1
T(n) = T(n-1) + O(n), n > 1
"""

# 2.3-5 Binary Search Pseudocode
"""
BINARY_SEARCH_ITERATIVE(A[a1, a2, ..., an], target)
    lo = 1
    hi = A.length
    mid = (lo + hi) // 2

    While lo < hi
        if target > A[mid]
            lo = lo + mid
        elseif target < A[mid]
            hi = hi - mid
        else
            return mid
    return NIL

BINARY_SEARCH_RECURSIVE(A[a1, a2, ..., an], target)
    lo = 1
    hi = A.length
    mid = (lo + hi) // 2

    if low > hi
        return NIL
    elseif A[mid] == target
        return mid
    elseif target > A[mid]
        return BINARY_SEARCH_RECURSIVE(A[mid + 1...hi], target)
    else
        return BINARY_SEARCH_RECURSIVE(A[lo...mid - 1], target)

During each iteration the input length being considered
is halved. Hence the complexity is O(lgn)
"""

# 2.3-7 Sum Finding Algorithm
"""
First, the set should be sorted using Mergesort taking O(nlogn) time.
Next, the program should iterate through each element, find the element's
difference with the target sum and then perform binary search to whether
this value exists in the set. This should take O(n) time to iterate and
during each iteraion, O(lgn) time to find the value. Hence, this algorithm
computes the solution in O(nlgn) time.
"""

# 2-1 Insertion sort on small arrays in merge sort
"""
a) Insertion sort has a worst case time complexity of O(n^2). Each sublist
is of k length and therefore takes O(k^2) time for sorting. There are n/k
sublists which means that the overall time complexity = k^2 * n/k = O(nk)

b) The recursion depth of merge sort is determined by the number of sublists
to be merged. There are n/k sublists so therefore there are lg(n/k) iterations/
levels of recursion. Each iteration performs a MERGE procedure which takes O(n)
time. Therefore the time complexity of this coarsened merge sort is nlg(n/k)

c) k = lg(n)

d) Choose k to be the largest length of a sublist for which insertion
sort is faster than merge sort.
"""

# 2-2 Correctness of bubblesort
"""
a) That A' contains all elements in A but in sorted order.

b) INV: 
"""