# choice
Shows a list of choices, and allows the selection of one of them.


![choice.gif](../../../pic/choice.gif)


### usage

```python
from terminal_layout.extensions.choice import *
from terminal_layout import *

c = Choice('Which is the Best Programming Language? (press <esc> to exit) ',
           ['Python', 'C/C++', 'Java', 'PHP', 'Go', 'JS', '...'],
           icon_style=StringStyle(fore=Fore.blue),
           selected_style=StringStyle(fore=Fore.blue))

choice = c.get_choice()
if choice:
    index, value = choice
    print(value, 'is the Best Programming Language')
```

There are several parameter you can set:

| name            | default                         | desc               |
|-----------------|---------------------------------|--------------------|
| title           |                                 | title              |
| choices         |                                 | a list of choices  |
| icon            | '> '                            | delimiter list     |
| icon\_style     | StringStyle\(fore=Fore\.green\) | icon style         |
| choices\_style  | StringStyle\(\)                 | choices style      |
| selected\_style | StringStyle\(\)                 | selected style     |
| loop            | True                            | loop               |
| default_index   | 0                               | default icon index |
| stop_key        | ['q']                           | stop key           |