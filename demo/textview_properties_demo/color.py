# -*- coding: utf-8 -*-
from terminal_layout import *

print('\ncolor support window, linux, osx\n')

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('', 'fore = black', width=30, fore=Fore.black),
                           TextView('', 'back = black', back=Back.black)],
                          [TextView('', 'fore = red', width=30, fore=Fore.red), TextView('', 'back = red', back=Back.red)],
                          [TextView('', 'fore = green', width=30, fore=Fore.green),
                           TextView('', 'back = green', back=Back.green)],
                          [TextView('', 'fore = yellow', width=30, fore=Fore.yellow),
                           TextView('', 'back = yellow', back=Back.yellow)],
                          [TextView('', 'fore = blue', width=30, fore=Fore.blue), TextView('', 'back = blue', back=Back.blue)],
                          [TextView('', 'fore = magenta', width=30, fore=Fore.magenta),
                           TextView('', 'back = magenta', back=Back.magenta)],
                          [TextView('', 'fore = cyan', width=30, fore=Fore.cyan), TextView('', 'back = cyan', back=Back.cyan)],
                          [TextView('', 'fore = white', width=30, fore=Fore.white),
                           TextView('', 'back = white', back=Back.white)],
                          [TextView('', 'fore = lightblack', width=30, fore=Fore.lightblack),
                           TextView('', 'back = lightblack', back=Back.lightblack)],
                          [TextView('', 'fore = lightred', width=30, fore=Fore.lightred),
                           TextView('', 'back = lightred', back=Back.lightred)],
                          [TextView('', 'fore = lightgreen', width=30, fore=Fore.lightgreen),
                           TextView('', 'back = lightgreen', back=Back.lightgreen)],
                          [TextView('', 'fore = lightyellow', width=30, fore=Fore.lightyellow),
                           TextView('', 'back = lightyellow', back=Back.lightyellow)],
                          [TextView('', 'fore = lightblue', width=30, fore=Fore.lightblue),
                           TextView('', 'back = lightblue', back=Back.lightblue)],
                          [TextView('', 'fore = lightmagenta', width=30, fore=Fore.lightmagenta),
                           TextView('', 'back = lightmagenta', back=Back.lightmagenta)],
                          [TextView('', 'fore = lightcyan', width=30, fore=Fore.lightcyan),
                           TextView('', 'back = lightcyan', back=Back.lightcyan)],
                          [TextView('', 'fore = lightwhite', width=30, fore=Fore.lightwhite),
                           TextView('', 'back = lightwhite', back=Back.lightwhite)]
                      ])

ctl.draw(auto_re_draw=False)


