def fibonacci(n):
    if n <= 0:
        print("Invalid input. Please enter a positive integer.")
        return
    elif n == 1:
        print("Fibonacci Series:")
        print(0)
    elif n == 2:
        print("Fibonacci Series:")
        print(0)
        print(1)
    else:
        print("Fibonacci Series:")
        a, b = 0, 1
        print(a)
        print(b)
        for _ in range(2, n):
            c = a + b
            print(c)
            a, b = b, c

# Example usage:
fibonacci(10)  # Change the argument to get desired number of Fibonacci numbers
