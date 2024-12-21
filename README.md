# Python vs Rust: Performance Comparison

This project demonstrates a performance comparison between Python and Rust for two common operations:

1. Calculating Fibonacci numbers.
2. Multiplying two numbers.

The goal is to highlight the advantages of using Rust for computationally intensive tasks while showcasing Python's ease of use for quick prototyping.

---

## **Features**
- **Rust Implementation:** Optimized algorithms for Fibonacci calculation and multiplication, compiled as a Python module using PyO3.
- **Python Implementation:** Equivalent algorithms written purely in Python.
- **Performance Metrics:** Measures execution time, CPU usage, and memory usage for each implementation.
- **Real-time Results:** Outputs whichever implementation finishes first.

---

## **Usage**

### **Setup**
1. Install Rust and Python.
2. Add the PyO3 dependency to your `Cargo.toml`:
   ```toml
   [dependencies]
   pyo3 = { version = "0.18", features = ["extension-module"] }
   ```
3. Build the Rust module:
   ```bash
   maturin develop
   ```
4. Install the required Python packages:
   ```bash
   pip install psutil
   ```

### **Run the Program**
1. Execute the Python script:
   ```bash
   python main.py
   ```
2. Follow the menu prompts to:
   - Calculate Fibonacci numbers.
   - Multiply two numbers.

---

## **Example Output**
```text
welcome to the Math Application

Menu:
1. Calculate Fibonacci
2. Multiply Two Numbers
3. Exit
Choose an option: 1
Enter the Fibonacci index: 20
Fibonacci(20) [Rust] = 6765 (time: 0.000077 seconds, CPU: 0.00%, Memory: 16.91 MB)
Fibonacci(20) [Python] = 6765 (time: 0.002380 seconds, CPU: 0.00%, Memory: 17.09 MB)
```

---

## **Performance Insights**
1. **Speed:** Rust significantly outperforms Python for computationally intensive tasks, such as calculating Fibonacci numbers for larger indices.
2. **Resource Efficiency:** Rust uses less memory and takes advantage of multiple threads for improved CPU usage.
3. **Scalability:** Rust remains efficient for large inputs, whereas Python's performance degrades rapidly.

---

## **Why Use Python + Rust?**
This hybrid approach allows you to:
- Utilize Rust for performance-critical components.
- Leverage Python's simplicity for scripting and prototyping.

---

## **Contributing**
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

