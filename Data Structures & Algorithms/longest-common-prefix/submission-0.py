class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        for i in range(1,len(strs)):
            while strs[i].startswith(first)==False:
                first=first[:-1]

                if first=="":
                    return ""
        return first



        