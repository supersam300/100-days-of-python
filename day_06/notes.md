# Day 6: Notes

## Project Overview
Today's project is a Hangman game implementation split across multiple Python files for better organization:

- `code.py` — Main game logic and word selection
- `layers.py` — ASCII art for different hangman states
- `makeDashes.py` — Helper function to create the word display

## File Breakdown

### `layers.py`
This module manages the visual representation of the hangman's state.

**Key Features:**
- Function `layers(num)` returns ASCII art for different game states
- Takes a number (1-7) representing game progress
- Contains 7 different hangman states:
  1. Empty gallows
  2. Head only
  3. Head and body
  4. Head, body, one arm
  5. Head, body, both arms
  6. Head, body, arms, one leg
  7. Complete hangman


### `makeDashes.py`
Helper module for displaying the word's state during gameplay.

**Purpose:**
- Creates the initial display for the hidden word
- Shows progress as letters are guessed
- Maintains game state visibility

### `code.py`
Main game file that ties everything together.

**Components:**
- Word selection from predefined list
- Integration with `layers.py` for visual state
- Game loop and logic implementation
- Input handling and validation

## Key Python Concepts Demonstrated
1. **Modular Programming**
   - Splitting code across multiple files
   - Using imports to share functionality

2. **String Manipulation**
   - Multi-line strings for ASCII art
   - String formatting for game display

3. **Function Design**
   - Clear parameter handling
   - Proper return values
   - Default behaviors

4. **Code Organization**
   - Logical separation of concerns
   - Reusable components

## Common Pitfalls and Solutions
- Remember to return values from functions to avoid 'None' output
- Maintain consistent indentation in ASCII art
- Use proper function definition syntax (`def` not `define`)
- Handle edge cases in input validation

## Example Game Flow
```
Welcome to Hangman!
Word: _ _ _ _ _
Guesses left: 6

+---+
|   |
O   |
    |
    |
    |
=========

Guess a letter: a
```

## Testing and Debugging Tips
1. Test `layers.py` independently:
   ```python
   print(layers(1))  # Should show empty gallows
   print(layers(7))  # Should show complete hangman
   ```

2. Verify `makeDashes.py`:
   ```python
   print(make_dash(5))  # Should show "_ _ _ _ _"
   ```

3. Check game state management in `code.py`

---
