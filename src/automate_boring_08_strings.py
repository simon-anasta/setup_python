# Notes made during chapter 8 of Automate the Boring Stuff With Python
# 2025-11-27

# %% Strings ------------------------------------------------------------------

# escape characters
msg = 'line1\nline2'
print(msg)
# raw strings do not convert escape characteres
# useful for file paths
msg = r'line3\nline4'
print(msg)
# multiline strings
msg = '''line5
line6'''
print(msg)

# %% Strings as lists ---------------------------------------------------------

msg = 'I have an amazing name'
'z' not in msg
'have' in msg
'Have' in msg

msg.startswith('I have')
msg.endswith('name')


# %% Formating strings --------------------------------------------------------

# f-strings work like glue::glue
clothing = 'hat'
style = 'feather'
f'I wear a {clothing} made of {style}'

# can compute within
f'I wear a {clothing * 2}'

# % wildcards
'I wear a %s made of %s' % (clothing, style)

# format
'I wear a {} made of {}'.format(clothing, style)

# %% capitalisation -----------------------------------------------------------

msg = 'Sir Fish'
msg.lower()
msg.upper()
msg.islower()
msg.isupper()

# checks
msg.isalpha() # letters only
msg.isalnum() # letters and numbers
msg.isdecimal() # only numbers (decimal point not accepted)

# %% Other manipulations ------------------------------------------------------

# join
'_'.join(['a', 'b', 'c'])

# split
'a_b_c__d'.split('_')

# add white space
'123'.ljust(10)
'123'.rjust(10, '.')

# remove white space
msg.strip()
msg.lstrip()
msg.rstrip()

# %% clipboard ----------------------------------------------------------------

# import pyerclip
# pyperclip.copy(msg)
# pyperclip.paste()

# %%
