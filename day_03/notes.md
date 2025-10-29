# Day 3: Treasure Island — Notes

## Code overview
This is a simple text-based adventure that asks the player to make a series of choices to find the treasure. The program demonstrates branching with nested conditionals and user input handling.

## Valid inputs / expected answers
- First choice (`choice1`): the code checks for the exact string "left" to continue the game. Any other input leads to a game-over branch.
- Second choice (`choice2`): the code checks for the exact string "wait" to proceed. Any other input (for example "swim") results in a game-over.
- Third choice (`choice3`): valid winning choice is "yellow". "red" and "blue" are explicitly handled as game-over outcomes.

Notes: the current implementation compares raw input strings, so inputs are case-sensitive and must match exactly (for example, "Left" or trailing spaces will not match).

## Code breakdown (step-by-step)
1. `print("welcome to treasure island!")`
   - Prints the welcome banner.

2. `print("your mission is to find the treasure")`
   - Explains the player's objective.

3. `choice1 = input("<----left.  Choose a path  .right----->\n")`
   - Prompts the player for the first decision: go left or right.

4. `if choice1 == "left":` ... `else: ...`
   - If the player types exactly "left" the story continues. Any other response goes to the `else` block and ends the game.

5. Inside the `left` branch the player sees a lake and is asked `choice2 = input("<----swim. Choose a path .wait----->\n")`.
   - If the player types exactly "wait" the game continues to the doors section; otherwise they drown and the game is over.

6. If `choice2 == "wait"` the player is shown three magical doors and asked to pick one:
   - `choice3 = input("<-----red <-----yellow-----> blue----->\n")`
   - If they type `"yellow"` they win. If `"red"` or `"blue"`, each branch contains a different game-over message.

7. All other branches not matching the exact expected strings result in game-over messages.

## Key concepts demonstrated
- Conditional statements (`if`, `elif`, `else`) and nesting.
- User input with `input()` and storing values in variables.
- Simple branching narrative based on user choices.

## Common pitfalls and notes for improvement
- Case sensitivity: Input comparisons are exact. Use `.lower().strip()` on input to accept different cases and remove accidental spaces, e.g. `choice1 = input(...).lower().strip()`.











