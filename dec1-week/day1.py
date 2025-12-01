# https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
def missingNumbers(arr, brr):
    # Write your code here
    for i in arr:
        if i in brr:
            brr.remove(i)
    return sorted(list(set(brr)))