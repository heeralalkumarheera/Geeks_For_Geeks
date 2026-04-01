# Given a positive integer n, count all possible distinct binary strings of length n such that there are no consecutive 1’s.

# Examples :

# Input: n = 3
# Output: 5
# Explanation: 5 strings are ("000", "001", "010", "100", "101").
# Input: n = 2
# Output: 3
# Explanation: 3 strings are ("00", "01", "10").
# Input: n = 1
# Output: 2
# Constraints:
# 1 ≤ n ≤ 44

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(n)

# function banaya
def countStrings(n):
    # Base cases
    if n == 1:
        return 2
    if n == 2:
        return 3

    # dp list banayi
    dp = [0] * (n + 1)

    dp[1] = 2  # length 1
    dp[2] = 3  # length 2

    # loop 3 se n tak
    for i in range(3, n + 1):
        # formula apply
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]  # final answer


# 👇 ye part add karo run ke liye
if __name__ == "__main__":
    n = int(input("Enter n: "))  # input lena
    print(countStrings(n))       # function call