# AI_Basics
This project consists of two directories; 1_planning and 2_optimising.

In the 1_planning directory, a minimax algorithm is implemented for Tic Tac Toe AI.

In the 2_optimising directory, algorithms are implemented to optimise a toaster by **Exhaustive Search, Hill-climbing, and Gradient Ascent (+Epochs)**.

The project is managed by Poetry and uses Python 3.10.

## Prerequisites
- Python 3.10
- [poetry](https://python-poetry.org/)

## Installing
1.  Clone the repository using `git clone <repository_url>`.

2. Activate poetry virtual environment.
```
# Create a virtual environment
$ poetry shell
# Install all packages
$ poetry install
```

## Getting Started
### Tic Tac Toe AI
1_planning uses Pygame to create the Tic Tac Toe game. The minimax algorithm is implemented in the tictactoe.py file.
```
# Don't move to 1_planning folder
$ python 1_planning/runner.py
```
<img width="346" alt="Screenshot 2023-04-25 at 14 46 02" src="https://user-images.githubusercontent.com/78789212/234280846-9aed320e-502f-406e-afc3-e891eb37c0bc.png">


### Optimisation of a Toaster
To optimise the toaster, navigate to the 2_optimising directory. 

The main.py file contains the **OptimiseAlgo** class, which implements the optimisation algorithms. 

Run the main.py file to check the class. 

However, it is recommended to view the **toast.ipynb** file, which contains a more detailed explanation of each optimisation algorithm and the results.
```
$ cd 2_optimising
$ python main.py
```

