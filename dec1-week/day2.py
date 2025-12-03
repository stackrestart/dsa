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
        
# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {} 

        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [num_dict[diff], i]
            num_dict[num] = i
        return []
    
# https://leetcode.com/problems/reverse-string/description/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]  
            l += 1
            r -= 1
        return s