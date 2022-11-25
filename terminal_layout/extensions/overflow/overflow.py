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
from terminal_layout.readkey import Key
from terminal_layout.log import logger
try:
    from os import get_terminal_size
except:
    from backports.shutil_get_terminal_size import get_terminal_size


class OverflowType:
    hidden = 'hidden'
    scroll = 'scroll'

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


class OverflowVertical(View, Hidden):
    """
    垂直方向的Overflow
    """
    is_first_draw = True
    h_cache = None
    old_row_visibility = None

    @instance_variables
    def __init__(self, table, overflow=OverflowType.hidden,
                 # 下面参数type为scroll时才有效
                 stop_key=Key.ESC, up_key=Key.UP, down_key=Key.DOWN,
                 scroll_start=0, current_index=0, loop=False,
                 btm_text='-- more --'):
        """
        :param table: TableLayout
        :param overflow: hidden or scroll
        :param stop_key: 停止按键监听的key
        :param up_key: 
        :param down_key: 
        :param scroll_start: 从哪行开始支持滚动。比如有标题的情况下标题是不需滚动的。
        :param current_index: 第一次绘制时最开头的行数

        """
        pass

    def before_draw(self):
        if self.overflow == OverflowType.hidden:
            self.hidden()
        else:
            self.scroll()

    def draw(self):
        logger.debug(f'before_draw 1 old={self.old_row_visibility}')
        self.before_draw()
        logger.debug(f'before_draw 2 old={self.old_row_visibility}')

        self.table.draw()
        self.after_draw()
        logger.debug(f'after_draw old={self.old_row_visibility}')


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


