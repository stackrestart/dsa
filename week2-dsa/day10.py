# https://www.hackerrank.com/challenges/taum-and-bday/problem?isFullScreen=false
def taumBday(b, w, bc, wc, z):
    ans = 0
    if bc + z <= wc:
        ans += w * (bc + z)
    else:
        ans += w * wc
    if wc + z <= bc:
        ans += b * (wc + z)
    else:
        ans += b * bc
    return ans

