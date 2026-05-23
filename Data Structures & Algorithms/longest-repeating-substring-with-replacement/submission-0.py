class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        right=0
        ans=0
        maxfreq=0
        for right in range(len(s)):
            ch =s[right]
            if ch  in count:
                count[ch]+=1
            else:
                count[ch]=1
            if count[ch]>maxfreq:
                maxfreq=count[ch]
            window=right-left+1

            while window-maxfreq>k:
                leftch=s[left]
                count[leftch]-=1
                left+=1
                window =right-left+1
            if window >ans:
                ans=window
        return ans 

        