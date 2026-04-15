# Given a string s, replace all the spaces in the string with '%20'.

# Examples:

# Input: s = "i love programming"
# Output: "i%20love%20programming"
# Explanation: The 2 spaces are replaced by '%20'
# Input: s = "Mr Benedict Cumberbatch"
# Output: "Mr%20Benedict%20Cumberbatch"
# Explanation: The 2 spaces are replaced by '%20'
# Constraints:
# 1 ≤ s.size() ≤ 104

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)

#gfg solution

class Solution:
    def URLify(self, s):
        result = ""

        for ch in s:
            if ch == ' ':
                result += "%20"
            else:
                result += ch

        return result