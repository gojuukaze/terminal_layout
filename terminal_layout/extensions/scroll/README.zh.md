# scroll

让 `TableLayout` 支持滚动。

注意：**必须配合`TableLayout`和`TableRow`使用!!**

![scroll.gif](../../../pic/scroll.gif)

## usage

```python
from terminal_layout import *
from terminal_layout.extensions.scroll import *

rows = [[TextView(str(i), str(i))] for i in range(50)]

ctl = LayoutCtl.quick(TableLayout, rows)
# ctl.enable_debug(height=13)
scroll = Scroll(ctl, stop_key='q', loop=True, more=True, scroll_box_start=3)
scroll.scroll()

```

There are several parameter you can set:

| **name**             | **default** | **desc**                                                         |
|----------------------|-------------|------------------------------------------------------------------|
| ctl                  |             | LayoutCtl                                                        |
| stop_key             | Key.ESC     | 停止滚动的key                                                         |
| up_key               | Key.UP      |                                                                  |
| down_key             | Key.DOWN    |                                                                  |
| scroll_box_start     | 0           | 从哪行开始可以滚动。若第一行要显示标题，可设置scroll_box_start=1 （详细说明见最后的cal_scroll部分） |
| default_scroll_start | 0           | 初始化时, scroll_box中哪行显示在第一的位置                                      |
| loop                 | False       |                                                                  |
| btm_text             | ''          | 底部的文本，为空则不显示                                                     |
| more                 | False       | 类似于man的效果。为Ture会自动添加 btm_text                                    |
| callback             | None        | 滚动后的回调                                                           |
| re_draw_after_scroll | True        | 滚动后是否执行重绘。为false时你需要自己调用re_draw                                  |
| re_draw_after_stop   | False       | 停止滚动后是否重绘                                                        |


> default_scroll_start 说明  
> 若terminal高度为4, table有6行（即高度为6），default_scroll_start=6。  
> 绘制时，显示在terminal顶部的是row_2。
> ```
>   row_0
>   row_1
> |------------|
> | row_2      |
> | row_3      |  <=== terminal, h=4
> | row_4      |
> | row_5      |
> |------------|
> ```
  
  
## 修改滚动事件行为

有多种方法可以修改滚动后的行为

### 1. 通过callback

```python
from terminal_layout.extensions.scroll import *

ctl = ...
scroll = ...


def my_callback(event):
    if event == ScrollEvent.up:
        ...
        # or ctl.re_draw()
        scroll.draw()
    # ...

```

`up`, `down` 事件默认会在调用callback之前进行`re_draw`。如果你callback中对view进行了修改，则需要调用函数重绘。

如果你callback中改变了table的行数，你应该使用 `scroll.draw()` 这个函数会重新计算scroll位置

### 2. 重写滚动事件

如果你想在计算scroll位置之前进行一些操作（比如：禁止向上循环，但允许向下循环），
就需要重写滚动事件。

有多种方法可以重写滚动事件

* 通过 `stop_func`, `up_func`, `down_func`

  ```python
  from terminal_layout.extensions.scroll import *
  
  ctl = LayoutCtl(...)
  scroll = Scroll(ctl, loop=True)
  
  def up(kl, event):
    if scroll.current_scroll_start - 1 < scroll.scroll_box_start:
        return 
    scroll.up()
    ctl.re_draw()
  
  scroll.scroll(up_func=up)
  ```

* 添加`key_listener`事件

  ```python
  from terminal_layout.extensions.scroll import *
  from terminal_layout.readkey import Key
  
  ctl = LayoutCtl(...)
  scroll = Scroll(ctl, up_key=None, loop=True)
  
  key_listener = scroll.init_kl()
  
  @key_listener.bind_key(Key.UP)
  def up(kl, event):
    if scroll.current_scroll_start - 1 < scroll.scroll_box_start:
        return 
    scroll.up()
    ctl.re_draw()
  
  scroll.draw()
  key_listener.listen()
  ```
  或者不通过`init_kl`自己初始化`KeyListener`

  ```python
  from terminal_layout.extensions.scroll import *
  from terminal_layout.readkey import Key, KeyListener
  
  ctl = LayoutCtl(...)
  scroll = Scroll(ctl, loop=True)
  
  key_listener = KeyListener()
  
  @key_listener.bind_key(Key.UP)
  def up(kl, event):
    ...

  key_listener.bind_key(Key.DOWN, down_func , decorator=False)
  key_listener.bind_key('q', stop_func , decorator=False)
  
  scroll.draw()
  key_listener.listen()

  ```
  
## cal_scroll 返回值说明

* `scroll_box_start` : 可滚动区域开始位置。一般用于要一直显示标题的情况
* `scroll_box_end` : 可滚动区域结束位置 
* `scroll_start` : 滚动区域实际显示的开始位置
* `scroll_end` : 滚动区域实际显示的结束位置

![cal_scroll.png](../../../pic/cal_scroll.png)
