# Day 4 notes

## Overview
Day 4 contains a small set of examples for working with user input, modules, and simple game logic. The main files in this folder are:

- `code.py` — an example/exercise script for the day's practice. Inspect it to see the exact exercise used.
- `rock_paper_scissors.py` — a command-line Rock/Paper/Scissors game that imports move values from `rpc_module.py` and uses `random.choice` to pick the computer's move.
- `rpc_module.py` — a small module that defines the constants used by the game such as `rock`, `paper`, and `scissor`.

## `rpc_module.py` (module of choices)
- Purpose: centralize the game's choice values so other scripts can import them.
- Typical contents: simple assignments like `rock = "rock"`, `paper = "paper"`, `scissor = "scissors"` (or similar).

Checklist / improvements:
- Keep naming consistent (`scissor` vs `scissors`); prefer one form everywhere.
- Use string values that are easy to print and compare (e.g., `"rock"`).

## `rock_paper_scissors.py` (game script)
What it does:
- Imports `random` and `rpc_module`.
- Builds a list of choices from `rpc_module` and uses `random.choice` to select the computer's move.
- Reads an integer input from the user (0/1/2) to select rock/paper/scissors.
- Compares the player's choice and the computer's choice and prints the result.

Important lines & observations
- Choices list construction:
  - `rpc_choice = [rpc_module.paper, rpc_module.rock, rpc_module.scissor]`
    - The list order defines the numeric mapping (index → move). Document which index maps to which move.
- Random selection (bug observed):
  - Wrong: `com_choice = random.choice[rpc_choice]` (raises TypeError because `random.choice` is a function and cannot be subscripted).
  - Right: `com_choice = random.choice(rpc_choice)`
- Input parsing and indexing:
  - `choice = int(input("enter your choice : rock(0),paper(1),scissors(2)\n"))`
  - Validate `choice` is 0, 1, or 2 before using it as an index to avoid IndexError.
- Boolean logic bug:
  - Wrong: using `&` where `and` is intended (e.g., `a == rock & b == scissor`). Use `and` for logical conjunction.
- Printing values:
  - Prefer `print(rpc_choice[choice])` instead of concatenation if the values are not guaranteed to be strings.

Common pitfalls in current script
- TypeError from calling `random.choice` with square brackets.
- Using bitwise `&` instead of logical `and`.
- No input validation (ValueError/IndexError risk).
- Inconsistent naming (`scissor` vs `scissors`).




