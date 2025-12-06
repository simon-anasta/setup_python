# Notes made during chapter 18 of Automate the Boring Stuff With Python
# 2025-12-04

# %% comma separated values ---------------------------------------------------

# open
import csv
example_file = open('example.csv')
example_reader = csv.reader(example_file)

# convert to list
example_data = list(example_reader)
example_data[row][column]

# OR iterate
for row in example_reader:
    msg = 'Row #' + str(example_reader.line_num) + ' ' + str(row)
    print(msg)

# close reading
example_file.close()

# writing
example_file = open('output.csv', 'w', newline = '')
example_writer = csv.writer(example_file)

example_writer.writerow(['list', 'of', 'elements'])

example_file.close()

# %% tab separated values -----------------------------------------------------

# as for csv but with different configuration
example_file = open('output.tsv', 'w', newline = '')
example_writer = csv.writer(example_file, delimiter='\t', lineterminator='\n\n')
# write
example_file.close()

# %% header rows in csv -------------------------------------------------------

# if the first row contains header information
# then DictReader is a better choice

example_file = open('example.csv')
example_reader = csv.DictReader(example_file)
example_data = list(example_reader)
# but now data is a list of dictionaries
# with dictionary names from the first row of the file
example_file.close()

# if column names are missing
# we can add them
example_file = open('example.csv')
example_reader = csv.DictReader(example_file, ['col1', 'col2', 'col3'])
# identical dictionary structure
example_file.close()

# when writing need to provide column names
example_file = open('example.csv', 'w', newline='')
example_writer = csv.DictWriter(example_file, ['col1', 'col2', 'col3'])
example_writer.writerow({'col1': 'value1', 'col2': 'value2', 'col3': 'value3'})
example_file.close()

# %% JSON ---------------------------------------------------------------------

import json
json_string = '{"name": "Alice Doe", "age": 30, "car": null, "programmer": true, "address": {"street": "100 Larkin St.", "city": "San Francisco", "zip": "94102"}, "phone": [{"type": "mobile", "number": "415-555-7890"}, {"type": "work", "number": "415-555-1234"}]}'

# convert to nested dictionaries and lists
data = json.loads(json_string)
# convert to string
string = json.dumps(data)
# convert to string with nice format
string = json.dumps(data, indent = 2)

# notes
# 
# uses null instead of None
# requires "double-quotes" instead of 'single-quotes'

# %% XML ----------------------------------------------------------------------
# look up if you ever need it
