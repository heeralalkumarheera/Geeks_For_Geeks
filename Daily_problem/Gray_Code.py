# Given a number n, generate bit patterns from 0 to 2n-1 such that successive patterns differ by one bit. 
# A Gray code sequence must begin with 0.
 
# Examples:
# Input: n = 2
# Output: ["00", "01", "11", "10"]
# Explanation: 
# 00 and 01 differ by one bit.
# 01 and 11 differ by one bit.
# 11 and 10 also differ by one bit.
# Input: n = 3
# Output: ["000", "001", "011", "010", "110", "111", "101", "100"]
# Explanation:
# 000 and 001 differ by one bit.
# 001 and 011 differ by one bit.
# 011 and 010 differ by one bit.
# Similarly, every successive pattern 
# differs by one bit.
# Constraints :
# 1 ≤ n ≤ 16
# Expected Complexities
# Time Complexity: O(2^n)
# Auxiliary Space: O(2^n)


# gfg Solution

class Solution:
    def graycode(self, n):
        # Step 1: base case
        result = ["0", "1"]
        
        # Agar n = 1 hai
        if n == 1:
            return result
        
        # Step 2: 2 se n tak build karo
        for i in range(2, n + 1):
            
            # reverse list banate hain
            rev = result[::-1]
            
            # first half → '0' prefix
            for j in range(len(result)):
                result[j] = "0" + result[j]
            
            # second half → '1' prefix
            for j in range(len(rev)):
                rev[j] = "1" + rev[j]
            
            # dono ko combine karo
            result = result + rev
        
        return result