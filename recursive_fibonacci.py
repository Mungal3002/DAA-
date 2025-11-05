#recursive fibonacci
def fib_recursive(n, step_count=0):
    step_count += 1
    if n == 0:
        return 0, step_count
    elif n == 1:
        return 1, step_count
    else:
        a, step_count = fib_recursive(n - 1, step_count)
        b, step_count = fib_recursive(n - 2, step_count)
        return a + b, step_count

n = int(input("Enter n: "))
fib, steps = fib_recursive(n)
print(f"Fibonacci number at position {n} is {fib}")
print(f"Total steps: {steps}")
