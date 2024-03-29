# -*- coding: utf-8 -*-
import os
import sys
import platform
import threading
import time
from typing import Union


from terminal_layout.helper.helper import get_terminal_size
from terminal_layout.ansi import term_init
from terminal_layout.view import *
from terminal_layout.view.base import View


class NULL:
    pass


class BaseViewProxy(object):
    def __init__(self, ctl, view):
        self.ctl = ctl  # type: LayoutCtl
        self.view = view

    def set(self, k, v, raise_error):
        try:
            setattr(self.view, k, v)
        except Exception as e:
            if raise_error:
                raise e

    def set_width(self, width, raise_error=False):
        self.set('width', width, raise_error)

    def set_visibility(self, visibility, raise_error=False):
        self.set('visibility', visibility, raise_error)

    def set_gravity(self, gravity, raise_error=False):
        self.set('gravity', gravity, raise_error)

    def set_text(self, text, raise_error=False):
        self.set('text', text, raise_error)

    def set_back(self, back, raise_error=False):
        self.set('back', back, raise_error)

    def set_style(self, style, raise_error=False):
        self.set('style', style, raise_error)

    def set_fore(self, fore, raise_error=False):
        self.set('fore', fore, raise_error)

    def set_weight(self, weight, raise_error=False):
        self.set('weight', weight, raise_error)

    def delay_set_text(self, text, delay=0.3):
        """
        set text one by one
        """
        s = ''
        for c in text:
            s += c
            self.set_text(s, raise_error=True)
            time.sleep(delay)

    def get(self, k, default):
        """
        if default == NULL , it is raised an error when the attribute doesn't exist
        如果default为NULL，当不存在变量时会抛错
        """
        if default == NULL:
            return getattr(self.view, k)
        else:
            return getattr(self.view, k, default)

    def get_id(self, default=NULL):
        return self.get('id', default)

    def get_width(self, default=NULL):
        return self.get('width', default)

    def get_real_width(self, default=NULL):
        return self.get('real_width', default)

    def get_visibility(self, default=NULL):
        return self.get('visibility', default)

    def get_gravity(self, default=NULL):
        return self.get('gravity', default)

    def get_text(self, default=NULL):
        return self.get('text', default)

    def get_back(self, default=NULL):
        return self.get('back', default)

    def get_style(self, default=NULL):
        self.get('style', default)

    def get_fore(self, default=NULL):
        self.get('fore', default)

    def get_weight(self, default=NULL):
        self.get('weight', default)

    def get_parent(self, default=NULL):
        """
        :rtype: View
        """
        self.get('parent', default)

    def remove(self):
        """
        :rtype: bool
        """
        return self.view.remove()

    def is_show(self):
        return self.view.is_show()


class TextViewProxy(BaseViewProxy):

    def set_text(self, text, raise_error=False):
        self.set('text', text, raise_error)

    def set_back(self, back, raise_error=False):
        self.set('back', back, raise_error)

    def set_style(self, style, raise_error=False):
        self.set('style', style, raise_error)

    def set_fore(self, fore, raise_error=False):
        self.set('fore', fore, raise_error)

    def set_weight(self, weight, raise_error=False):
        self.set('weight', weight, raise_error)

    def set_overflow(self, overflow, raise_error=False):
        self.set('overflow', overflow, raise_error)

    def delay_set_text(self, text, delay=0.3):
        """
        set text one by one
        """
        s = ''
        for c in text:
            s += c
            self.set_text(s, raise_error=True)
            time.sleep(delay)

    def get_text(self, default=NULL):
        return self.get('text', default)

    def get_back(self, default=NULL):
        return self.get('back', default)

    def get_style(self, default=NULL):
        self.get('style', default)

    def get_fore(self, default=NULL):
        self.get('fore', default)

    def get_weight(self, default=NULL):
        self.get('weight', default)

    def get_overflow(self, default=NULL):
        self.get('overflow', default)


class LayoutProxy(BaseViewProxy):
    def add_view(self, v):
        self.view.add_view(v)

    def add_views(self, *views):
        self.view.add_views(*views)

    def add_view_list(self, views):
        self.view.add_view_list(views)

    def insert_view(self, i, view):
        return self.view.insert(i, view)

    def remove_view_by_id(self, id):
        """
        :rtype: bool
        """
        return self.view.remove_view_by_id(id)

    def set_overflow_vertical(self, overflow_vertical, raise_error=False):
        self.set('overflow_vertical', overflow_vertical, raise_error)

    def get_overflow_vertical(self, default=NULL):
        return self.get('overflow_vertical', default)


