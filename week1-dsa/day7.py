# https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
def birthday(s, d, m):
    len_s = len(s)
    sum = 0
    count_sq = 0
    for i in range(m):
        sum += s[i]
    if sum == d:
        count_sq += 1
    for j in range(m, len_s):
        sum = sum - s[j - m] + s[j]
        if sum == d:
            count_sq += 1
    return count_sq

# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

# list to dictionary with frequency
arr = [12,3,4,5,6]
freq_dict = {}
for item in arr:
    freq_dict[item] = freq_dict.get(item,0) + 1
print(freq_dict)

# https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true
def migratoryBirds(arr):
    freq_dict = {}
    count = 0
    ans = 0
    for item in arr:
        freq_dict[item] = freq_dict.get(item,0) + 1
    for key,value in freq_dict.items():
        if count < value or (count == value and key < ans):
            count = value
            ans = key
    return ans
            
# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
def bonAppetit(bill, k, b):
    total_bill = sum(bill)
    total_bill -= bill[k]
    bill_per_person = total_bill // 2
    if b == bill_per_person:
        print("Bon Appetit")
    else:
        print(b - bill_per_person)

# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    ans = ''
    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            ans = '12.09.' + str(year)
            return ans
        else:
            ans = '13.09.' + str(year)
            return ans
    else:
        if year % 400 == 0 or (year % 4 ==0 and year % 100 !=0):
            ans = '12.09.' + str(year)
            return ans
        else:
            ans = '13.09.' + str(year)
            return ans
        
# https://www.hackerrank.com/challenges/counting-valleys/problem
def countingValleys(steps, path):
    total_val = 0
    up = 0
    down = 0
    for i in range(steps):
        if path[i] == 'U':
            up += 1
            if up == down:
                total_val += 1
        else:
            down += 1
    return total_val

# https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true
def getMoneySpent(keyboards, drives, b):
    min_b = min(drives)
    min_k = min(keyboards)
    if min_b + min_k > b:
        return -1
    else:
        l = []
        for i in keyboards:
            for j in drives:
                if i + j <= b:
                    l.append(i+j)
    return max(l)
