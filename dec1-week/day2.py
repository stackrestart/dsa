# https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num: int) -> int:
        if num >= 0 and num <= 9:
            return num
        else:
            return (num - 1) % 9 + 1
        
# https://leetcode.com/problems/minimum-number-game/description/
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr =[]
        nums.sort()
        for i in range(0,len(nums),2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums

# https://leetcode.com/problems/fizz-buzz/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                arr.append("FizzBuzz")
            elif i % 3 == 0:
                arr.append("Fizz")
            elif i % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i))
        return arr
        