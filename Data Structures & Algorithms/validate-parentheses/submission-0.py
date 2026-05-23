class Solution:
    def isValid(self, s: str) -> bool:
        result=[]
        for ch in s:
            if ch=="("or ch=="[" or ch=="{":
                result.append(ch)
            elif ch==")":
                if len(result)==0 or result[-1]!="(":
                    return False
                else:
                    result.pop()
            elif ch=="]":
                if len(result)==0 or result[-1]!="[":
                    return False
                else:
                    result.pop()
            elif ch=="}":
                if len(result)==0 or result[-1]!="{":
                    return False
                else:
                    result.pop()
        return len(result)==0

        