class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result=[]
        for op in operations:
            if op=="+":
                newch=result[-1]+result[-2]
                result.append(newch)
            elif op=="D":
                new=result[-1]*2
                result.append(new)
            elif op=="C":
                result.pop()
            else:
                result.append(int(op))
        return sum(result)
            
        