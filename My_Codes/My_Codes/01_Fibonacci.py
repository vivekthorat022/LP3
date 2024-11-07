def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return ( recursive_fibonacci(n - 1) + recursive_fibonacci(n-2) )
    
def iterative_fibonacci(limit):
    a, b = 0, 1
    steps = 0
    while(a <= limit):
        print(a, end = " ")
        a, b = b, (a+b)
        steps += 1
    print()
    return steps

if __name__ == "__main__":
    limit = int(input("\nEnter limit for Fibonacci Sequence (Iterative) : "))

    print("\nFibonacci Sequence (Iterative) : ")
    steps_iterative = iterative_fibonacci(limit)
    print(f"Number of steps in Iterative Approach : {steps_iterative}")

    n = int(input("\nEnter position for Fibonacci Sequence (Recursive) :"))

    print(f"\nFibonacci Number at position {n} (Recursive) : {recursive_fibonacci(n)}")