class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def tracker(row, col, used, i):
            '''
            fail cases:
            1) our index on the board is not correct so row/col is negative or a higher num
            then the len
            2) if the letter we are on in word is not equal to the letter we are on in the board
            3) if we have already used this row,col
            '''
            '''
            true cases: if the we get to the len of word on our i of word we got the word in the board and return treu
            '''
            if i == len(word):
                return True
            if (row < 0 or row >= len(board)) or (col < 0 or col >= len(board[0])):
                return False
            if word[i] != board[row][col]:
                return False
            if (row, col) in used:
                return False
            # 1004 am

            # if all the above is false then lets search this row,col pair add it to used
            used.append((row, col))
            
            # and then check up down left right to see if we found it 
            found = tracker(row + 1, col, used, i + 1) or tracker(row, col + 1, used, i + 1) or tracker(row - 1, col, used, i + 1) or tracker(row, col - 1, used, i + 1)

            used.pop()     

            return found
        for i in range(len(board)):
            for j in range(len(board[0])):
                if tracker(i, j, [], 0):
                    return True
        return False
                    