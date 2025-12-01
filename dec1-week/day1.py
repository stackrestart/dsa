# https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
def missingNumbers(arr, brr):
    # Write your code here
    for i in arr:
        if i in brr:
            brr.remove(i)
    return sorted(list(set(brr)))

# https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true
def closestNumbers(arr):
    # Write your code here
    arr_srt = sorted(arr)
 
    res = []
    pairs = {}
 
    for i in range(0, len(arr_srt) - 1):
        pairs[i] = abs(arr_srt[i] - arr_srt[i+1])
 
    min_diff = min(pairs.values())
 
    for k, v in pairs.items():
        if v == min_diff:
            res.append(arr_srt[k])
            res.append(arr_srt[k + 1])
 
    return res