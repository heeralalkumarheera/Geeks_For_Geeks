# Given a number, in the form of an array num[] containing digits from 1 to 9(inclusive). Find the next smallest palindrome strictly larger than the given number.

# Examples:

# Input: num[] = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]
# Output: [9, 4, 1, 8, 8, 0, 8, 8, 1, 4, 9]
# Explanation: Next smallest palindrome is 9 4 1 8 8 0 8 8 1 4 9.
# Input: num[] = [2, 3, 5, 4, 5]
# Output: [2, 3, 6, 3, 2]
# Explanation: Next smallest palindrome is 2 3 6 3 2.
# Constraints:
# 1 ≤ n ≤ 105
# 1 ≤ num[i] ≤ 9

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)

#gfg solution

class Solution:
    def nextPalindrome(self, num):
        n = len(num)

        # 🔥 Case 1: all 9
        if all(x == 9 for x in num):
            return [1] + [0]*(n-1) + [1]

        # Step 1: middle find
        mid = n // 2
        i = mid - 1
        j = mid + 1 if n % 2 else mid

        # Step 2: check if left smaller
        left_smaller = False
        while i >= 0 and num[i] == num[j]:
            i -= 1
            j += 1

        if i < 0 or num[i] < num[j]:
            left_smaller = True

        # Step 3: mirror left → right
        i = mid - 1
        j = mid + 1 if n % 2 else mid

        while i >= 0:
            num[j] = num[i]
            i -= 1
            j += 1

        # Step 4: handle carry if needed
        if left_smaller:
            carry = 1

            if n % 2 == 1:
                num[mid] += carry
                carry = num[mid] // 10
                num[mid] %= 10
                i = mid - 1
                j = mid + 1
            else:
                i = mid - 1
                j = mid

            while i >= 0 and carry:
                num[i] += carry
                carry = num[i] // 10
                num[i] %= 10
                num[j] = num[i]
                i -= 1
                j += 1

        return num