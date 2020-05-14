import sys
import readchar

from terminal_layout.logger import logger

from colorama import Fore, Back, Style
from colorama import Cursor

sys.stdout.write(Fore.RED + 'and in dim text\n' + Style.RESET_ALL)
sys.stdout.flush()
sys.stdout.write('input some:\n')
sys.stdout.flush()
sys.stdout.write('back to normal now\n')
sys.stdout.flush()
sys.stdout.write(Cursor.UP(2) + Cursor.FORWARD(11))
sys.stdout.flush()
msg = ''


while True:
    a = readchar.readkey()
    logger.info('%s,%s', repr(a), len(a))


    if a == readchar.key.ENTER:
        break
    if a == readchar.key.CTRL_C:
        break
    if a==readchar.key.BACKSPACE:
        back_num = len(msg)
        msg=msg[:-1]
    if a==readchar.key.LEFT:
        sys.stdout.write(Cursor.BACK(1))

        sys.stdout.flush()
        msg += a
        continue
    else:
        back_num = len(msg)
        msg+=a


    if back_num != 0:
        sys.stdout.write(Cursor.BACK(9999)+Cursor.FORWARD(11)+' '*back_num+Cursor.BACK(back_num))
    sys.stdout.write(msg)
    
    sys.stdout.flush()

sys.stdout.write(Cursor.DOWN(2) + Cursor.BACK(999999) + msg + '\n')
sys.stdout.flush()
print(str(msg)=='as1')