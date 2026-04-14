# Given a string s, remove all the spaces from the string and return the modified string.

# Examples:

# Input: s = "g eeks for ge eks"
# Output: "geeksforgeeks"
# Explanation: All space characters are removed from the given string while preserving the order of the remaining characters, resulting in the final string "geeksforgeeks".
# Input: s = "abc d "
# Output: "abcd"
# Explanation:  All space characters are removed from the given string while preserving the order of the remaining characters, resulting in the final string "abcd".
# Constraints:
# 1 ≤ |s| ≤ 105

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)
#gfg solution
class Solution:
    def removeSpaces(self, s):
        result = ""

        for ch in s:
            if ch != ' ':
                result += ch

        return result