# https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num: int) -> int:
        if num >= 0 and num <= 9:
            return num
        else:
            return (num - 1) % 9 + 1