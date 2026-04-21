# Given an array arr[] consisting of 0’s and 1’s. A flip operation involves changing all 0's to 1's and all 1's to 0's within a contiguous subarray. Formally, select a range (l, r) in the array arr[], such that (0 ≤ l ≤ r < n) holds and flip the elements in this range.

# Return the maximum number of 1's you can get in the array after doing at most 1 flip operation.

# Examples :

# Input: arr[] = [1, 0, 0, 1, 0]
# Output: 4
# Explanation: By flipping the subarray from index 1 to 2, the array becomes [1, 1, 1, 1, 0]. This results in a total of 4 ones, which is the maximum possible after at most one flip.
# Input: arr[] = [1, 0, 0, 1, 0, 0, 1]
# Output: 6
# Explanation: By flipping the subarray from index 1 to 5, the array becomes [1, 1, 1, 0, 1, 1, 1]. This results in a total of 6 ones, which is the maximum possible after at most one flip.
# Constraints:
# 1 ≤ n ≤ 106
# 0 ≤ arr[i] ≤ 1

# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)

#gfg solution

class Solution:
    def maxOnes(self, arr):
        total_ones = sum(arr)

        max_gain = 0
        curr_gain = 0

        for num in arr:
            # convert
            val = 1 if num == 0 else -1

            # Kadane
            curr_gain = max(val, curr_gain + val)
            max_gain = max(max_gain, curr_gain)

        return total_ones + max_gain