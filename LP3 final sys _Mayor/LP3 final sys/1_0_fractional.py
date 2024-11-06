def knapsack(weights, values, capacity):
    # n is the number of items
    n = len(weights)
    
    # Create a 2D DP table where dp[i][w] will store the maximum value 
    # that can be obtained using the first i items and capacity w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Iterate through each item (i from 1 to n) and each weight capacity (w from 1 to capacity)
    for i in range(1, n + 1):  # i represents the number of items considered (1 to n)
        for w in range(1, capacity + 1):  # w represents the current capacity being considered (1 to capacity)
            
            # If the weight of the current item is less than or equal to the current capacity
            if weights[i - 1] <= w:  # We use i-1 because the dp table is 1-indexed but the lists are 0-indexed.
                # Option 1: Exclude the item - the value will be the same as the previous row (dp[i-1][w])
                # Option 2: Include the item - add the value of the item and the remaining value from the previous row (dp[i-1][w - weights[i - 1]])
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # If the item cannot be included (because its weight is greater than the current capacity w)
                # The maximum value is the same as not including the item (take the previous row value)
                dp[i][w] = dp[i - 1][w]
    
    # The bottom-right cell of the dp table (dp[n][capacity]) contains the maximum value
    # that can be obtained with the full list of items and the full capacity.
    return dp[n][capacity]

# Example usage:
weights = [10, 40, 20, 30]  # Weights of the items
values = [60, 40, 100, 120]  # Values of the items
capacity = 50  # Capacity of the knapsack

# Call the knapsack function to calculate the maximum value that can be carried in the knapsack
max_value = knapsack(weights, values, capacity)

# Print the result
print("Maximum value in Knapsack =", max_value)
