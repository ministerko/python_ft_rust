import time
import rust_math
import psutil
from concurrent.futures import ThreadPoolExecutor

def python_fibonacci(n):
    """Calculate Fibonacci in pure Python."""
    if n <= 1:
        return n
    return python_fibonacci(n - 1) + python_fibonacci(n - 2)

def python_multiply(a, b):
    """Multiply two numbers in pure Python."""
    return a * b

def measure_resources():
    """Get CPU and memory usage."""
    process = psutil.Process()
    cpu = process.cpu_percent(interval=0.1)
    memory = process.memory_info().rss / (1024 * 1024)  # Convert to MB
    return cpu, memory

def main():
    print("welcome to the Math Application")
    while True:
        print("\nMenu:")
        print("1. Calculate Fibonacci")
        print("2. Multiply Two Numbers")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            n = int(input("Enter the Fibonacci index: "))

            def calculate_rust():
                start_rust = time.time()
                result_rust = rust_math.fibonacci(n)
                end_rust = time.time()
                cpu, memory = measure_resources()
                print(f"Fibonacci({n}) [Rust] = {result_rust} "
                      f"(time: {end_rust - start_rust:.6f} seconds, CPU: {cpu:.2f}%, Memory: {memory:.2f} MB)")

            def calculate_python():
                start_python = time.time()
                result_python = python_fibonacci(n)
                end_python = time.time()
                cpu, memory = measure_resources()
                print(f"Fibonacci({n}) [Python] = {result_python} "
                      f"(time: {end_python - start_python:.6f} seconds, CPU: {cpu:.2f}%, Memory: {memory:.2f} MB)")

            with ThreadPoolExecutor() as executor:
                executor.submit(calculate_rust)
                executor.submit(calculate_python)

        elif choice == "2":
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))

            def multiply_rust():
                start_rust = time.time()
                result_rust = rust_math.multiply(a, b)
                end_rust = time.time()
                cpu, memory = measure_resources()
                print(f"{a} * {b} [Rust] = {result_rust} "
                      f"(time: {end_rust - start_rust:.6f} seconds, CPU: {cpu:.2f}%, Memory: {memory:.2f} MB)")

            def multiply_python():
                start_python = time.time()
                result_python = python_multiply(a, b)
                end_python = time.time()
                cpu, memory = measure_resources()
                print(f"{a} * {b} [Python] = {result_python} "
                      f"(time: {end_python - start_python:.6f} seconds, CPU: {cpu:.2f}%, Memory: {memory:.2f} MB)")

            with ThreadPoolExecutor() as executor:
                executor.submit(multiply_rust)
                executor.submit(multiply_python)

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    import psutil
    main()
