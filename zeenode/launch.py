import os
from zeenode.load import load
from keep_alive import keep_alive

window = 'mode 90,19'
os.system(window)
keep_alive()
load()