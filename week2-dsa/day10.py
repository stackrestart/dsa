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
    
