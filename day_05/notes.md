# Day 05 notes

## Overview
Today's main exercise is building a random password generator in Python. The program lets the user choose how many letters, numbers, and special characters they want in their password, then generates a randomized password accordingly.

## Code Breakdown
1. **Imports and setup**
   - `import random` — for random selection and shuffling.
   - Lists for letters, numbers, and special characters are defined.

2. **User input**
   - The user is prompted for the number of letters, numbers, and special characters they want in their password.
   - Inputs are converted to integers for use in loops.

3. **Password construction**
   - The program randomly selects the requested number of letters, numbers, and symbols, and appends them to a list.
   - The list is shuffled to ensure the password is not predictable (e.g., all letters first, then numbers, then symbols).
   - The shuffled list is joined into a single string to form the final password.

4. **Output**
   - The generated password is printed to the user.

## Key Concepts
- Lists and list operations (append, shuffle, join)
- Random selection (`random.choice`)
- User input and type conversion
- String manipulation

## Example Usage
How many letters do you need in your password? 4
How many numbers do you need in your password? 2
How many special characters do you need in your password? 3
Generated password: a1b@c$2*


