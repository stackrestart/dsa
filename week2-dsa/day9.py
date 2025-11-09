# https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true solve again
def cutTheSticks(arr):
    ans = []
    arr.sort()
    prev = len(arr)
    i = 0
    while i < len(arr):
        r = i + 1
        while r < len(arr) and arr[i] == arr[r]:
            r += 1
        tt = r - i
        i = r
        ans.append(prev)
        prev = prev - tt
    return ans   

# https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
def acmTeam(topic):
    max_topics = 0
    max_teams = 0
    n = len(topic)
    for i in range(n):
        for j in range(i+1, n):
            count_1 = 0
            for k in range(len(topic[i])):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    count_1 += 1
            if count_1 > max_topics:
                max_topics = count_1
                max_teams = 1
            elif count_1 == max_topics:
                max_teams += 1
    return [max_topics, max_teams]

# https://www.hackerrank.com/challenges/find-the-median/problem?h_r=profile
def findMedian(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    med_index = n //2
    return arr[med_index]

