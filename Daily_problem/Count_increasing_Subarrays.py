# Given an array arr[] of integers, count the number of subarrays in arr[] which are strictly increasing with size greater or equal to 2. A subarray is a contiguous part of array. A subarray is strictly increasing if each element is greater then it's previous element if it exists.

# Examples:

# Input: arr[] = [1, 4, 5, 3, 7, 9]
# Output: 6
# Explanation: The strictly increasing subarrays are: [1, 4], [1, 4, 5], [4, 5], [3, 7], [3, 7, 9], [7, 9]
# Input: arr[] = [1, 3, 3, 2, 3, 5]
# Output: 4
# Explanation: Increasing Subarrays of size greater or equal to 2 are : {1, 3}, {2, 3}, {2, 3, 5}, {3, 5}. So answer for this test case is 4.
# Input: arr[] = [2, 2, 2, 2]
# Output: 0
# Explanation: No strictly increasing subarray exists.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 107

# Expected Complexities
# gfg solution 
class Solution:
    def countIncreasing(self, arr):
        n = len(arr)
        length = 1   # current increasing segment length
        ans = 0

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                # increasing hai → length badhao
                length += 1
            else:
                # 🔥 sequence break ho gaya
                # previous segment ka count add karo
                ans += (length * (length - 1)) // 2

                # reset for new segment
                length = 1

        # 🔥 last segment ka calculation
        ans += (length * (length - 1)) // 2

        return ans