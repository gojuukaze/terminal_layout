"""

"""
from terminal_layout.helper.class_helper import instance_variables
from terminal_layout.view.params import OverflowVertical, Visibility
from terminal_layout.view.layout import TableRow
from terminal_layout.view.text_view import TextView
from terminal_layout.readkey import Key, KeyListener
from terminal_layout.log import logger
from terminal_layout.helper.helper import get_terminal_size


class ScrollEvent:
    up = 'up'
    down = 'down'
    stop = 'stop'


scroll_btm_row = '_scroll_btm_row_'
scroll_btm_text = '_scroll_btm_text_'


class Scroll(object):
    """
    注意：只支持TableLayout ！！！
    """
    old_layout_overflow = None

    @instance_variables
    def __init__(self, ctl,
                 stop_key=Key.ESC, up_key=Key.UP, down_key=Key.DOWN,
                 scroll_box_start=0, default_scroll_start=0, loop=False,
                 btm_text='', more=False, callback=None, re_draw_after_scroll=True):
        """
        :param ctl: ctl
        :param overflow: hidden or scroll

        :param stop_key: 停止scroll的key
        :param up_key:
        :param down_key:
        :param scroll_box_start: 从哪行开始可以滚动。若第一行要显示标题，则scroll_start=1
        :param default_scroll_start: 初始化时滚动区域第一行下标。
        :param loop: 循环
        :param btm_text: 底部的文本，为空则不显示
        :param more: 类似于man的效果。Ture会自动添加 btm_text
        :param callback: 滚动后的回调
        :param re_draw_after_scroll: 滚动后执行重绘。为false时你需要自己调用re_draw


        current_scroll_start 当前显示的滚动区域的第一行, 详细说明如下


          row_0 
         ------------------------   
        | row_1                  |  <= terminal, height=4
        | row_2                  |
        | row_3                  |
        | row_4                  |
         ------------------------    

        外框表示terminal，其高度为4。row 1-4 显示在terminal中。
        此时current_scroll_start = 1 
        若 loop=False ，触发down时 current_scroll_start不变 （ 注意不会+1 !!）
        若 loop=True ，触发down时 current_scroll_start=0 

        --- 

        假设terminal高度为4，table有5行，
        初始化时 current_scroll_start=4，首次绘制时 current_scroll_start 会被设为1


        """
        self.current_scroll_start = default_scroll_start
        if self.current_scroll_start < self.scroll_box_start:
            self.current_scroll_start = self.scroll_box_start
        if more:
            self.btm_text = '-- more --'

    def init_kl(self):
        """
        :rtype: KeyListener
        """
        self.key_listener = KeyListener()
        if self.stop_key:
            self.key_listener.bind_key(
                self.stop_key, self._stop, decorator=False)
        if self.up_key:
            self.key_listener.bind_key(self.up_key, self._up, decorator=False)
        if self.down_key:
            self.key_listener.bind_key(
                self.down_key, self._down, decorator=False)
        return self.key_listener

    def draw(self):
        # 修改table的overflow
        table = self.ctl.get_layout()
        self.old_layout_overflow = table.get_overflow_vertical()
        table.set_overflow_vertical(OverflowVertical.none)
        # 添加btm
        if self.btm_text:
            r = TableRow.quick_init(scroll_btm_row,
                                    TextView(scroll_btm_text, self.btm_text)
                                    )
            table.add_view(r)

        self.update(self.current_scroll_start, is_first=True)

        self.ctl.draw(auto_re_draw=False)

    def scroll(self):
        self.init_kl()
        self.draw()
        self.key_listener.listen()

    def _callback(self, event):
        if not self.callback:
            return
        self.callback(event)

    def _up(self, kl, event):
        self.up()
        if self.re_draw_after_scroll:
            self.ctl.re_draw()
        self._callback(ScrollEvent.up)

    def up(self):
        self.update(self.current_scroll_start-1)

    def _down(self, kl, event):
        self.down()
        if self.re_draw_after_scroll:
            self.ctl.re_draw()
        self._callback(ScrollEvent.down)

    def down(self):
        self.update(self.current_scroll_start+1)

    def _stop(self, kl, event):
        self.stop(kl)
        if self.re_draw_after_scroll:
            self.ctl.draw()
        self._callback(ScrollEvent.stop)

    def stop(self, kl):
        kl.stop()
        table = self.ctl.get_layout()
        table.set_overflow_vertical(self.old_layout_overflow)
        if self.btm_text:
            table.remove_view_by_id('_scroll_btm_row_')
            table.view.old_row_visibility.pop(-1)

    def update(self, new_current_scroll_start, is_first=False):
        _, h = self.ctl.get_terminal_size()
        # 最后一行需要显示光标，因此-1
        h -= 1+self.scroll_box_start

        table = self.ctl.get_layout().view

        scroll_box_end = len(table.data)

        if self.btm_text:
            h -= 1
            scroll_box_end -= 1

        scroll_box_h = scroll_box_end-self.scroll_box_start

        for r in table.data:
            if r.visibility == Visibility.gone:
                scroll_box_h -= 1
        if h >= scroll_box_h:
            return

        scroll_start = new_current_scroll_start
        if scroll_start < self.scroll_box_start:
            # 首次绘制时，不会出现 scroll_start<self.scroll_box_start
            # 因此进这里一定是按了up键
            if self.loop:
                scroll_start = scroll_box_end-h
            else:
                scroll_start = self.scroll_box_start
        elif scroll_start+h > scroll_box_end:
            # 进这里说明是按down键，或者首次绘制时
            if self.loop and not is_first:
                scroll_start = self.scroll_box_start

        # 计算scroll_start， scroll_end
        # 优先显示scroll_start下面部分，高度还有剩余就从上面补

        left_h = h
        scroll_end = scroll_start

        # 因为可能有view隐藏的情况，这里直接循环到scroll_box_end，而不是 scroll_start+h
        for i, r in enumerate(table.data[scroll_start:scroll_box_end]):
            if not left_h:
                break

            scroll_end = scroll_start+i+1
            if r.visibility != Visibility.gone:
                left_h -= 1

        while left_h and scroll_start-1 >= self.scroll_box_start:
            scroll_start -= 1
            if table.data[scroll_start].visibility != Visibility.gone:
                left_h -= 1
        self.current_scroll_start = scroll_start

        # 修改 visibility
        table.old_row_visibility = []
        for r in table.data[:self.scroll_box_start]:
            table.old_row_visibility.append(r.visibility)

        for i, r in enumerate(table.data[self.scroll_box_start:scroll_box_end]):
            i += self.scroll_box_start
            table.old_row_visibility.append(r.visibility)
            if i >= scroll_start and i < scroll_end:
                r._set_is_show(True)
            else:
                r.visibility = Visibility.gone
                r._set_is_show(False)

        if self.btm_text:
            btm =table.data[-1]
            table.old_row_visibility.append(btm.visibility)
            if self.more and scroll_end >= scroll_box_end:
                btm.data[0].text='-- end --'
            else:
                btm.data[0].text='-- more --'
