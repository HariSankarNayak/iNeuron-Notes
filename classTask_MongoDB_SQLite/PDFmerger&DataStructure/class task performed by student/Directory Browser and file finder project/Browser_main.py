'''
This is the main program which calls the start1 function to build Browser and File finder
Menu and operations
'''
from Browser_start import start1
from Browser_logger import *
writelogs('Browser_main','info','main program started')
try:
    start1()
except Exception as e:
    writelogs('Browser_main', 'error', 'Some error occurred while calling start1')
    writelogs('Browser_main','exception','e')
else:
    writelogs('Browser_main','info','The Browser and File finder worked successfully')
