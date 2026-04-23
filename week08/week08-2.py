#week 08-2.py leetcode 374
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n+1
        while left < right:
            mid = (left + right) // 2
            if guess(mid)==0: return mid
            if guess(mid)>0: left = mid + 1
            else: right = mid
        return left

#另外一種寫法
        #for i in range(n+1): print( -guess(i), end=' ')
        return bisect_left( range(n+1), 0, key=lambda x:-guess(x) )
