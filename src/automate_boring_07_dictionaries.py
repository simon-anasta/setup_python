# Notes made during chapter 7 of Automate the Boring Stuff With Python
# 2025-11-25

# %% Dictionary ---------------------------------------------------------------

# list []
# tuple ()
# dictionary {}

# key value pairs:
my_dict = {
    "k1": "v1",
    "k2": "v2"
}

my_dict["k1"]

# fetching keys or values
my_dict.values()
my_dict.keys()
# fetching pairs
my_dict.items()

# as a list
list(my_dict.keys())

for key in my_dict.keys():
    print(my_dict[key])

for key, value in my_dict.items():
    print(value, key)

# %% Existing values ----------------------------------------------------------

'k3' in my_dict.keys()

# set value if does not exist
if 'k3' not in my_dict.keys():
    my_dict['k3'] = 'v3'
# equivalent
my_dict.setdefault('k3','v3')

# fetch non-existant will error
my_dict['k4']

# fetch if exists
if 'k4' in my_dict.keys():
    print(my_dict['k4'])
else:
    print('v4')
# equivalent
my_dict.get('k4','v4')

# %% Reversing a dictionary ---------------------------------------------------

keys = [1,2,3,4,5,6,7]
values = ['a','b','c','d','e','f','g']

my_dict = {}

for ii in range(len(keys)):
    my_dict[keys[ii]] = values[ii]

alt_dict = {}

for key, value in my_dict.items():
    alt_dict[value] = key

# more compare
{keys[ii]: values[ii] for ii in range(len(keys))}
# compact reverse
{value: key for key, value in my_dict.items()}

# %% mofifying a dictionary ---------------------------------------------------

def modify_dict(current, addition):
    assert isinstance(current, dict)
    assert isinstance(addition, dict)

    for item in addition.keys():
        current[item] = current.get(item, 0) + addition[item]

    return(current)

current = {'a': 10, 'b': 2}
addition = {'a': 2, 'c': 1}

out = modify_dict(current, addition)
print(out)

# %%
