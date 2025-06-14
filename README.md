# Algebraic-Number-Guess-Game
Interactive Python CLI puzzle: choose operations, get an equation, solve for x, and see if you guessed the hidden number. (My first Python Project)

## Run it
```bash
# clone or download the repo
git clone https://github.com/sakshambista11/Algebraic-Number-Guess-Game.git
cd Algebraic-Number-Guess-Game

# run the script
Algebraic-Number-Guess-Game.py
```
Requires Python 3.10+ (no external libraries).

## Features
- Random number from 1–100 each round
- Input validation so out of range guesses get re-prompted
- Two math operations (* or /, then + or -) chosen by the player
- Friendly success / failure messages

## How it Works
- Game picks a random number with random.randint.
- Player picks operations; program builds an algebraic expression.
- Player solves expression to “guess” the number.
- Script checks the answer and prints a result.

## Roadmap/Future Ideas
- “Play again?” loop with attempt counter
- Difficulty modes (e.g. 1 – 50, 1 – 500)
- Hint system (higher / lower) or limited lives
- Develop the game with a GUI

## What I Learned
- Modular function design and return values
- Validating user input with while loops and exception handling
- Basic Git workflow (commits, pushes, README writing)





