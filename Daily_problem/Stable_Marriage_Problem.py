# You are given two arrays men[] and women[], each of length n, where:

# men[i] represents the preference list of the i-th man, ranking all women in order of preference.
# women[i] represents the preference list of the i-th woman, ranking all men in order of preference.
# The task is to form n pairs (marriages) such that:

# Each man is matched with exactly one woman, and each woman is matched with exactly one man.
# The matching is stable, meaning there is no pair (man, woman) who both prefer each other over their current partners.
# It is guaranteed that a stable matching always exists. Return the stable matching from the men’s perspective, i.e., the one where men are considered for the final output.
# Return an array result[] of size n, where result[i] denotes the index (0-based) of the woman matched with the i-th man.

# Examples: 

# Input: n = 2, men[] = [[0, 1], [0, 1], women[] = [[0, 1], [0, 1]]
# Output: [0, 1]
# Explanation:
# Man 0 is married to Woman 0 (his first choice and her first choice).
# Man 1 is married to Woman 1 (his second choice and her second choice).
# Input: n = 3, men[] = [[0, 1, 2], [0, 1, 2], [0, 1, 2]], women[] = [[2, 1, 0], [2, 1, 0], [2, 1, 0]]
# Output: [2, 1, 0]
# Explanation:
# Man 0 is married to Woman 2 (his third choice and her third choice).
# Man 1 is married to Woman 1 (his second choice and her second choice).
# Man 2 is married to Woman 0 (his first choice and her first choice).
# Constraints: 
# 2 ≤ n ≤ 103
# 0 ≤ men[i] ≤ n - 1
# 0 ≤ women[i] ≤ n - 1

# Expected Complexities
# Time Complexity: O(n^2)
# Auxiliary Space: O(n^2)

#gfg solution
class Solution:
    def stableMarriage(self, men, women):
        # Step 1: Get n
        n = len(men)
        
        # Step 2: Initialize all men as free
        free_men = list(range(n))
        
        # women_partner[w] = man engaged to woman w
        women_partner = [-1] * n
        
        # men_next_proposal[m] = next woman index to propose
        men_next_proposal = [0] * n
        
        # Step 3: Create ranking for women
        women_rank = [[0] * n for _ in range(n)]
        
        for w in range(n):
            for rank, man in enumerate(women[w]):
                women_rank[w][man] = rank
        
        # Step 4: Gale-Shapley Algorithm
        while free_men:
            man = free_men.pop(0)
            
            # Next woman to propose
            woman = men[man][men_next_proposal[man]]
            men_next_proposal[man] += 1
            
            # If woman is free
            if women_partner[woman] == -1:
                women_partner[woman] = man
            
            else:
                current_partner = women_partner[woman]
                
                # If woman prefers new man
                if women_rank[woman][man] < women_rank[woman][current_partner]:
                    women_partner[woman] = man
                    free_men.append(current_partner)
                else:
                    free_men.append(man)
        
        # Step 5: Build result (man -> woman)
        result = [0] * n
        for w in range(n):
            m = women_partner[w]
            result[m] = w
        
        return result