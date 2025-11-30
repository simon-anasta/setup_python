# Notes made during chapter 12 of Automate the Boring Stuff With Python
# 2025-11-30

# %% bash and powershell commands ---------------------------------------------
# on windows

# list PATH (bash)
echo %PATH%
# list path (powershell)
$env:path
# one line per item
$env:path.split(';')

# locate folder in PATH with contents (bash)
where git
# locate on PATH (powershell)
Get-Command git

# %% fetching info about the current script -----------------------------------

# the executing files location
from pathlib import Path
Path(__file__)
# does not work interactive

# Python
import sys
# location of Python
sys.executable
# version information
sys.version
sys.version_info.major
sys.version_info.minor

# operating system
import os
# os type (nt = windows, posit = macOS or Linux)
os.name
# win32 = windows, darwin = macOS, linux = Linux
sys.platform

# platform module can fetch hardware information
# package = collection of code
# module = individual .py file

# %% receiving input frm the command line -------------------------------------

# we can run scripts
uv run python file.py

# additional arguments
uv run python file.py hello world
# everything after 'python' goes into sys.argv
sys.argv
# ['file.py', 'hello', 'world']

# spaces are separators, use double quotes to group
uv run python file.py "hello world"
sys.argv
# ['file.py', 'hello world']

# argparse module is designed for handling complex inputs

# %% accessing the clipboard --------------------------------------------------

import pyperclip
# fetch from clipboard
pyperclip.paste()
# send to clipboard
pyperclip.copy('message')

# paste returns empty text if the thing copied is not text

# %% clear terminal -----------------------------------------------------------

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# this if-else pattern is not recommended

# %% Message boxes ------------------------------------------------------------

import pymsgbox

pymsgbox.alert('display msg until ok clicked')
pymsgbox.confirm('require user to click OK or cancel')
pymsgbox.prompt('fetch text')
pymsgbox.password('fetch text with characters concealed')

# %% .bat file contents to run a script ---------------------------------------

# this is best saved in yourScript.bat
@call %HOMEDRIVE%%HOMEPATH%\Scripts\.venv\Scripts\activate.bat
@python %HOMEDRIVE%%HOMEPATH%\Scripts\yourScript.py %*
@pause # only needed if there is text to review
@deactivate

# if the script foler is on the PATH
# then you can call yourScript.bat direct from CMD
# the .bat is optional on Windows
# so you could run it just be calling yourScript

# %% Compile programs with PyInstaller

# instructions on pg 285

# from bash
python -m PyInstaller --onefile yourScript.py








