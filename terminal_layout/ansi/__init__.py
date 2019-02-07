
from terminal_layout.ansi.fore import Fore as _Fore
from terminal_layout.ansi.back import Back as _Back
from terminal_layout.ansi.style import Style as _Style
from colorama import Cursor as _Cursor
from colorama import init as _init
from colorama.ansi import clear_line as _clear_line
from colorama.ansi import clear_screen as _clear_screen

Fore = _Fore
Back = _Back
Style = _Style
Cursor = _Cursor

term_init = _init
clear_line = _clear_line
clear_screen = _clear_screen
