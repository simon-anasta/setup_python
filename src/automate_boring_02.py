# Notes made during chapter 2 of Automate the Boring Stuff With Python
# 2025-11-22

# %% logicals -----------------------------------------------------------------

# and is prefered over &
# or is prefered over |
# as have shortcircuiting

# and and or can be applied to non-logicals
6 and 5 # = 5
6 or 5 # = 6

# and & or take later precedence
4 < 6 and 4 < 5 # = True
(4 < 6) and (4 < 5) # = True
4 < (6 and 4) < 5 # = False

# and resolves before or
False and False or True # = True
True or False and False # = True
# order of `and` and `or` does not matter
(True or False) and False # = False

# not resolves first
not False or True # = True
True or not False # = True
(not False) or True # = True
not (False or True) # = False



# %% if, else, elif -----------------------------------------------------------

def fizzbuzz(num):

    if num % 12 == 0:
        return("fizzbuzz")
    if num % 4 == 0:
        return('fizz')
    elif num % 3 == 0:
        return('buzz')
    else:
        return(str(num))

vector = [fizzbuzz(ii+1) for ii in range(20)]

# %%
