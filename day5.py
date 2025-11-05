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

