class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=[set() for _ in range(9)]
        c=[set() for _ in range(9)]
        b=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value=board[i][j]
                if value==".":
                    continue 
                box=(i//3)*3+(j//3)
                if value in r[i] or value in c[j] or value in b[box]:
                    return False

                r[i].add(value)
                c[j].add(value)
                b[box].add(value)
        return True