from colorama import init
import sys

from colorama.ansi import clear_line

from terminal_layout.logger import logger
from terminal_layout.readkey import readkey
from terminal_layout.readkey.key import Key

init()

from colorama import Fore, Back, Style
from colorama import Cursor

sys.stdout.write(Fore.RED + 'and in dim text' + Style.RESET_ALL + '\n')
sys.stdout.flush()
sys.stdout.write('\n')
sys.stdout.flush()
sys.stdout.write('back to normal now' + '\n')
sys.stdout.flush()
sys.stdout.write(Cursor.UP(2) + 'input som:')
sys.stdout.flush()

s = ''

while True:
    back_num = len(s)
    a = readkey()
    if a == Key.ENTER:
        break
    if a==Key.BACKSPACE:
        s=s[:-1]
    else:
        s+=a
    
    sys.stdout.write(clear_line()+ Cursor.BACK(99999)+'input some:'+s+Style.RESET_ALL)
    sys.stdout.flush()

sys.stdout.write(Cursor.DOWN(2) + Cursor.BACK(99999) + s + '\n')
sys.stdout.flush()
