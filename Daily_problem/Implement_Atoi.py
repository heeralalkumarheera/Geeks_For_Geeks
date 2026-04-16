# Given a string s, convert it into a 32-bit signed integer (similar to the atoi() function) without using any built-in conversion functions.
# The conversion follows these rules:

# Ignore Leading Whitespaces: Skip all leading whitespace characters.
# Check Sign: If the next character is either '+' or '-', take it as the sign of the number. If no sign is present, assume the number is positive.
# Read Digits: Read the digits and ignore any leading zeros. Stop reading when a non-digit character is encountered or the end of the string is reached. If no digits are found, return 0.
# Handle Overflow: If the number exceeds the range of a 32-bit signed integer:
# Return 2³¹ − 1 (i.e., 2147483647) if it is greater than the maximum value.
# Return −2³¹ (i.e., -2147483648) if it is smaller than the minimum value.
# Return the final integer value.

# Examples:

# Input: s = "-123"
# Output: -123
# Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer
# Input: s = " -"
# Output: 0
# Explanation: No digits are present, therefore the returned answer is 0.
# Input: s = " 1231231231311133"
# Output: 2147483647
# Explanation: The converted number will be greater than 231 – 1, therefore print 231 – 1 = 2147483647.
# Input: s = "-999999999999"
# Output: -2147483648
# Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.
# Input: s = "  -0012gfg4"
# Output: -12
# Explanation: Nothing is read after -12 as a non-digit character ‘g’ was encountered.
# Constraints:
# 1 ≤ |s| ≤ 15

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)

#gfg solution 

class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1️⃣ skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2️⃣ check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3️⃣ read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4️⃣ overflow check
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31

            num = num * 10 + digit
            i += 1

        return sign * num