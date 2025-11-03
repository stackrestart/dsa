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
