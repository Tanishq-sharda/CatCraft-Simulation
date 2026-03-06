# CatCraft Simulation
A Python text-based simulation game demonstrating object-oriented programming and model–view software design.

## Description

This project simulates a small game world where users interact with virtual cats. Each cat has attributes such as health, fish in its stomach, and whether it is wild or tame.

Users can:
- Feed cats
- Hit cats
- Advance to the next night
- Quit the game

The program follows a **model–view structure**:
- `Cat.py` implements the **Cat class (model)** that stores and updates the cat's state.
- `cat_craft.py` implements the **user interface (view)** that interacts with the user and calls methods from the model.

## Technologies

- Python
- Object-Oriented Programming
- Command-line Interface

## How to Run

Clone the repository and run:

```bash
python cat_craft.py
