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
    

