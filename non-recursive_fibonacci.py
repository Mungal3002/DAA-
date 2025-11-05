# Program to calculate Fibonacci numbers and count steps

def fibonacci(n):
    a, b = 0, 1
    step_count = 0  # Initialize step counter

    if n == 0:
        step_count += 1
        return a, step_count
    elif n == 1:
        step_count += 1
        return b, step_count

    for i in range(2, n + 1):
        step_count += 1   # Count each loop iteration
        c = a + b
        a = b
        b = c

    return b, step_count

# Input
n = int(input("Enter the term number (n): "))

# Output
fib_num, steps = fibonacci(n)
print(f"Fibonacci number at position {n} is {fib_num}")
print(f"Total steps taken: {steps}")
