# scroll
让 `TableLayout` 支持滚动

![choice.gif](../../../pic/choice.gif)


## usage

* **必须配合`TableLayout`和`TableRow`使用!!**

```python
from terminal_layout import *
from terminal_layout.extensions.scroll import *

rows=[ [TextView(str(i),str(i))] for i in range(50)]

ctl = LayoutCtl.quick(TableLayout, rows)
# ctl.enable_debug(height=13)
scroll = Scroll(ctl, stop_key='q', loop=True, more=True, scroll_box_start=3)
scroll.scroll()

```

There are several parameter you can set:

| **name**             | **default** | **desc**                              |
|----------------------|-------------|---------------------------------------|
| ctl                  |             | LayoutCtl                             |
| stop_key             | Key.ESC     | 停止滚动的key                              |
| up_key               | Key.UP      |                                       |
| down_key             | Key.DOWN    |                                       |
| scroll_box_start     | 0           | 从哪行开始可以滚动。若第一行要显示标题，可设置scroll_start=1 |
| default_scroll_start | 0           | 初始化时滚动区域第一行下标                         |
| loop                 | False       |                                       |
| btm_text             | ''          | 底部的文本，为空则不显示                          |
| more                 | False       | 类似于man的效果。为Ture会自动添加 btm_text         |
| callback             | None        | 滚动后的回调                                |
| re_draw_after_scroll | True        | 滚动后执行重绘。为false时你需要自己调用re_draw         |

### callback

callback在 draw 之后调用

```python
from terminal_layout.extensions.scroll import *

def my_callback(event):
    if event== ScrollEvent.up:
        pass
    # ...
```

### scroll_box

scroll_box 可以理解为可滚动的区域