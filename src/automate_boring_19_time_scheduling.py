# Notes made during chapter 19 of Automate the Boring Stuff With Python
# 2025-12-07

# %% time basics --------------------------------------------------------------

import time

# time since Unix epoch
time.time()
# readable time
time.ctime()
# time components
time.localtime()

# elapsed time
start_time = time.time()
time.sleep(2)
end_time = time. time()
elapsed_time = end_time - start_time

# %% datatime for easier manipulation -----------------------------------------

import datetime
datetime.datetime.now()

# unpacking
dt = datetime.datetime.now()
dt.year, dt.month, dt.day

# craeting datetimes
year_start = datetime.datetime(2025, 1, 1, 0, 0, 0)
year_end = datetime.datetime(2025, 12, 31, 23, 59, 59)
year_start < year_end
elapsed_time = year_end - year_start

# adding time
one_day =datetime.timedelta(days=1)
tomorrow = datetime.datetime.now().date() + one_day

# does not work
today = datetime.datetime.now().date()
tomorrow = today
tomorrow.day = tomorrow.day + 1 # not writable

# does work
today = datetime.datetime.now().date()
tomorrow = datetime.date(today.year, today.month, today.day + 1)

# %% waiting ------------------------------------------------------------------

target_time = datetime.datetime(tomorrow)

while datetime.datetime.now() < tomorrow:
    time.sleep(1)
print("it is a new day")
# use sleep to reduce CPU demand

# %% printing our dates and times ---------------------------------------------

# prefered printing YYYY-MM-DD
str(tomorrow)
# YYYY-MM-DD HH:MM:SS.sss
str(datetime.datetime.now())

# format control
now = datetime.datetime.now()
now.strftime('%Y-%m-%d') # YYYY-MM-DD
now.strftime('%H:%M:%S') # HH:MM:SS

# %% text to dates ------------------------------------------------------------

datetime.datetime.strptime('2025/12/07', '%Y/%m/%d')

# %% running another process --------------------------------------------------

import subprocess

# wait for launched application to complete/close
subprocess.run(['C:/Windows/System32/calc.exe'])

# open launched application and continue
subprocess.Popen(['C:/Windows/System32/calc.exe'])

# monitor current state
open_calc = subprocess.Popen(['C:/Windows/System32/calc.exe'])
open_calc.poll() == None # still running
open_calc.wait() # do nothing until process closes
open_calc.poll()

# or kill it
open_calc.kill()

# Jupyter returns once subprocess is open
# not once closed

# passing command line arguments
subprocess.run(['C:/Windows/Notepad.exe', __file__])
# this idea can be used to open files with default application

# %% receive output from subprocesses -----------------------------------------

proc = subprocess.run(['ping', '-n', '4', 'nostarch.com'], capture_output=True, text=True)
print(proc.stdout)
# need both capture_output and text
# result is in stdout

# %%
