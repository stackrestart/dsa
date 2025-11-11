# https://www.hackerrank.com/challenges/taum-and-bday/problem?isFullScreen=false
def taumBday(b, w, bc, wc, z):
    ans = 0
    if bc + z <= wc:
        ans += w * (bc + z)
    else:
        ans += w * wc
    if wc + z <= bc:
        ans += b * (wc + z)
    else:
        ans += b * bc
    return ans

# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
def kaprekarNumbers(p, q):
    ans = []
    for i in range(p, q + 1):
        d = len(str(i))
        sq = str(i ** 2)
        if i == 1:
            ans.append(i)
        elif (len(sq)) > d and i == int(sq[-d:]) + int(sq[:-d]) and int(sq[d:]) != 0:
            ans.append(i)
    if len(ans) == 0:
        print("INVALID RANGE")
    else:
        print(*ans, end = "")

# https://www.hackerrank.com/challenges/chocolate-feast/problem?h_r=profile
def chocolateFeast(n, c, m):
    # Write your code here
    initial = n // c
    wrappers = initial
    count_c = initial
    while(wrappers >= m):
        wrappers = wrappers - m
        wrappers += 1
        count_c += 1
    return count_c
    
# https://www.hackerrank.com/challenges/insertionsort1/problem?h_r=profile
def insertionSort1(n, arr):
    sort_element = arr[-1]
    for i in range(len(arr)-1, -1, -1):
        if i != 0 and arr[i - 1] > sort_element:
            arr[i] = arr[i - 1]
            print(*arr)
        if arr[i - 1] < sort_element:
            arr[i] = sort_element
            print(*arr)
            break
        if i == 0:
            arr[i] = sort_element
            print(*arr)
            break

# https://www.hackerrank.com/challenges/strange-code/problem?h_r=profile
def strangeCounter(t):
    rem = 3
    while t > rem:
        t -= rem
        rem = rem*2
    return rem - t + 1