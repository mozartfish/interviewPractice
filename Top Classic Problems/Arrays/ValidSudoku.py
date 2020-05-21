class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = {'row': [{} for x in range(len(board))],
                'col': [{} for x in range(len(board[0]))],
                'sub':[{} for x in range(9)]}
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                entry = board[row][col]
                
                if entry != '.':
                    # invalid row
                    if entry in table['row'][row]: return False
                    table['row'][row][entry] = True
                    # invalid col
                    if entry in table['col'][col]: return False
                    table['col'][col][entry] = True
                    
                    # invalid sub block
                    block = (row//3) * 3 + col//3
                    if entry in table['sub'][block]: return False
                    table['sub'][block][entry] = True
        return True
                    