# 5192 4466 8X12 5X57

def brute_force_match(matchArr):
    res = []
    n = countX(expandArr(matchArr))
    perms = [['0']*n]
    bound = ['9']*n
    while perms[-1] != bound:
        perms.append(permNext(perms[-1], n))
    for i in perms:
        candidate = spliceArr(i, expandArr(matchArr))
        if (checkLuhn(candidate)):
            res.append(''.join(candidate))
    return len(res), res


def permNext(permArr, n):
    nextPerm = str(int(''.join(map(str, permArr))) + 1)
    if len(nextPerm) < n:
        nextPerm = '0'*(n-len(nextPerm)) + nextPerm
    return list(nextPerm)


def expandArr(compactArr):
    res = ['x']*compactArr[0]
    for i in range(len(compactArr[1])):
        res[compactArr[1][i]] = str(compactArr[2][i])
    return res


def spliceArr(cArr1, cArr2):
    j = 0
    for i in range(len(cArr2)):
        if cArr2[i] == 'x':
            cArr2[i] = cArr1[j]
            j += 1
        if j >= len(cArr1):
            break
    return cArr2


def countX(arr):
    count = 0
    for i in arr:
        if i == 'x':
            count += 1
    return count


def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if (isSecond == True):
            d = d * 2
        # We add two digits to handle cases that make two digits after doubling
        nSum += d // 10
        nSum += d % 10
        isSecond = not isSecond
    if (nSum % 10 == 0):
        return True
    return False


card = (16, [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15],
        [5, 1, 9, 2, 4, 4, 6, 6, 8, 1, 2, 5, 5, 7])
print(brute_force_match(card))
