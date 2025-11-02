# * * * * * 
#   * * * * * 
#     * * * * * 
#       * * * * * 
#         * * * * * 

n = 5
for i in range(n):
    for spaces in range(i):
        print(" ", end = " ")
    for stars in range(n):
        print("*", end = " ")
    print()


# n = 5
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

for i in range(n):
    sum = 0
    for j in range(1, i+2):
        print(j, end = " ")
        if j < i + 1:
            print( "+", end = " ")
        sum += j
    print("=", end = " ")
    print(sum)
    

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
for i in range(n):
    for j in range(n-i):
        print("*", end = " ")
    print()
    
        
    