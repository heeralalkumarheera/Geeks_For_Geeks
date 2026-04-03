# Give a n * n square matrix mat[][], return all the elements of its anti-diagonals from top to bottom.

# Examples :

# Input: n = 2, mat[][] = [[1, 2],
#                         [3, 4]]
# Output: [1, 2, 3, 4]

#gfg Solution

class Solution:
    def diagView(self, mat):
        n = len(mat)
        result = []
        
        for d in range(2*n - 1):
            row = max(0, d - (n - 1))
            col = d - row
            
            while row < n and col >= 0:
                result.append(mat[row][col])
                row += 1
                col -= 1
        
        return result