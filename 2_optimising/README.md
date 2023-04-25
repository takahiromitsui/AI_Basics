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
### Optimisation of a Toaster
To optimise the toaster, navigate to the 2_optimising directory. 

The main.py file contains the **OptimiseAlgo** class, which implements the optimisation algorithms.

- Exhaustive Search: Easy/Simple
- Hill-climbing: Medium
- Gradient Ascent(+Epochs): Hard and Very hard

Run the main.py file to check the class. 

However, it is recommended to view the **toast.ipynb** file, which contains a more detailed explanation of each optimisation algorithm and the results.
```
$ cd 2_optimising
$ python main.py
```
