# Notes made during chapter 11 of Automate the Boring Stuff With Python
# 2025-11-29

# %% shell utilities module ---------------------------------------------------

import shutil

shutil.copy(src, dst)
shutil.move(src, dst)

# %% make directory -----------------------------------------------------------

from pathlib import Path
wd = Path.cwd()
(wd / 'new folder').mkdir()

# %% deletion -----------------------------------------------------------------

# permanent deletion - risky
import os
os.unlink(path)

shutil.rmtree(path)

# recylcing bin
import send2trash
send2trash.send2trash(path)

# %% folder contents ----------------------------------------------------------

# option 1 as list
os.listdir(wd)

# iterator
for item in wd.iterdir():
    print(item)

# option 2 from iterator
list(wd.iterdir())
# option 3 as string from iterator
[str(item) for item in wd.iterdir()]

# sub-folders and directories
list(os.walk(wd))

# %% zip files ----------------------------------------------------------------

import zipfile

# file to zip
with open('tmp.txt', 'w', encoding = 'utf-8') as file_obj:
    file_obj.write('msg\n' * 1000000)

# zip it up
with zipfile.ZipFile('test.zip', 'w') as example_zip:
    example_zip.write('tmp.txt', compress_type = zipfile.ZIP_DEFLATED)

# inspecting zip files
example_zip = zipfile.ZipFile('test.zip')
example_zip.namelist()
example_zip.getinfo('tmp.txt')
example_zip.close()

# upzip it
example_zip = zipfile.ZipFile('test.zip')
example_zip.extractall()
example_zip.close()

# %%
