# Notes made during chapter 5 of Automate the Boring Stuff With Python
# 2025-11-24

# %% Exceptions ---------------------------------------------------------------

raise Exception("test")

qq = Exception("test")
raise qq

raise Warning("test warning")


# %% Assert -------------------------------------------------------------------

assert True
assert False
assert False, "message"


# %% Logging ------------------------------------------------------------------

import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s'
    )

logging.debug("message")

# does not work within interactive Juypter
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(message)s',
    filename = 'D:/Python Projects/testLog.txt'
    )

logging.debug("message")
logging.debug("message")


# %%
