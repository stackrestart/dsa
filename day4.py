# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
def diagonalDifference(arr): # O(n2)
    row = len(arr)
    col = len(arr[0])
    left_diag_sum = 0
    right_diag_sum = 0
    abs_diff = 0
    for i in range(row):
        for j in range(col):
            if i == j:
                left_diag_sum += arr[i][j]
            if i + j == row - 1:
                right_diag_sum += arr[i][j]
    
    abs_diff = abs(left_diag_sum - right_diag_sum)
    return abs_diff

 # Optimized code O(n)
def diagonalDifference(arr):
    n = len(arr)
    col = n - 1
    left_diag_sum = 0
    right_diag_sum = 0
    for i in range(n):
        left_diag_sum += arr[i][i]
        right_diag_sum += arr[i][col]
        col -= 1
    return abs(left_diag_sum - right_diag_sum)


# https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true
def aVeryBigSum(ar):
    arr_sum = 0
    for i in ar:
        arr_sum += i
    return arr_sum

# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true    
def compareTriplets(a, b):
    # Write your code here
    alice_score = 0
    bob_score = 0
    n = len(a)
    for i in range(n):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            alice_score += 1
        else:
            bob_score += 1
    ans = [alice_score, bob_score]
    return ans


    