# From 4.1 in Introduction to Algorithms - CLRS
def max_crossing_subarray(A, lo, hi, mid):
    left_sum = float('-inf')
    sum = 0
    max_left = mid
    for i in range(mid, lo-1, -1):
        sum = A[i] + sum
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    max_right = mid + 1
    for i in range(mid + 1, hi + 1):
        sum = A[i] + sum
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return max_left, max_right, (left_sum + right_sum)

def max_subarray(A, lo, hi):
    if lo == hi:
        return lo, hi, A[lo]
    else:
        mid = (lo + hi) // 2
        left_lo, left_hi, left_sum = max_subarray(A, lo, mid)
        right_lo, right_hi, right_sum = max_subarray(A, mid + 1, hi)
        cross_lo, cross_hi, cross_sum = max_crossing_subarray(A, lo, hi, mid)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_lo, left_hi, left_sum
        elif right_sum >= right_sum and right_sum >= cross_sum:
            return right_lo, right_hi, right_sum
        else:
            return cross_lo, cross_hi, cross_sum

def test():
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_subarray(A, 0, len(A) - 1))

