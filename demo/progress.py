import time
from terminal_layout.extensions.progress import *

with Progress('Downloading', 10) as p:
    for i in range(10):
        if p.is_finished():
            break
        time.sleep(0.3)
        p.add_progress(i)

with Progress('Downloading', 10, reached='▓', unreached='░', suffix_style=SuffixStyle.fraction) as p:
    for i in range(10):
        if p.is_finished():
            break
        time.sleep(0.3)
        p.add_progress(i)
print('')
with Loading('Loading', 10) as l:
    for i in range(10):
        if l.is_finished():
            break
        time.sleep(0.3)
        l.add_progress(i)

with Loading('Loading', 10, infix=InfixChoices.style10, delimiter=[' ', ' | '], suffix_style=SuffixStyle.fraction) as l:
    for i in range(10):
        if l.is_finished():
            break
        time.sleep(0.3)
        l.add_progress(i)
