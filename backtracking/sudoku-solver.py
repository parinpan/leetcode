# Leetcode: https://leetcode.com/problems/sudoku-solver/
# Level: Hard


class Solution:
    def __init__(self):
        self.colSets = [set() for _ in range(9)]
        self.rowSets = [set() for _ in range(9)]
        self.subSets = [set() for _ in range(9)]
        
        self.empties = []
        self.validEntries = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        
    def getSubBoardIndex(self, i, j):
        return 3 * (i // 3) + (j // 3)
    
    def saveState(self, i, j, num):
        self.colSets[j].add(num)
        self.rowSets[i].add(num)
        self.subSets[self.getSubBoardIndex(i, j)].add(num)
        
    def removeState(self, i, j, num):
        self.colSets[j].remove(num)
        self.rowSets[i].remove(num)
        self.subSets[self.getSubBoardIndex(i, j)].remove(num)
        
    def saveFirstBoard(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    self.saveState(i, j, board[i][j])
                else:
                    self.empties.append((i, j))

    def isSolved(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if len(self.colSets[j]) < 9 or \
                    len(self.rowSets[i]) < 9 or \
                        len(self.subSets[self.getSubBoardIndex(i, j)]) < 9:
                    return False

        return True
                    
    def crackSudoku(self, board, index=0):
        if index >= len(self.empties):
            return self.isSolved(board)

        i, j = self.empties[index]

        for entry in self.validEntries:
            if entry in self.colSets[j] or \
                    entry in self.rowSets[i] or \
                        entry in self.subSets[self.getSubBoardIndex(i, j)]:
                continue

            board[i][j] = entry
            self.saveState(i, j, entry)

            if self.crackSudoku(board, index + 1):
                return True

            board[i][j] = '.'
            self.removeState(i, j, entry)
            
        return False
    
    def solveSudoku(self, board) -> None:
        self.saveFirstBoard(board)
        self.crackSudoku(board)


if __name__ == '__main__':
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    assert s.solveSudoku(board) == None
    assert board == [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
