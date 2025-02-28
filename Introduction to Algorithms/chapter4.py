# Ex 4.1-1
"""
A single element array containing the least negative number.
"""

# Ex 4.1-2 Brute Force solution maximum subarray
"""
BRUTE_FORCE_SOL(A, lo, hi)
    max_sum = -inf
    res_lo = lo
    res_hi = hi
    for i = lo to hi
        for j = i + 1 to hi
            candidate_sum = sum(A[i...j])
            if candidate_sum > max_sum
                max_sum = candidate_sum
                res_lo = i
                res_hi = j
    return res_lo, res_hi, max_sum
"""

# Ex 4.1-4
"""
I would just add a conditional statement that returns an
empty subarray when the final result sum is negative.
"""

# Ex 4.1-5
"""
ITERATIVE-FIND-MAXIMUM-SUBARRAY(A)
    n = A.length
    max-sum = -∞
    sum = -∞
    for j = 1 to n
        currentHigh = j
        if sum > 0
            sum = sum + A[j]
        else
            currentLow = j
            sum = A[j]
        if sum > max-sum
            max-sum = sum
            low = currentLow
            high = currentHigh
    return (low, high, max-sum)

Note: I have no idea how this was done :((
"""

# I will revisit 4.3 onwards later as it's just recurrence relations
