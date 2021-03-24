from terminal_layout.extensions.choice import *
from terminal_layout import *

c = Choice('Which is the Best Programming Language?',
           ['Python', 'C/C++', 'Java', 'PHP', 'Go', 'JS', '...'],
           icon_style=StringStyle(fore=Fore.blue),
           selected_style=StringStyle(fore=Fore.blue),default_index=2)

choice = c.get_choice()
if choice:
    index, value = choice
    print(value, 'is the Best Programming Language')
