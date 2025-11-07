n = int(input())
def pattern0(n):
    for i in range(n):
        for j in range(n+1):
            print("0", end = " ")
        print()
# pattern0(n)

def pattern1(n):
    for i in range(1,n+1):
        for j in range(i):
            print("0", end = " ")
        print()
# pattern1(n)

def pattern2(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j, end = " ")
        print()
# pattern2(n)

def pattern3(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i, end = " ")
        print()
# pattern3(n)

def pattern4(n):
    for i in range(1,n+1):
        for j in range(65,65+n+1):
            if(i >= j-65+1):
                print(chr(i+64), end = " ")
        print()
# pattern4(n)

# Better approach 
def pattern4(n):
    for i in range(0,n):
        for j in range(i+1):
                print((chr)(65+i), end = " ")
        print()
# pattern4(n)
# A
# B C
# C D E
# D E F G

for i in range(n):
    for j in range(i+1):
        print(chr(65+j+i), end = " ")
    print()

# E
# D E
# C D E
# B C D E
# A B C D E
for i in range(n):
    for j in range(i+1):
        print(chr(n-i+j+64), end = " ")
    print()


#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 
for i in range(n):
    for spaces in range(n-i-1,0,-1):
        print(" ", end = " ")
    for k in range(i+1):
        print(k+1, end = " ")
    print()
    

# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end = " ")
    print()

#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5 
for i in range(n):
    for j in range(1, n - i):
        print(" ", end = " ")
    for j in range(i + 1, 2 * i + 2):
        print(j, end = " ")
    for j in range(2*i , i, -1):
        print(j, end = " ")
    print()
    

#     * 
#   * * * 
# * * * * * 
#   * * * 
#     * 
n = 5
x = n //2 + 1
for i in range(x):
    for j in range(1, x - i):
        print(" ", end = " ")
    for j in range(1, (2*i + 2)):
        print("*", end = " ")
    print()
for i in range(1, (n - x) + 1):
    for j in range(i):
        print(" ", end = " ")
    for j in range(1, n - (2*i) + 1):
        print("*", end = " ")
    print()

