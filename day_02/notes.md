# Tip Calculator

## Code Overview
This program calculates how much each person should pay when splitting a bill, including a tip. It takes into account the total bill amount, tip percentage, and number of people sharing the bill.

## Code Breakdown

1. `print("welcome to the tip calculator ")`
   - Displays a welcome message for the tip calculator program

2. `bill = float(input("what was the total amount of the bill ? \n"))`
   - Gets the total bill amount from user
   - `float()` converts the input string to a decimal number
   - Allows for bills with decimal points (e.g., $45.50)

3. `tip = int(input("what percentage amount was tipped ? \n"))`
   - Gets the tip percentage from user
   - `int()` converts the input to an integer
   - Expects whole numbers (e.g., 15 for 15%)

4. `people = int(input("how many people are splitting the bill ? \n"))`
   - Gets the number of people sharing the bill
   - `int()` converts the input to an integer
   - Expects whole numbers (e.g., 4 people)

5. `bill_with_tip = tip/100 * bill + bill`
   - Calculates total bill including tip
   - `tip/100` converts percentage to decimal (e.g., 15% → 0.15)
   - Multiplies bill by tip percentage and adds to original bill
   - Mathematical formula: bill + (bill × tip_percentage)

6. `split = bill_with_tip/people`
   - Calculates amount each person should pay
   - Divides total bill (including tip) by number of people

7. `print(f"the total amount a person must pay including a {tip}% tip is {split}")`
   - Displays final amount per person
   - Uses f-string to insert tip percentage and split amount into message

## Key Concepts
- Type Conversion: Using `float()` and `int()` to convert string inputs to numbers
- Mathematical Operations: 
  - Division (`/`)
  - Multiplication (`*`)
  - Addition (`+`)
- User Input: Getting and processing multiple inputs
- Variables: Storing and manipulating numerical values
- F-strings: Formatting output with variable values

## Program Flow
1. Welcome user
2. Get bill amount (allows decimals)
3. Get tip percentage (whole number)
4. Get number of people (whole number)
5. Calculate total with tip
6. Calculate split amount per person
7. Display result

## Common Pitfalls
- Remember to convert string inputs to appropriate number types
- Order of operations matters in calculations
