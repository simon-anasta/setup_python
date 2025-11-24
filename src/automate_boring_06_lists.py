# Notes made during chapter 6 of Automate the Boring Stuff With Python
# 2025-11-24

# %% Lists --------------------------------------------------------------------

# make a list
new_list = [1, 2, 3]
# fetch values
print(new_list[0]) # Python is zero indexed
print(new_list[1])
print(new_list[2])
print(new_list[3]) # index out of range

len(new_list)

# types can be mixed
newer_list = [1, 'a', None, False]
print(newer_list)
type_list = [type(ii) for ii in newer_list]
print(type_list)

# membership can be checked
'a' in newer_list
None not in newer_list

# %% Fetching via indexes -----------------------------------------------------

my_list = [ii for ii in range(10)]

# negative indexes fetch from end of list
my_list[-2] # second from the end

# colon to fetch range
my_list[3:5] # zero indexed nd excluding last value
my_list[3:3] # empty as excludes last entry
my_list[3:1] # also empty

my_list[:] # the whole list
my_list[4:] # list starting from 4
my_list[:6] # list up to 6
my_list[:-3] # list up to 3rd-to-last

# %% Manipulation -------------------------------------------------------------

# lists are mutable / updatable
my_list = ['a', 'b', 'c']
my_list[2] = 'd'
print(my_list)

# concatenate
print(my_list + 'e') # fails as 'e' is not a list
print(my_list + ['e']) # works

# replicate
my_list * 2

# remove items
del my_list[1]
print(my_list)

# del also removes variables
var = 1
del var
print(var) # errors

# %% Unpacking ----------------------------------------------------------------

full_name = ['John', 'Doe', 'Smith']
first, middle, last = full_name
# number of values on left side must be an exact match
print(first)

# %% Enumerate for index and value --------------------------------------------

my_list = ['a', 'b', 'c', 'd', 'e']

for index, item in enumerate(my_list):
    print('-------------')
    print(index)
    print(item)
    print('Position ' + str(index) + ' has item ' + item)

# get indexes
indexes = [ii for ii, value in enumerate(my_list)]
print(indexes)
indexes = [ii for ii in range(len(my_list))]
print(indexes)

# %% Augmented assignment -----------------------------------------------------

value = 0
while value < 5:
    value += 1
    print(value)

# five options
# += -= /= *= %=

# work on strings
value = 'a'
value += 'b'

# work on lists
value = ['a']
value += ['b']

# %% List methods -------------------------------------------------------------

my_list = [1,2,3,4,3,5,6]

# index
my_list.index(2) # index of argument
my_list.index(3) # multiple matches, returns first one
my_list.index(9) # error with no matches

# append
my_list.append(7) # value added to end
my_list

# insert
my_list.insert(3, 99)
# position 3 becomes 99
# all other values shifted backwards

# remove
my_list.remove(99)
my_list.remove(3) # only removes first match

# sort
my_list.sort()
# modifies in place
# errors is list is of mixed type

mylist = ['a', 'A', 'boo','ba', 'Bee']
mylist.sort()
# capitals sort before lowercase (ASCIIbetical)

# reverse
# modifies in place
my_list.reverse()

# %% Long lines ---------------------------------------------------------------

# open brackets naturally continue to next line
my_list = [1,
           2,
           3
        ]

# use slash otherwise
1 + \
2 + \
3

# %% Strings are sequences ----------------------------------------------------

# just like lists
my_string = 'qwerty'
my_string[0]
my_string[-1]

# but not mutable - these error
my_string.sort()
my_string[2] = 'x'
# build a new string instead

# convert to list
list(my_string)
# convert back to string
''.join(my_list)

# %% tuple --------------------------------------------------------------------
# use to communicate contents are unchanged
# slight optimisation is execution

# made with brackets
my_tuple = ('a','b','c')
length_one_tuple = ('a',) # needs trailing comma

# also immutable
my_tuple.sort() # errors
del my_tuple[2] # errors

# convertable
a_list = list(my_tuple)
a_tuple = tuple(my_list)

# %% Lists are refered not copied ---------------------------------------------

list1 = [1,2,3]
list2 = list1
list1.append(4)

print(list2) # also contains the value 4

import copy
list2 = copy.copy(list1)
list1.append(5)
print(list2) # does not contain the value 5

# copy.deepcopy to copy lists within lists

# %% Matrix screensaver -------------------------------------------------------

import random, time

def matrix_screen(width = 50, length = 100):
    """Displays matrix-style screen of given width"""
    assert isinstance(width, int)
    assert isinstance(length, int)
    
    # setup
    state = [0] * width
    display = [' '] * width
    
    # loop
    for ii in range(length):
        # loop over width
        for jj in range(width):
            # restart stream
            if random.random() < 0.03:
                state[jj] = random.randint(4, 14)
            
            if state[jj] == 0:
                display[jj] = ' '
            else:
                display[jj] = random.choice(['0','1'])
                state[jj] -= 1
        
        # conclude
        print(''.join(display))
        time.sleep(0.1)

matrix_screen()
# works better in the terminal than Jupyer
# to copy multiple lines to terminal, need spaces on empty lines

# %%
