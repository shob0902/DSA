class Solution:
    def calPoints(self, ops: List[str]) -> int:
        a=[]
        for i in range(len(ops)):
            if ops[i]=="+":
                a.append(a[-1]+a[-2])
            elif ops[i]=="D":
                a.append(a[-1]+a[-1])
            elif ops[i]=="C":
                a.pop()
            else:
                a.append(int(ops[i]))
        return sum(a)

            