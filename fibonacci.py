def fibonacci(x):
    fib_sequence = [0, 1]  # Start with first two terms
    for _ in range(x - 2):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:x]  # Return only the first n terms

try:
    # Accept user input
    x = int(input("Enter a positive integer for Fibonacci sequence: "))

    # Validate input
    if x <= 0:
        print("Error: Please enter a positive integer greater than zero.")
    else:
        # Generate and display Fibonacci sequence
        fibonacci_numbers = fibonacci(x)
        print("Fibonacci Sequence:", fibonacci_numbers)

except ValueError:
    print("Error: Invalid input! Please enter a valid positive integer.")

