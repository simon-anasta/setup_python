# Notes made during chapter 9 of Automate the Boring Stuff With Python
# 2025-11-29

# %% Four steps for regular expressions ---------------------------------------

# 1: import
import re
# 2: compile to get a pattern object
phone_number_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# 3: search to get a match
matches = phone_number_pattern.search('My number is 123-456-7890')
# 4: group to get the matched text
found = matches.group()

print(found)

# no match
matches = phone_number_pattern.search('This string contains no phone number')
matches == None # True

# %% Groups -------------------------------------------------------------------

# brackets within pattern are captured separately
phone_number_pattern = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matches = phone_number_pattern.search('My number is 123-456-7890')

# retrieve just part of match
print(matches.group(1))
print(matches.group(2))

# retried whole match
print(matches.group())
print(matches.group(0))

# retrieve whole match as tuple
print(matches.groups())

# %% search vs findall --------------------------------------------------------

re_pattern = re.compile(r'\d\d')

# search finds first match
print(re_pattern.search('abc1234').group())
# findall finds all matches (non-overlapping)
print(re_pattern.findall('abc1234'))


# %% Regex flags --------------------------------------------------------------

# include new lines within dot
re_pattern = re.compile(r'.*', re.DOTALL)
# case insensitive
re_pattern = re.compile(r'.*', re.I)
re_pattern = re.compile(r'.*', re.IGNORECASE)

# combine with pipe
re_pattern = re.compile(r'.*', re.IGNORECASE | re.DOTALL)

# %% Substitution -------------------------------------------------------------

import re
num_pattern = re.compile('[0-9]')
num_pattern.sub('__', 'Any number, like 4, will become 2 underscores')

# with group capturing
num_pattern = re.compile('([0-9])')
num_pattern.sub('_\\1_', 'Any number, like 4, will gain 1 underscore on each side')

# %% Human readable -----------------------------------------------------------

from humre import * # so we don't have to put 'humre.' in front of everything

# human readable (but verbose) to regex
raw_pattern = group(
    optional_group(either(
            exactly(3, DIGIT), # Area code
            OPEN_PAREN + exactly(3, DIGIT) + CLOSE_PAREN
    )),
    optional(group_either(WHITESPACE, '-', PERIOD)), # Separator
    group(exactly(3, DIGIT)), # First three digits
    group_either(WHITESPACE, '-', PERIOD), # Separator
    group(exactly(4, DIGIT)), # Last four digits
    optional_group( # Extension
        zero_or_more(WHITESPACE),
        group_either('ext', 'x', r'ext\.'),
        zero_or_more(WHITESPACE),
        group(between(2, 5, DIGIT))
    )
)

pattern = re.compile(raw_pattern)

# regex to human readable
parse(r'\d{3}-\d{3}-\d{4}')
# not working, always returns None, even on author-supplied strings

# %%
