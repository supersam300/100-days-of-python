# Project Notes: Day 10 - Calculator App

## Overview
This project is a simple command-line calculator application written in Python. It allows users to perform basic arithmetic operations and chain calculations using the result of the previous operation.

## Features
- **Basic Arithmetic**: Supports Addition (+), Subtraction (-), Multiplication (*), and Division (/).
- **Continuous Calculation**: Users can continue calculating with the result of the previous operation.
- **Recursive Interface**: The calculator restarts nicely if the user chooses to start a new calculation.
- **Unit Tests**: Includes a test suite (`test_calculator.py`) using `unittest` to verify core functions.

## Code Structure
- **`code.py`**: Main application logic.
  - Helper functions: `add`, `subtract`, `multiply`, `divide`.
  - `operations` dictionary: Maps symbols to functions.
  - `calculator()`: Main loop handling user input and flow control.
- **`test_calculator.py`**: Unit tests for the arithmetic functions.

## How to Run
1.  **Run the App**:
    ```bash
    python3 day_10/code.py
    ```
2.  **Run Tests**:
    ```bash
    python3 day_10/test_calculator.py
    ```

## Future Improvements (TODO)
- [ ] Add input validation (handle non-numeric inputs).
- [ ] Handle division by zero errors.
- [ ] Add more advanced operations (exponents, roots).
