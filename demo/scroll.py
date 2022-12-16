from terminal_layout import *
from terminal_layout.extensions.scroll import *
import time
import sys


s = '''python2 - print "Hello, World!"
python3 - print("Hello, World!")
c - printf("Hello, World!")
c++ - cout << "Hello, World!" << endl
java - System.out.println("Hello, World!")
JS - console.log('Hello, World!');
php - echo "Hello, World!"
c# - Console.WriteLine("Hello, World!")
shell - echo "Hello, World!"
go - fmt.Println("Hello, World!")
rust - println("Hello, World!")'''


color = [Back.blue, Back.red, Back.magenta,
         Back.cyan, Back.green, Back.yellow, ]

title_style = {
    'back': Back.magenta,
    'width': Width.fill,
    'gravity': Gravity.center

}
rows = [[],
        [TextView('title', 'Hello, World!', **title_style)],
        [TextView('', ' ', **title_style)],
        ]

scroll_style = {
    'back': Back.blue,
    'fore': Fore.black
}
for i, ss in enumerate(s.split('\n')):
    lan, code = ss.split(' - ')
    rows.append([
        TextView('', ' '+str(i)+'.'+lan.title(), width=10, **scroll_style),
        TextView('', '| '+code, width=Width.fill, **scroll_style)
    ])


ctl = LayoutCtl.quick(TableLayout, rows)
ctl.enable_debug(height=13)

scroll = Scroll(ctl, stop_key='q', loop=True, more=True, scroll_box_start=3)
scroll.scroll()
