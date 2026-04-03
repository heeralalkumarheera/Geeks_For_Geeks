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