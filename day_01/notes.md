# Day 1: Brand Name Generator

## Code Overview
This program creates a brand name by combining the user's hometown and pet name.

## Code Breakdown

1. `print("welcome to the brand name generator")`
   - Displays a welcome message to the user

2. `last = input("enter the city you grew up in\n")`
   - Uses Python's `input()` function to get user input
   - Stores the city name in variable `last`
   - `\n` creates a new line after the prompt

3. `first = input("enter the name of your pet\n")`
   - Gets another input from the user
   - Stores the pet name in variable `first`
   - `\n` creates a new line after the prompt

4. `print(f"the name of your brand will be {first} {last}")`
   - Uses an f-string to format the output
   - `{first}` and `{last}` are placeholders that get replaced with the actual values
   - Combines the pet name and city name with a space between them

## Key Concepts
- User Input: Using `input()` function to get data from users
- Variables: Storing user input in variables for later use
- F-strings: Modern string formatting in Python using `f"..."` syntax
- String concatenation: Combining multiple strings into one output

## Program Flow
1. Welcome message
2. Get city name from user
3. Get pet name from user
4. Combine inputs to generate brand name
5. Display final brand name to user