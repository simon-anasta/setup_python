# Notes made during chapter 1 of Automate the Boring Stuff With Python
# 2025-11-22

# %% imports ------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# %% exponentiation -----------------------------------------------------------

vector = [ii for ii in range(100)]

star = [ii * 2 for ii in vector]
doublestar = [ii ** 2 for ii in vector]
hat = [ii ^ 2 for ii in vector]

# plot
plt.scatter(vector, star)
plt.scatter(vector, doublestar)
plt.scatter(vector, hat)

# conclusions
# star for multiple
# doublestar for exponentiation
# hat for bit-wise XOR (not maths)

# %% division -----------------------------------------------------------------

slash = [ii / 3 for ii in vector]
doubleslash = [ii // 3 for ii in vector]
percent = [ii % 3 for ii in vector]

# plot
plt.scatter(vector, slash)
plt.scatter(vector, doubleslash)
plt.scatter(vector, percent)

# conclusions
# slash is decimal division
# doubleslash is integer division (rounding down)
# percent is modulo

# %% strings ------------------------------------------------------------------

# double or single quotes work
'a' + "b"
'a"b' + "c'd"
# Single are the default (become \' within text)

# convert to string
str(1) + str(0)
# convert to number
int(str(1) + str(5))
float(str(1) + '.' + str(5))

# console input
my_name = input('>')
# does not work - Jupyter does not have a console

# %% string input via widget --------------------------------------------------

from ipywidgets import widgets
from IPython.display import display

text = widgets.Text(description = "Enter name")
display(text)
print(text.value)
# this is dynamic
# text.value updates with the text in the widget

# %% better input handling via widget -----------------------------------------

text = widgets.Text(description='Your name:')

# Function to run when user presses Enter
def on_submit(change):
    # Print the value
    print("You entered:", text.value)
    
    # Hide the widget
    # text.layout.display = 'none'
    text.close()

# Trigger the function when Enter is pressed
text.on_submit(on_submit)

display(text)

# %% even better input handling via widget and function -----------------------

import threading

def input0(description):
    done = threading.Event()

    text = widgets.Text(description = description)

    def on_submit(change):
        text.close()
        done.set()

    text.on_submit(on_submit)

    display(text)
    done.wait()

    return(text.value)

answer = input0('Name? ')
print(answer)

# this does not work
# Juypter handling is asynchronous
# threading interfers with this

# %% help documentation -------------------------------------------------------

help(round)
help(abs)



