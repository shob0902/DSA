class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r=[]
        for n in range(numRows):
            row=[1]
            val=1
            for k in range(1,n+1):
                val=val*(n-k+1)//k
                row.append(val)
            r.append(row)
        return r