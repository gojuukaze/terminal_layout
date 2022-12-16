# scroll
让 `TableLayout` 支持滚动

![choice.gif](../../../pic/choice.gif)


### usage

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

| name            | default                         | desc               |
|-----------------|---------------------------------|--------------------|
