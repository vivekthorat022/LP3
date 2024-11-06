# Initialize the first two Fibonacci numbers
a, b = 0, 1  # 'a' is the current Fibonacci number, 'b' is the next one
steps = 0  # Initialize a counter to track the number of steps taken

# Get input from the user
limit = int(input("Enter the limit: "))  # Prompt the user for a limit and convert it to an integer

# Print the Fibonacci sequence and count the steps
print("Fibonacci Sequence:")  # Print a header for the Fibonacci sequence
while a <= limit:  # Continue generating Fibonacci numbers until 'a' exceeds the limit
    print(a, end=" ")  # Print the current Fibonacci number without a newline
    a, b = b, a + b  # Update 'a' to 'b' (next number) and 'b' to 'a + b' (next Fibonacci number)
    steps += 1  # Increment the step counter for each Fibonacci number generated

print("\nNumber of steps:", steps)  # Print the total number of steps taken to generate the sequence

# The Fibonacci formula used here is: F(n) = F(n−1) + F(n−2)
