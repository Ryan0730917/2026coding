#week03-3.py leetcode 1456
#母音 Vowels: a,e,ii.o.u
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') #把五個字母變成set
        count = 0
        for i in range(k):
            if s[i] in vowels: count += 1
        #離開迴圈時,確認前k個字母,有count 個母音,先當答案
        ans = count
        N = len(s)
        for i in range(k, N):
            if s[i] in vowels: count += 1
            if s[i-k] in vowels: count -= 1
            ans = max(ans, count)
        return ans
