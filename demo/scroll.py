import platform
from terminal_layout import *
from terminal_layout.extensions.scroll import *

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

title_style = {
    'back': Back.magenta if platform.system() == 'Windows' else Back.ex_plum_2,
    'width': Width.fill,
    'gravity': Gravity.center

}
rows = [[],
        [TextView('title', 'Hello, World!', **title_style)],
        [TextView('', ' ', **title_style)],
        ]

scroll_style = {
    'back': Back.blue if platform.system() == 'Windows' else Back.ex_sky_blue_2,
    'fore': Fore.black
}
for i, ss in enumerate(s.split('\n')):
    lan, code = ss.split(' - ')
    rows.append([
        TextView('', ' ' + str(i) + '.' + lan.title(), width=10, **scroll_style),
        TextView('', '| ' + code, width=Width.fill, **scroll_style)
    ])

ctl = LayoutCtl.quick(TableLayout, rows)
ctl.set_buffer_size(200)
ctl.enable_debug(height=12)

scroll = Scroll(ctl, stop_key='q', loop=True, more=True, scroll_box_start=3)
scroll.scroll()
