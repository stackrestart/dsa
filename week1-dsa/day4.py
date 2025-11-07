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

# https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            positive_count += 1
        elif arr[i] == 0:
            zero_count += 1
        else:
            negative_count += 1
    print("{:.6f}".format(positive_count / n))
    print("{:.6f}".format(negative_count / n))
    print("{:.6f}".format(zero_count / n))

# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
def staircase(n):
    for i in range(n):
        print((n-i-1)*" " + (i+1)*'#' )

# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
def miniMaxSum(arr):
    n = len(arr)
    l = []
    for i in range(n):
        sum = 0
        for j in range(n):
            if i != j:
                sum += arr[j]
        l.append(sum)
    l.sort()
    print(l[0],l[-1])
 # alternate approach
def miniMaxSum(arr):
    n = len(arr)
    total = 0
    min_ele = 10**9
    max_ele = 1
    for i in range(n):
        total += arr[i]
        min_ele = min(min_ele, arr[i])
        max_ele = max(max_ele,arr[i])
    print(total - max_ele, total - min_ele)

# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
def birthdayCakeCandles(candles):
    max_height = 0
    candles_c = 0
    for i in candles:
        max_height = max(max_height, i)
    for i in candles:
        if i == max_height:
            candles_c += 1
    return candles_c

# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
def timeConversion(s):
    if s[-2] == 'P':
        if s[:2] == '12':
            return '12' + s[2:len(s)-2]  
        num = str(12 + int(s[0:2]))
    else:
        if s[:2] == '12':
            return '00' + s[2:len(s)-2]  
        return s[:len(s)-2]
    return num + s[2:len(s)-2]

# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
def gradingStudents(grades):
    n = len(grades)
    output = []
    for i in range(n):
        if(grades[i] < 38):
            continue
        elif 5-grades[i]%5 >= 3:
            continue
        else:
            grades[i] += 5-grades[i]%5
    return grades

