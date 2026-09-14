class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def tracker(row, col, i, used):
            # if our row and col are not valid positions on the board we can return false 
            if i == len(word):
                return True
            if not(0 <= row < len(board) and 0 <= col < len(board[0])):
                return False
            if board[row][col] != word[i]: # if the letter we are currently on is not the one at the index also return false this aint the path 
                return False
            if (row, col) in used:
                return False # we have already covered this path!!! 
            
            used.append((row, col))

            if tracker(row + 1, col, i + 1, used) or tracker(row, col + 1, i + 1, used) or tracker(row - 1, col, i + 1, used) or tracker(row, col - 1, i + 1, used):
                return True

            # recursion 
            used.pop()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if tracker(i, j, 0, []):
                    return True
        return False