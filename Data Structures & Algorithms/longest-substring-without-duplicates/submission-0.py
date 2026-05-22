class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set()
        left=0
        right=0
        maxlength=0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            maxlength=max(maxlength , right-left+1)
        return maxlength