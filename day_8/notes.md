# Caesar Cipher Program Notes

## Overview
This program (`ceasercypher.py`) attempts to implement a Caesar Cipher, a simple substitution technique where each letter in the text is shifted by a fixed number of positions down the alphabet.

## Code Breakdown

### Variables
- `alphabet`: A list containing all lowercase English letters from 'a' to 'z'.
- `direction`: Takes user input to decide whether to 'encode' or 'decode'. **Note:** This variable is currently collected but not used in the logic; the program runs both encryption and decryption regardless of this input.
- `text`: The message input by the user to be processed.
- `shift`: The integer amount to shift the letters by.

### Functions
#### `encrypt(text, shift)`
This function handles the core logic:
1.  **Encryption Loop**:
    - Iterates through each character in the input `text`.
    - Finds the index of the character in the `alphabet` list.
    - Calculates the new position by adding `shift` to the current index.
    - Appends the character at the new position to `cypher_text`.
    - *Current Limitation*: If `pos + shift` exceeds 25 (the last index of `alphabet`), the program will raise an `IndexError`. It does not wrap around to the beginning of the alphabet.

2.  **Decryption Loop**:
    - Takes the generated `cypher_text`.
    - Iterates through each character.
    - Calculates the original position by subtracting `shift`.
    - Appends the character to `plain_text`.
    - Prints the decrypted value.

## Current Limitations & Potential Improvements
1.  **Index Out of Range**: The code does not handle wrapping around the alphabet (e.g., shifting 'z' by 1 should be 'a'). This requires using the modulo operator (`%`) or checking bounds.
2.  **Unused Logic**: The `direction` input is ignored. The code should ideally check `if direction == "encode":` or `decode` to choose which path to take.
3.  **Non-Alphabet Characters**: The code assumes all characters in `text` exist in the `alphabet` list. Spaces, numbers, or symbols will cause a `ValueError` when `alphabet.index()` is called.
