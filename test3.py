from codecs import getincrementaldecoder

import readchar
from colorama import init

from terminal_layout.logger import logger


from colorama import Fore, Back, Style
from colorama import Cursor
import getpass

print(Fore.RED + 'and in dim text' + Style.RESET_ALL)
print('input some:')
print('back to normal now')

import os
import sys
import termios


def press_any_key_exit(msg):
    # 获取标准输入的描述符
    fd = sys.stdin.fileno()

    # 获取标准输入(终端)的设置
    old_ttyinfo = termios.tcgetattr(fd)

    # 配置终端
    # new_ttyinfo = old_ttyinfo[:]

    # 使用非规范模式(索引3是c_lflag 也就是本地模式)
    # new_ttyinfo[3] &= ~termios.ICANON
    # # 关闭回显(输入不会被显示)
    # new_ttyinfo[3] &= ~termios.ECHO

    # 输出信息
    sys.stdout.write(msg)
    sys.stdout.flush()
    # 使设置生效
    # termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
    # 从终端读取
    i = 3
    msg = r''
    declass = getincrementaldecoder('utf-8')
    de = declass()

    while True:
        a = readchar.readkey()

       

        if a == readchar.key.ENTER:
            break
        if a==readchar.key.CTRL_C:
            raise 
        
        logger.info('%s,%s',msg,len(msg))
        back_num = len(msg)

        
        msg += a

        if back_num != 0:
            sys.stdout.write(Cursor.BACK(back_num))
        sys.stdout.write(msg)

        sys.stdout.flush()

    # 还原终端设置
    termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)

    sys.stdout.write(Cursor.DOWN(2) + Cursor.BACK(999999) + msg + '\n')
    sys.stdout.flush()


press_any_key_exit(Cursor.UP(2) + Cursor.FORWARD(11))


