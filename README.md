# ✊ Rock Paper Scissors

> A command-line Rock, Paper, Scissors game in Python where you play against a computer opponent that picks its move at random.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-completed-brightgreen?style=for-the-badge)
![Project](https://img.shields.io/badge/project-personal-blueviolet?style=for-the-badge)

---

## 📌 About the Project

**Rock Paper Scissors** is an interactive console game written in Python. The player chooses rock, paper or scissors by typing a number, the computer picks its own move at random, and the program draws both hands in ASCII art and announces whether the player won, lost or drew.

This is a **personal project developed independently** as part of my programming portfolio. It was built to practise the full cycle of a simple game: generating a random value, reading player input, displaying the result and applying the rules of the game with conditional logic.

---

## 🎯 Learning Objectives

- **Random number generation**: using `random.randint()` to give the computer an unpredictable move.
- **User input handling**: reading the player's choice from the terminal with `input()` and converting it with `int()`.
- **Conditional logic**: using `if` and `elif` chains to display each move and to decide the winner.
- **Multi-line strings**: storing ASCII art in triple-quoted strings and printing it as the hands of the game.
- **Combining conditions**: using `and` to check the player's move and the computer's move together.
- **Formatted terminal output**: using `\n` inside a prompt to build a readable menu.

---

## ⚙️ How It Works

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Computer     │ -> │ Player picks │ -> │ Show player  │ -> │ Compare the  │ -> │ Print result │
│ picks 1 to 3 │    │ 1, 2 or 3    │    │ and computer │    │ two moves    │    │ Win / Lose / │
│ at random    │    │              │    │ hands        │    │              │    │ Draw         │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

The two moves are compared using the numbers `1` (rock), `2` (paper) and `3` (scissors):

| Player \ Computer | Rock (1) | Paper (2) | Scissors (3) |
|---|---|---|---|
| **Rock (1)** | Draw! | Game Over | You win! |
| **Paper (2)** | You win! | Draw! | Game Over |
| **Scissors (3)** | Game Over | You win! | Draw! |

### Code Walkthrough

```python
import random
computer =random.randint(1,3)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Welcome to the Rock, Paper, Scissors game!')
player=int(input('What do you choose?\n[1]Rock\n[2]Paper\n[3]Scissors\n------> '))

if player == 1:
    print(rock)
if player ==2:
    print(paper)
if player ==3:
    print(scissors)

if computer == 1:
    print('The computer chose Rock')
    print(rock)
if computer ==2:
    print('The computer chose Paper')
    print(paper)
if computer ==3:
    print('The computer chose Scissors')
    print(scissors)

if player == 1 and computer == 2:
    print ('Game Over!!')
elif player == 1 and computer == 3:
    print('You win!')
elif player == 2 and computer == 3:
    print ('Game Over!')
elif player == 2 and computer ==1:
    print('You win!')
elif player == 3 and computer == 1:
    print('Game Over!')
elif player == 3 and computer == 2:
    print('You win!')
if player == computer:
    print('Draw!')
```

| Line / Section | Responsibility |
|---|---|
| `import random` | Loads Python's random module |
| `computer = random.randint(1,3)` | Picks the computer's move: 1, 2 or 3 (both ends included) |
| `rock`, `paper`, `scissors` | Triple-quoted strings holding the ASCII art for each hand |
| `print('Welcome...')` | Shows the welcome message |
| `player = int(input(...))` | Shows the menu and reads the player's choice as a whole number |
| First block of `if` | Prints the hand the player chose |
| Second block of `if` | Announces and prints the hand the computer chose |
| `if / elif` chain | Compares both moves and prints "You win!" or "Game Over" |
| Final `if player == computer` | Prints "Draw!" when both chose the same move |

**Technical note.** `random.randint(1,3)` includes both `1` and `3`, so each of the three moves has the same chance of being picked. The win/lose rules are written as an explicit `if / elif` chain with one branch per losing or winning combination, and the draw is checked in a separate `if` at the end. This keeps each rule easy to read, at the cost of some repetition.

One behaviour worth knowing: the game does not validate the input. A number outside 1 to 3 (for example `4`) prints the computer's move but no result, and text that is not a number (for example `abc`) stops the program with a `ValueError`.

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/) installed
- No external libraries required (`random` is part of Python's standard library)

### Installation and Execution

```bash
git clone https://github.com/guiggsp-hub/Rock-Paper-Scissors.git
cd Rock-Paper-Scissors
python main.py
```

### Sample Run

```
Welcome to the Rock, Paper, Scissors game!
What do you choose?
[1]Rock
[2]Paper
[3]Scissors
------> 1

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

The computer chose Scissors

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You win!
```

---

## 🧠 Skills Demonstrated

`Python` · `Random Module` · `User Input` · `Type Conversion` · `Conditional Logic` · `Boolean Operators` · `Multi-line Strings` · `CLI Applications`

---

## 👤 Author

Developed independently by **Guilherme Garcia** as part of a personal programming portfolio.

[![GitHub](https://img.shields.io/badge/GitHub-guiggsp--hub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/guiggsp-hub)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Guilherme%20Garcia-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-garcia-796633287/)
