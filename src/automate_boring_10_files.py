# Notes made during chapter 10 of Automate the Boring Stuff With Python
# 2025-11-29

# %%  Path basics -------------------------------------------------------------

import os
from pathlib import Path

# makes a path object (WindowsPath on Windows)
Path('C:','User', 'Documents')

# combine two separeate paths
Path('C:') / Path('User')

# working directory
initial_wd = Path.cwd()
os.chdir("..")
Path.cwd()
os.chdir(initial_wd)
Path.cwd()

# %% Path additions -----------------------------------------------------------

# home path
Path.home()

# check if absolute path
Path("subfolder").is_absolute()
# convert to absolute path
Path("subfolder").absolute()

# %% Decomposing paths --------------------------------------------------------

pp = Path('C:/User/Documents/my_file.txt')

# drive
pp.anchor
# folder
pp.parent
pp.parents[0] # equivalent

pp.parent.parent
pp.parents[1] # equivalent

# file
pp.name
pp.stem
pp.suffix
# split
pp.parts

# %% file details -------------------------------------------------------------

pp = Path('D:/Python Projects/setup_python/src/automate_boring_01_basics.py')
# check existance
pp.exists()

# fetch file details
file_stats = pp.stat()

file_stats.st_size # file sie in bytes
file_stats.st_mtime # modified time
file_stats.st_ctime # creation time
file_stats.st_atime # last accessed time

# convert times to local time
import time

time.asctime(time.localtime(file_stats.st_mtime))

# %% Globs: simple regex with only ? and * ------------------------------------

pp = Path.cwd()

# glob is needed for locating contents of folders

# all contents
list(pp.glob('*'))
# only files starting with .
list(pp.glob('.*'))

for ff in pp.glob('*'):
    if ff.is_file():
        print('File: ' + ff.name)
    if ff.is_dir():
        print('Folder: ' + ff.name)

# %% read and write plain text files ------------------------------------------

pp = Path.cwd()
ff = Path('tmp.txt')

# simplest approach
ff.write_text('test message')
ff.read_text()
ff.unlink()

# more options

# writing
ffile = open(ff, 'w', encoding = 'UTF-8')
ffile.write('line1\n')
ffile.write('line2start ')
ffile.write('line2end\n')
ffile.write('line3\nline4\n')
ffile.close()

# appending
ffile = open(ff, 'a', encoding = 'UTF-8')
ffile.write('line 5\nline 6\n')
ffile.close()

# reading from files
ffile = open(ff, 'r')
all_contents = ffile.read()
ffile.close()

ffile = open(ff, 'r')
itemised_contents = ffile.readlines()
ffile.close()

# read single line
ffile = open(ff, 'r')
current_line = ffile.readline()
current_line = ffile.readline() # returns '' at end of file
ffile.close()

# %% context management using with --------------------------------------------
# removes the need to call 'close'

with open(ff, 'r') as ffile:
    all_lines = ffile.readlines()

# delete file
ff.unlink()

# %% shelve for saving Python contents ----------------------------------------

import shelve

# write
shelve_file = shelve.open('tmp_py_vars')
shelve_file['colours'] = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
shelve_file['sizes'] = {'small': 10, 'medium': 50, 'large': 200}
shelve_file.close()
# supports appending, treat as dictionary

# read
shelve_file = shelve.open('tmp_py_vars')
# fetch keys
list(shelve_file.keys())
# convert to dictionary
dict(shelve_file)

colours = shelve_file['colours']
sizes = shelve_file['sizes']

shelve_file.close()

# delete file
Path('tmp_py_vars').unlink()

# %%