class LayoutCtl(object):
    debug = False
    version = 0
    _drawing = False
    _stop_flag = False
    auto_re_draw = True

    def check(self):
        if not sys.stdout.isatty():
            raise RuntimeError('terminal_layout can only run on Terminal')

    def __init__(self, layout=None, skip_check=False):
        if not skip_check:
            self.check()
        self.layout = layout  # type:View
        self.refresh_lock = threading.Lock()
        self.init_refresh_thread()

    def init_refresh_thread(self):
        self.refresh_thread_stop = False
        self.refresh_thread = threading.Thread(
            target=LayoutCtl.refresh,
            args=(self,),
        )
        self.refresh_thread.daemon = True

    def set_buffer_size(self, size):
        """
        当输出的文本太大会出现界面闪烁的情况，这时要调大sys.stdout的缓冲区
        （见 https://github.com/gojuukaze/terminal_layout/issues/3 ）
        建议在draw之前调用
        """
        self.buffering = size
        sys.stdout = os.fdopen(sys.stdout.fileno(), 'w',
                               self.buffering, encoding='utf-8')

    def is_stop(self):
        return self._stop_flag

    @classmethod
    def quick(cls, layout_class, data, id='root', row_id_formatter='{table_id}_row_{index}'):
        """

        :param layout_class: TableRow or TableLayout
        :param data: TableRow的data为 [textView, ...] ;
                     TableLayout的data为 [ [textView], ]

        :param id: layout的id
        :param row_id_formatter: 创建TableLayout时设置row的id。

        :return:
        :rtype :LayoutCtl
        """
        if layout_class is TableLayout:
            table_layout = TableLayout.quick_init(id, data, row_id_formatter)
            return cls(table_layout)
        elif layout_class is TableRow:
            row = TableRow.quick_init(id, data)
            return cls(row)
        else:
            raise TypeError("quick not support %s" % (str(layout_class, )))

    def set_layout(self, layout):
        """

        :return:
        """

        self.layout = layout

    def get_layout(self) -> LayoutProxy:
        """

        :return:
        :rtype:LayoutProxy
        """
        return LayoutProxy(self, self.layout)

    def enable_debug(self, width=50, height=10):
        self.debug = True
        self.debug_width = width
        self.debug_height = height

    def get_terminal_size(self):
        if self.debug:
            self.height = self.debug_height
            self.width = self.debug_width
        else:
            size = get_terminal_size()
            self.height = size.lines
            self.width = size.columns

            if platform.system() == 'Windows':
                self.width -= 1

        return self.width, self.height

    def update_width(self):
        self.get_terminal_size()
        self.layout.update_width(self.width)

    def draw(self, auto_re_draw=True):
        term_init()
        self.auto_re_draw = auto_re_draw
        self.version += 1
        self.update_width()
        self.layout.set_terminal_size(*self.get_terminal_size())
        self.layout.draw()

        sys.stdout.write('\n')
        sys.stdout.flush()
        if auto_re_draw:
            self.refresh_thread.start()

    def clear(self):
        self.layout.clear()

    def re_draw(self):
        self.refresh_lock.acquire()
        self.clear()

        self.update_width()
        self.layout.set_terminal_size(*self.get_terminal_size())

        self.layout.draw()

        sys.stdout.write('\n')
        sys.stdout.flush()
        self.refresh_lock.release()

    @staticmethod
    def refresh(ctl):
        while True:
            if ctl.is_stop() or ctl.refresh_thread_stop:
                break
            time.sleep(0.1)
            ctl.re_draw()

    def find_view_by_id(self, id) -> Union[TextViewProxy, LayoutProxy, None]:
        """
        :rtype: Union[TextViewProxy, LayoutProxy, None]
        """
        v = self.layout.find_view_by_id(id)
        if not v:
            return None
        if isinstance(v, TextView):
            return TextViewProxy(self, v)
        else:
            return LayoutProxy(self, v)

    def stop(self):
        if not self.is_stop():
            self._stop_flag = True
            self.refresh_thread.join()
            self.re_draw()
