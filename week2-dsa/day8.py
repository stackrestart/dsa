# Program to implement selection Sort
l = [2,5,24,1,4,52,41,38]
n = len(l)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if l[j] < l[min_index]:
            min_index = j
    l[i], l[min_index] = l[min_index], l[i]

print(l)


# Program to implement Bubble Sort
l = [2,5,24,1,4,52,41,38,3,5]
n = len(l)
for i in range(n - 1, 0, -1):
    didSwap = 0
    for j in range(i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            didSwap = 1
    if didSwap == 0:
        break
print(l)

# program to implement Insertion Sort
l = [2,5,24,1,4,52,41,38,3,5,4,21]
n = len(l)
for i in range(n):
    j = i
    while j > 0 and l[j - 1] > l[j]:
        l[j - 1], l[j] = l[j], l[j - 1]
        j -= 1
print(l)
    



# https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true
def pickingNumbers(a):
    a.sort()
    n = len(a)
    current_length = 0
    max_length = 1
    for i in range(n):
        maxi = a[i]
        mini = a[i]
        for j in range(i+1,n):
            maxi = max(maxi, a[j])
            mini = min(mini, a[j])
            if(maxi - mini <= 1):
                current_length = j - i + 1
        max_length = max(max_length, current_length)
        
    return max_length   

# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true
def designerPdfViewer(h, word):
    max_height = 0
    for i in range(len(word)):
        max_height = max(max_height, h[ord(word[i]) - 97])
    return max_height * len(word)
    
# https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true
def utopianTree(n):
    height = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            height += 1
        else:
            height = height * 2
    return height

# https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true
def angryProfessor(k, a):
    count_on_time = 0
    for i in a:
        if i <= 0:
            count_on_time += 1
    if count_on_time >= k:
        return "NO"
    else:
        return "YES"
    
# https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true
def circularArrayRotation(a, k, queries):
    k = k % len(a)
    ans = []
    for i in range(k):
        last = a.pop(-1)
        a.insert(0, last)
    for i in queries:
        ans.append(a[i])
    return ans

# https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
def permutationEquation(p):
    n = len(p)
    lis = [0] * (n + 1)
    ans = []
    for i in range(n):
        lis[p[i]] = i + 1
    for i in range(1, n + 1):
        ans.append(lis[lis[i]])
    return ans

# https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true
def findDigits(n):
    ans = 0
    n_copy = n
    while n_copy > 0:
        digit = n_copy % 10
        if digit !=0 and n % digit == 0:
            ans += 1
        n_copy = n_copy // 10
    return ans

# https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true
def hurdleRace(k, height):
    ans = 0
    for i in height:
        if i > k:
            ans = max(ans, i - k)
    return ans


    