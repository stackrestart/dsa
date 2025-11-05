# Hashing 101

#lets say if we number and its frequency in the array, code without hashing is

# n = [1,2,3,4,4,2,1,1,1]
# target = int(input())
# count = 0
# for i in n:
#         if i == target:
#                 count += 1
# print(count) # time complexity O(n) if multiple elements in a range time complexity O(m*n)

# n = int(input())
# # hash = []
# # for i in range(51):
# #         hash[i] = 0
# hash = [0] * 51

# q = int(input())
# array = []
# for i in range(n):
#         array.append(int(input()))
#         hash[array[i]] += 1

# for i in range(q):
#         query = int(input())
#         count = hash[query]
#         print( "query", query, "count" , count )


# hashmap implementation in python

from collections import defaultdict
hashmap = defaultdict(int)
n = int(input())
for i in range(n):
        num = int(input())
        hashmap[num] += 1
q = int(input())
for i in range(q+1):
        query1 = int(input())
        count = hashmap[query1]
        print(query1, count)


# https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_a = 0
    count_o = 0
    dist_a = 0
    dist_o = 0
    for i in apples:
        dist_a = i + a
        if dist_a >= s and dist_a <= t:
            count_a += 1
    for j in oranges:
        dist_o = j + b
        if dist_o >= s and dist_o <= t:
            count_o += 1
    print(count_a)
    print(count_o)
    
# https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"
    else:
        num = x2 - x1
        vel = v2 - v1
        if num % vel == 0:
            return "YES"
        else:
            return "NO"

# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
def getTotalX(a, b):
    max_a = max(a)
    max_b = max(b)
    count_possible = 0
    for i in range(max_a, max_b + 1):
        good_i = True
        for j in a:
            if i % j != 0:
                good_i = False
        for k in b:
            if k % i != 0:
                good_i = False
        if good_i == True:
            count_possible += 1
    return count_possible

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
def breakingRecords(scores):
    min_s = scores[0]
    max_s = scores[0]
    min_count = 0
    max_count = 0
    for i in scores:
        if i < min_s:
            min_s = min(min_s, i)
            min_count += 1
        if i > max_s:
            max_s = max(max_s, i)
            max_count += 1   
    return [max_count, min_count]
    
