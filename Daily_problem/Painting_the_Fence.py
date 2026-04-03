# Given a fence with n posts and k colours, find out the number of ways of painting the fence so that not more than two consecutive posts have the same colours.
# Answers are guaranteed to be fit into a 32 bit integer.

# Examples:

# Input: n = 3, k = 2 
# Output: 6
# Explanation: Let the 2 colours be 'R' and 'B'. We have following possible combinations:
# 1. RRB
# 2. RBR
# 3. RBB
# 4. BRR
# 5. BRB
# 6. BBR
# Input: n = 2, k = 4 
# Output: 16
# Explanation: After coloring first post with 4 possible combinations, you can still color next posts with all 4 colors. Total possible combinations will be 4x4=16
# Constraints:
# 1 ≤ n ≤ 300
# 1 ≤ k ≤ 105

def count_ways(n, k):
    # Agar sirf 1 post hai
    if n == 1:
        return k

    # Base case for 2 posts
    same = k * 1        # last 2 same
    diff = k * (k - 1)  # last 2 different

    # Loop from 3rd post
    for i in range(3, n + 1):
        # Agar last same hona hai
        new_same = diff
        
        # Agar last different hona hai
        new_diff = (same + diff) * (k - 1)

        # Update values
        same = new_same
        diff = new_diff

    # Final answer
    return same + diff


# Test
n = 3
k = 2
print(count_ways(n, k))