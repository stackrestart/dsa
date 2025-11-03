n = 5
# 1 3 5 7 9 
# 3 5 7 9 1 
# 5 7 9 1 3 
# 7 9 1 3 5 
# 9 1 3 5 7 

for i in range(n):
    for j in range(2*i + 1, 2 * n, 2):
        print(j, end = " ")
    a = 1
    for k in range(i):
        print(a, end = " ")
        a += 2
    print()

# sum of even and odd numbers
arr = [1, 2, 3, 4, 5, 6]
len_arr = len(arr)
even_sum = odd_sum = 0
for i in range(len_arr):
    if(arr[i] % 2 == 0):
        even_sum += arr[i]
    else:
        odd_sum += arr[i]
print(even_sum, odd_sum)
        
# sum of even and odd indices
arr = [3,1,4,5,6,2]
len_arr = len(arr)
even_sum = odd_sum = 0
for i in range(len_arr):
    if(i % 2 == 0):
        even_sum += arr[i]
    else:
        odd_sum += arr[i]
print(even_sum, odd_sum)

# 4 7 8 9 5  // Sum of Pairs of elements
# 5 6 7 3 
# 9 10 6 
# 11 7 
# 8 
arr = [3,1,4,5,6,2]
len_arr = len(arr)
for i in range(len_arr):
    sum_pairs = 0
    for j in range(i+1, len_arr):
        sum_pairs = arr[i] + arr[j]
        print(sum_pairs, end = " ")
    print()

# Sum of pairs of elements using 2 arrays
# 5 7 8 6 4 9 
# 3 5 6 4 2 7 
# 6 8 9 7 5 10 
# 7 9 10 8 6 11 
# 8 10 11 9 7 12 
# 4 6 7 5 3 8 
arr1 = [3,1,4,5,6,2]
arr2 = [2,4,5,3,1,6]
len_arr1 = len(arr1)
len_arr2 = len(arr2)
for i in range(len_arr1):
    sum_pairs = 0
    for j in range(len_arr2):
        sum_pairs = arr1[i] + arr2[j]
        print(sum_pairs, end = " ")
    print()

# max pair sum of 2 arrays
arr1 = [1,3,2,5,6,4]
arr2 = [2,5,7,1,4,11]
len_arr1 = len(arr1)
len_arr2 = len(arr2)
pair_sum = 0
max_sum = 0
for i in range(len_arr1):
    for j in range(len_arr2):
        pair_sum = arr1[i] + arr2[j]
        max_sum = max(pair_sum, max_sum)
print(max_sum)

# triplet sum
arr = [1, 3, 4, 5, 6, 2]
len_arr = len(arr)
triplet_sum = 0
for i in range(len_arr - 2):
    for j in range(i + 1, len_arr - 1):
        for k in range(i + 2, len_arr):
            triplet_sum = arr[i] + arr[j] + arr[k]
            print(triplet_sum, end = " ")
    print()

#even, odd triplet sum count        
arr = [1, 3, 4, 5, 6, 2]
len_arr = len(arr)
triplet_sum = 0
even_triplet_sum = 0
odd_triplet_sum = 0
for i in range(len_arr - 2):
    for j in range(i + 1, len_arr - 1):
        for k in range(j + 1, len_arr):
            triplet_sum = arr[i] + arr[j] + arr[k]
            if(triplet_sum % 2 == 0):
                even_triplet_sum += 1
            else:
                odd_triplet_sum += 1
print(even_triplet_sum, odd_triplet_sum)

# prime numbers count in a given range
upper = 10
lower = 3
prime_count = 0

for i in range(lower, upper + 1):
    count = 0
    for j in range(2, i + 1):
        if(i % j == 0):
            count += 1
    if(count == 1):
        prime_count += 1
        
    
print(prime_count)

# reverse numbers in a given range and add
upper = 19
lower = 11
rev_sum = 0
for i in range(lower, upper + 1):
    rev = 0
    num = i
    while(num > 0):
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    rev_sum += rev
print(rev_sum)

# first and last index of target element in the array
arr = [1,6,3,4,4,6,7]
firs_index = -1
last_index = -1
target = 6
for i in range(len(arr)):
    if(arr[i] == target):
        first_index = i
        break
for i in range(len(arr)-1, -1, -1):
    if(arr[i] == target):
        last_index = i
        break
print(first_index, last_index)

# count distinct numbers in a set
arr = [1,6,3,4,4,7,7,8,5]
count_distinct = 0
seen = set()
for i in arr:
    if i not in seen:
        seen.add(i)
        count_distinct += 1
print(count_distinct)

# Count of frequency of every element
arr = [1, 2, 4, 3, 2, 1, 7, 7]
n = len(arr)
count = 0
visited = [False for i in range(100)]
for i in range(n):
    if visited[arr[i]] == False:
        count =1
        visited[arr[i]] = True
        for j in range(i+1, n):
            if(arr[i] == arr[j]):
                count += 1
                visited[arr[j]] = True
        print(arr[i], count)


# 2D arrays
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = len(arr)
col = len(arr[0])
for i in range(row):
    for j in range(col):
        print(arr[i][j], end = " ")
    print()

# 2D array left and right diagonal
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = len(arr)
col = len(arr[0])
for i in range(row):
    for j in range(col):
        if i==j:
            print("left diag",arr[i][j], end = " ")
        if i + j == row - 1:
            print("right diag",arr[i][j], end = " ")

# boundary elements matrices 3*3
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = len(arr)
col = len(arr[0])
for i in range(row):
    for j in range(col):
        if i == 0 or j == 0 or i == row - 1 or j == col - 1:
            print(arr[i][j], end = " ")
    print()


# transpose of a matrix
# arr = [[1,2,3],[4,5,6],[7,8,9]]

# row = len(arr)
# col = len(arr[0])

# # Create a new empty matrix
# transpose = [[0 for _ in range(row)] for _ in range(col)]

# for i in range(row):
#     for j in range(col):
#         transpose[j][i] = arr[i][j]

# for i in range(col):
#     for j in range(row):
#         print(transpose[i][j], end=" ")
#     print()

arr = [[1,2,3],[4,5,6],[7,8,9]]

row = len(arr)
col = len(arr[0])

for i in range(row):
    for j in range(i + 1, col):  # notice j starts from i+1
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for i in range(row):
    for j in range(col):
        print(arr[i][j], end=" ")
    print()

