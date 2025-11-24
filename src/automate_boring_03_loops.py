# Notes made during chapter 3 of Automate the Boring Stuff With Python
# 2025-11-23

# %% input alternative with while loop ----------------------------------------

# does not work
# something not sync'ed between widget and script
from ipywidgets import widgets
from IPython.display import display
import time

text = widgets.Text(description='Your name:')
display(text)

while not " " in text.value or not "\n" in text.value:
    time.sleep(1)

text.close()
print(text.value)

# %% range options ------------------------------------------------------------
# [closed, open) format 

# num steps
for ii in range(10):
    print(ii)

# start and stop
for ii in range(10, 20):
    print(ii)

# start, stop, increment
for ii in range(10, 20, 2):
    print(ii)

# reverse
for ii in range(5, -1, -1):
    print(ii)

# %% random numbers -----------------------------------------------------------

import random

random.random()
random.sample(range(20), 20)

qq = ['a','b','c']
random.choices(qq, k = 4)

# %% example control flow -----------------------------------------------------

for ii in range(100):

    break_condition = abs(random.randint(0,100) - ii) < 3
    no_work_to_do = abs(random.randint(0,100) - ii) < 6

    if break_condition:
        print("breaking")
        break # exit loop

    if no_work_to_do:
        print("continuing")
        continue # return to start of loop

    pass # do nothing


# %%
