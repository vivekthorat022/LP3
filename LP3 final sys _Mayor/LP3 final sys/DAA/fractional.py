# Function to calculate the maximum value in the knapsack
def fractional_knapsack(weights, values, capacity):
    # Calculate the ratio of value/weight for each item
    n = len(weights)  # Get the number of items
    # Create a list of tuples containing (value/weight ratio, index)
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    
    # Sort items by value/weight ratio in decreasing order
    ratios.sort(reverse=True, key=lambda x: x[0])  # Sort based on the first element of the tuple (the ratio)

    total_value = 0  # Initialize total value of the knapsack
    for ratio, i in ratios:  # Iterate over sorted items
        if weights[i] <= capacity:  # If the whole item can fit in the knapsack
            total_value += values[i]  # Add the full value of the item to total_value
            capacity -= weights[i]  # Decrease the remaining capacity of the knapsack
        else:
            # If only a fraction of the item can fit
            total_value += values[i] * (capacity / weights[i])  # Add the fraction of the item's value
            break  # Break out of the loop as the knapsack is now full
        
    return total_value  # Return the maximum value that can be carried in the knapsack

# Example usage
weights = [10, 30, 20, 20]  # List of weights for each item
values = [60, 40, 100, 120]  # List of values for each item
capacity = 50  # Maximum weight capacity of the knapsack

# Call the fractional_knapsack function and store the result in max_value
max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", max_value)  # Print the maximum value that can be carried in the knapsack