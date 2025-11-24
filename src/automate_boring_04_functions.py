# Notes made during chapter 4 of Automate the Boring Stuff With Python
# 2025-11-23

# %% scope test ---------------------------------------------------------------

# values do not have to be defined at definition
def scope_test(num):
    return(value + num)

# value in parent environment will be used
value = 1
print(scope_test(2))

# current value in parent environment will be used
value = 3
print(scope_test(2))

# %% empty return -------------------------------------------------------------

def test_return(num):
    num

test = test_return(num = 1)
print(test)
print(type(test))

# default return type is `None`
# equialent to NULL in R

None == None # True
None == 1 # False
None == 0 # False
None == "" # False

# %% print variations ---------------------------------------------------------

print("dad", "mum", "son", "daughter")
print("dad", "mum", "son", "daughter", sep = ",")

family = ["dad", "mum", "son", "daughter"]
for ii in range(len(family)):
    print(family[ii], end = "")
for ii in range(len(family)):
    print(family[ii])

# %% error catching -----------------------------------------------------------

def error_test(num):
    try:
        print("trying calculation")
        10 / num
        print("calcualtion complete")
    except ZeroDivisionError: # must appear before catch-all
        print("can not divide by zero")
    except:
        print("some other error")
    else:
        print("no errors")
    finally:
        print("always do this")

error_test(4)
error_test("a")
error_test(0)

# %% Collatz sequence ---------------------------------------------------------

def next_collatz(num):
    """Calculate next number in Collatz sequence"""
    if num % 2 == 0:
        return(num // 2)
    if num % 2 == 1:
        return(3 * num + 1)
    else:
        ValueError

def collatz_sequence(num):
    """Calculate the Collatz sequence from input number to 1"""
    assert isinstance(num, int)
    assert num > 0
    assert num % 1 == 0

    print(num)
    steps = 0
    while num != 1:
        num = next_collatz(num)
        steps = steps + 1
        print(num)
    
    return(steps)

collatz_sequence(11)
collatz_sequence(120)

# %%
