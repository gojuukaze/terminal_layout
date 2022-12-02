"""

"""
from terminal_layout.helper.class_helper import instance_variables
from terminal_layout.view.params import OverflowVertical
from terminal_layout.view.layout import TableRow
from terminal_layout.view.text_view import TextView
from terminal_layout.readkey import Key, KeyListener
from terminal_layout.log import logger
from terminal_layout.helper.helper import get_terminal_size


class ScrollEvent:
    up = 'up'
    down = 'down'
    stop = 'stop'


class Scroll(object):
    """
    注意：直支持TableLayout ！！！
    """
    old_layout_overflow = None

    @instance_variables
    def __init__(self, ctl,
                 stop_key=Key.ESC, up_key=Key.UP, down_key=Key.DOWN,
                 scroll_start=0, current_index=0, loop=False,
                 btm_text='-- more --', callback=None, re_draw_after_scroll=True):
        """
        :param table: TableLayout
        :param overflow: hidden or scroll

        :param stop_key: 停止scroll的key
        :param up_key:
        :param down_key:
        :param scroll_start: 从哪行开始滚动，
        :param current_index: 当前显示的第一行。注意，这个表示的是终端中第一行对应的下标。
                              若终端有5行，layout有10行，把current_index设为8，则初始化时current_index会被设为5。
                              若终端有5行，当前current_index为5，调用down，如果loop=true，current_index会被置为0
                                                                            loop=false，current_index不会变
        :param loop: 循环
        :param btm_text: 底部的文本，类似于man的效果。为空则不显示
        :param callback: 滚动后的回调
        :param re_draw_after_scroll: 滚动后执行重绘。为false时你需要在callback中自己调用re_draw


        """
        pass

    def init_kl(self):
        self.kl = KeyListener()
        if self.stop_key:
            self.kl.bind_key(self.stop_key, self._stop, decorator=False)
        if self.up_key:
            self.kl.bind_key(self.up_key, self._up, decorator=False)
        if self.down_key:
            self.kl.bind_key(self.down_key, self._down, decorator=False)

    def start(self):
        # 1.初始化kl
        self.init_kl()
        # 2. 修改table的overflow
        table = self.ctl.get_layout()
        self.old_layout_overflow = table.get_overflow_vertical()
        table.set_overflow_vertical(OverflowVertical.none)
        # 3. 添加btm
        if self.btm_text:
            r=TableRow.quick_init('_scroll_btm_row_',TextView())
        
        self.ctl.draw(auto_re_draw=False)

    def _callback(self, event):
        if not self.callback:
            return
        self.callback(event)

    def _up(self, kl, event):
        self.up()

    def up(self):
        tmp = self.current_index-1
        if tmp < self.scroll_start:
            tmp = self.scroll_start if not self.loop else len(
                self.table.data)-1
        self.current_index = tmp
        self._callback(ScrollEvent.up)
        self.draw()

    def _down(self, kl, event):
        self.down()

    def down(self):
        tmp = self.current_index+1
        if tmp >= len(self.table.data):
            tmp = self.scroll_start if self.loop else len(self.table.data)-1
        self.current_index = tmp
        self._callback(ScrollEvent.down)

    def _stop(self, kl, event):
        self.stop()

    def stop(self):
        self.kl.stop()
        table = self.ctl.get_layout()
        table.set_overflow_vertical(self.old_layout_overflow)
        self._callback(ScrollEvent.stop)

    def update(self):
        _, h = self.ctl.get_terminal_size()

        # 注意，这里相当于 h = h-1-scroll_start，别理解错了
        # 最后一行需要显示光标，因此-1
        h -= 1+self.scroll_start

        if self.btm_text:
            h-=1

        show_start = self.current_index
        show_end = len(self.table.data)
