
# %% imports ------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# %% commands -----------------------------------------------------------------
print("Everything works!")

var = 3

var2 = var * 2

var3 = var2 ^ 3


# %% GitHub Copilot testing ---------------------------------------------------
# Copilot suggested this functions as auto complete under my guidance.

# function to compute Fibonacci numbers

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1

    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# function to compute the golden ratio

def golden_ratio(n):
    return fibonacci(n) / fibonacci(n - 1)

# %%
