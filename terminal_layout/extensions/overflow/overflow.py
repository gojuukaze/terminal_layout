"""
这个集成到table里还是单独作为一个插件？？

之前考虑过把hidden放到table里并作为默认的行为，scroll单独作为一个插件。
但后续修改代码时发现由于Overflow相关行为会在draw时修改view的属性，并在draw结束后把属性还原，
当启动auto_re_draw时这会和用户自己的修改行为冲突，这就必须加锁，增加了不必要的麻烦。

因此为了减少代码复杂度，把Overflow单独作为一个插件，并且插件建议关闭auto_re_draw
"""
from terminal_layout.helper.class_helper import instance_variables
from terminal_layout.view.params import Visibility
from terminal_layout.view.base import View
from terminal_layout.readkey import Key, KeyListener
from terminal_layout.log import logger
from terminal_layout.helper.helper import get_terminal_size



class OverflowType:
    hidden = 'hidden'
    scroll = 'scroll'


class ScrollEvent:
    up = 'up'
    down = 'down'
    stop = 'stop'


class Hidden(object):
    def hidden(self):
        _, h = get_terminal_size()
        # 最后一行需要显示光标，因此-1
        h -= 1
        self.old_row_visibility = []
        for r in self.table.data:
            self.old_row_visibility.append(r.visibility)
            if h > 0:
                if not r.visibility == Visibility.gone:
                    h -= 1
            else:
                r.visibility = Visibility.gone


class Scroll(object):

    def init_scroll(self):
        self.kl = KeyListener()
        if self.stop_key:
            self.kl.bind_key(self.stop_key, self._stop, decorator=False)
        if self.up_key:
            self.kl.bind_key(self.up_key, self._up, decorator=False)
        if self.down_key:
            self.kl.bind_key(self.down_key, self._down, decorator=False)

    def _callback(self, event):
        if not self.callbakc:
            return
        self.callback(event)

    def _up(self, kl, event):
        self.up()

    def up(self):
        tmp=self.current_index-1
        if tmp<self.scroll_start:
            tmp=self.scroll_start if not self.loop else len(self.table.data)-1
        self.current_index=tmp
        self._callback(ScrollEvent.up)

    def _down(self, kl, event):
        self.down()

    def down(self):
        self._callback(ScrollEvent.down)

    def _stop(self, kl, event):
        self.stop()

    def stop(self):
        self.kl.stop()
        self._callback(ScrollEvent.stop)
    
    def scroll(self):
        _,h=get_terminal_size()
        # 注意，这里相当于 h=h-1-scroll_start，别理解错了
        # 最后一行需要显示光标，因此-1
        h-=1+self.scroll_start

        show_start = self.current_index
        show_end = len(self.table.data)
        



class OverflowVertical(View, Hidden, Scroll):
    """
    垂直方向的Overflow
    """
    old_row_visibility = None

    @instance_variables
    def __init__(self, table, overflow=OverflowType.hidden,
                 # 下面参数type为scroll时才有效
                 stop_key=Key.ESC, up_key=Key.UP, down_key=Key.DOWN,
                 scroll_start=0, current_index=0, loop=False,
                 btm_text='-- more --', callback=None):
        """
        :param table: TableLayout
        :param overflow: hidden or scroll

        :param stop_key: 停止scroll的key
        :param up_key: hidden or scroll
        :param down_key: TableLayout
        :param scroll_start: 从哪行开始滚动，
        :param table: TableLayout
        :param overflow: hidden or scroll
        :param table: TableLayout
        :param overflow: hidden or scroll
        其他参数说明见Scroll类

        """
        if overflow == OverflowType.scroll:
            self.init_scroll()

    def before_draw(self):
        if self.overflow == OverflowType.hidden:
            self.hidden()
        else:
            self.scroll()

    def draw(self):
        self.before_draw()
        self.table.draw()
        self.after_draw()

    def after_draw(self):
        for i, r in enumerate(self.table.data):
            r.visibility = self.old_row_visibility[i]

    def clear(self):
        return self.table.clear()

    def update_width(self, parent_width):
        return self.table.update_width(parent_width)

    def find_view_by_id(self, id):
        return self.table.find_view_by_id(id)

    def get_width(self):

        return self.table.get_width()

    def get_real_width(self):

        return self.table.get_real_width()

    def __getitem__(self, item):

        return self.table.data[item]

    def insert(self, index, view):
        return self.table.insert(index, view)
