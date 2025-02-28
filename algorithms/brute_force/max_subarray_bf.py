# Ex 4.1-3 Maximum subarray brute force
def max_subarray_bf(A):
    res_lo = 0
    res_hi = len(A) - 1
    max_sum = float('-inf')
    for i in range(len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum = sum + A[j]
            if sum > max_sum:
                max_sum = sum
                res_lo = i
                res_hi = j
    return res_lo, res_hi, max_sum

def test():
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_subarray_bf(A))