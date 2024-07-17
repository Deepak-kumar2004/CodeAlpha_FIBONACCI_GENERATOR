def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        result = fibonacci(n)
        print(f"The first {n} terms of the Fibonacci sequence are:")
        print(result)

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()