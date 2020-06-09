# terminal_layout

The project help you to quickly build layouts in terminal  
(这个一个命令行ui布局工具)

<img src="pic/demo.gif"  alt="demo.gif" width="400"/>

----------------

**基于terminal_layout的扩展**

* [progress](terminal_layout/extensions/progress/README.md)

![progress.gif](pic/progress.gif)

* [choice](terminal_layout/extensions/choice/README.md)

![choice.gif](pic/choice.gif)


-------------------

** video demo **

<a href="https://asciinema.org/a/226120">
<img src="https://asciinema.org/a/226120.svg"  alt="asciicast" width="550"/>
</a>

# link

* [Github](https://github.com/gojuukaze/terminal_layout) 
* [文档](https://terminal-layout.readthedocs.io) 
* [https://asciinema.org/a/226120](https://asciinema.org/a/226120) 

# 安装 
```bash
pip install terminal-layout
```

# 依赖
* Python 2.7, 3.5+ (maybe 3.4)
* Linux, OS X, and Windows systems.

# Usage

 * easy demo:

```python
import time
from terminal_layout import *

ctl = LayoutCtl.quick(TableLayout,
                      # table id: root
                      [
                          [TextView('t1', 'Hello World!', width=Width.fill, back=Back.blue)],  # <- row id: root_row_00,
                          [TextView('t2', '', fore=Fore.magenta)],  # <- row id: root_row_1,
                      ],
                      )

# or layout=ctl.get_layout()
layout = ctl.find_view_by_id('root')
layout.set_width(20)

# default: auto_re_draw=True
ctl.draw()

# 如果使用delay_set_text(), 必须把auto_re_draw设为True，否则你需要自己在线程中执行re_draw()
ctl.find_view_by_id('t2').delay_set_text('你好,世界!', delay=0.2)

time.sleep(0.5)
row3 = TableRow.quick_init('', [TextView('t3', 'こんにちは、世界!')])
layout.add_view(row3)

# 如果执行draw()时auto_re_draw=True，你必须执行stop()
ctl.stop()

```
![](pic/hello.png)

* use `re_draw()`

```python
import time
from terminal_layout import *

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('t1', 'Hello World!', width=Width.fill, back=Back.blue)],
                          [TextView('t2', '', fore=Fore.magenta)],
                      ],
                      )


layout = ctl.find_view_by_id('root')
layout.set_width(20)

ctl.draw(auto_re_draw=False)

ctl.find_view_by_id('t2').set_text('你好,世界!')
ctl.re_draw()

time.sleep(0.5)
row3 = TableRow.quick_init('', [TextView('t3', 'こんにちは、世界!')])
layout.add_view(row3)
ctl.re_draw()

# 不需执行stop()
# ctl.stop()
```

 * use python2 unicode

```python
# -*- coding: utf-8 -*-
from terminal_layout import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('', u'中文，你好', back=Back.cyan, width=Width.wrap)],
                          [TextView('', u'中文，你好', back=Back.cyan, width=6)],
                          [TextView('', u'日本語，こんにちは', back=Back.cyan, width=Width.wrap)],
                      ]

                      )

ctl.draw()

```

![](pic/py2.png)


## View的属性

 * fore & back
 
```python
TextView('','fore',fore=Fore.red)
TextView('','back',back=Back.red)
```

<img width="560" src="pic/color.jpeg"/>

 * style

```python
TextView('','style',style=Style.dim)
```

<img width="560" src="pic/style.jpeg"/>

 * width
 
```python
TextView('','width',width=10)
```

<img width="560" src="pic/width.jpeg"/>

 * weight
 
```python
TextView('','weight',weight=1)
```

<img width="560" src="pic/weight.jpeg"/>

 * gravity
 
```python
TextView('','gravity',gravity=Gravity.left)
```

<img width="560" src="pic/gravity.jpeg"/>

 * visibility
 
```python
TextView('','',visibility=Visibility.visible)
```

<img width="560" src="pic/visibility.jpeg"/>


 * ex_style (not support windows)


```python
TextView('','ex_style',style=Style.ex_blink)
```

<img width="560" src="pic/ex_style.jpeg"/>

 * ex_fore & ex_back (not support windows)


```python
TextView('','ex_fore',fore=Fore.ex_red_1)
TextView('','ex_back',back=Back.ex_red_1)

```

<img width="560" src="pic/ex_color.jpeg"/>

# LICENSE

[GPLv3](https://github.com/gojuukaze/terminal_layout/blob/master/LICENSE)

# Thanks

 * [colorama](https://github.com/tartley/colorama) : Simple cross-platform colored terminal text in Python
 * [colored](https://gitlab.com/dslackw/colored) : Very simple Python library for color and formatting in terminal
