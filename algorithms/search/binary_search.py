# Initialise lo & hi pointers and calculate their mid value. Compare mid value to target and recursively 
# reduce search space accordingly. 

def binary_search(arr, target):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if target > arr[mid]:
            lo = mid + 1
        elif target < arr[mid]:
            hi = mid - 1
        else:
            return mid
    
    return None


if __name__ == '__main__':
    arr = [1, 2, 3, 7, 8, 10, 11, 12]
    print(binary_search(arr, 8))
