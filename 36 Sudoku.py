import numpy as np
class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSet(l):
            s = set()
            for i in l:
                if i=='.':
                    continue
                elif int(i) in range(1, 10) and int(i) not in s:
                    s.add(int(i))
                else:
                    return False
            return True


        board = np.array(board)
        for l in board:
            if checkSet(l) == False:
                return False
        for l in zip(*board):
            if checkSet(list(l)) == False:
                return False
        if checkSet(np.ndarray.flatten(board[:3,:3])) == False:
            return False
        if checkSet(np.ndarray.flatten(board[3:6,:3])) == False:
            return False
        if checkSet(np.ndarray.flatten(board[6:9,:3])) == False:
            return False
        if checkSet(np.ndarray.flatten(board[:3,3:6])) == False:
            return False
        if checkSet(np.ndarray.flatten(board[3:6,3:6])) == False:
            return False
        if checkSet(np.ndarray.flatten(board[6:9,3:6])) == False:
            return False
        if checkSet(np.ndarray.flatten(board[:3,6:9])) == False:
            return False
        if checkSet(np.ndarray.flatten(board[3:6,6:9])) == False:
            return False
        if checkSet(np.ndarray.flatten(board[6:9,6:9])) == False:
            return False
        return True
                