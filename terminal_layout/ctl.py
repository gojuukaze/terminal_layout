# -*- coding: utf-8 -*-
import os
import sys
import platform
import threading
import time

try:
    # py3
    from os import get_terminal_size
except:
    # py2
    from backports.shutil_get_terminal_size import get_terminal_size

from terminal_layout.ansi import term_init
from terminal_layout.logger import logger
from terminal_layout.view import *
from terminal_layout.view.base import View


class LayoutCtl(object):
    debug = False
    version = 0
    _drawing = False
    _stop_flag = False

    def __init__(self, layout=None):
        """
        Initialize thread.

        Args:
            self: (todo): write your description
            layout: (todo): write your description
        """
        self.layout = layout  # type:View
        self.refresh_lock = threading.Lock()
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
        sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', self.buffering, encoding='utf-8')

    def is_stop(self):
        """
        Return true if stop_flag is true.

        Args:
            self: (todo): write your description
        """
        return self._stop_flag

    @classmethod
    def quick(cls, layout_class, data):
        """

        :param layout_class:
        :param data:
        :return:
        :rtype :LayoutCtl
        """
        if layout_class is TableLayout:

            table_layout = TableLayout('root', Width.fill)
            i = 0
            for row_data in data:
                table_row = TableRow.quick_init('root_row_' + str(i), row_data, width=Width.fill)
                table_layout.add_view(table_row)
                i += 1
            return cls(table_layout)
        elif layout_class is TableRow:
            row = TableRow.quick_init('root', data, width=Width.fill)
            return cls(row)
        else:
            raise TypeError("quick not support %s" % (str(layout_class, )))

    def set_layout(self, layout):
        """

        :return:
        """

        self.layout = layout

    def get_layout(self):
        """

        :return:
        :rtype:LayoutProxy
        """
        return LayoutProxy(self, self.layout)

    def get_terminal_size(self):
        """
        Return the width of the terminal.

        Args:
            self: (todo): write your description
        """
        if self.debug:
            self.height = 10
            self.width = 50
            return

        size = get_terminal_size()
        self.height = size.lines
        self.width = size.columns

        if platform.system() == 'Windows':
            self.width -= 1
        return self.width, self.height

    def update_width(self):
        """
        Updates width.

        Args:
            self: (todo): write your description
        """
        self.get_terminal_size()
        self.layout.update_width(self.width)

    def draw(self, auto_re_draw=True):
        """
        Draw the terminal

        Args:
            self: (todo): write your description
            auto_re_draw: (bool): write your description
        """
        term_init()
        self.version += 1
        self.update_width()
        self.layout.draw()

        sys.stdout.write('\n')
        sys.stdout.flush()
        if auto_re_draw:
            self.refresh_thread.start()

    def clear(self):
        """
        Clears the layout.

        Args:
            self: (todo): write your description
        """
        self.layout.clear()

    def re_draw(self):
        """
        Re_width

        Args:
            self: (todo): write your description
        """
        self.refresh_lock.acquire()
        self.clear()

        self.update_width()
        self.layout.draw()

        sys.stdout.write('\n')
        sys.stdout.flush()
        self.refresh_lock.release()

    @staticmethod
    def refresh(ctl):
        """
        Refresh the running threads.

        Args:
            ctl: (todo): write your description
        """
        while True:
            if ctl.is_stop():
                break
            time.sleep(0.1)
            ctl.re_draw()

    def find_view_by_id(self, id):
        """
        Find a view by its id.

        Args:
            self: (todo): write your description
            id: (int): write your description
        """
        v = self.layout.find_view_by_id(id)
        if not v:
            return None
        if isinstance(v, TextView):
            return TextViewProxy(self, v)
        else:
            return LayoutProxy(self, v)

    def stop(self):
        """
        Stop the thread.

        Args:
            self: (todo): write your description
        """
        if not self.is_stop():
            self._stop_flag = True
            self.refresh_thread.join()
            self.re_draw()


class NULL:
    pass


class BaseViewProxy(object):
    def __init__(self, ctl, view):
        """
        Initialize the view.

        Args:
            self: (todo): write your description
            ctl: (str): write your description
            view: (bool): write your description
        """
        self.ctl = ctl  # type: LayoutCtl
        self.view = view

    def set(self, k, v, raise_error):
        """
        Sets the k value of k.

        Args:
            self: (todo): write your description
            k: (dict): write your description
            v: (dict): write your description
            raise_error: (bool): write your description
        """
        try:
            setattr(self.view, k, v)
        except Exception as e:
            if raise_error:
                raise e

    def set_width(self, width, raise_error=False):
        """
        Set the width.

        Args:
            self: (todo): write your description
            width: (int): write your description
            raise_error: (bool): write your description
        """
        self.set('width', width, raise_error)

    def set_visibility(self, visibility, raise_error=False):
        """
        Sets the visibility.

        Args:
            self: (todo): write your description
            visibility: (str): write your description
            raise_error: (bool): write your description
        """
        self.set('visibility', visibility, raise_error)

    def set_gravity(self, gravity, raise_error=False):
        """
        Sets the binary operator.

        Args:
            self: (todo): write your description
            gravity: (todo): write your description
            raise_error: (bool): write your description
        """
        self.set('gravity', gravity, raise_error)

    def set_text(self, text, raise_error=False):
        """
        Sets the text text.

        Args:
            self: (todo): write your description
            text: (str): write your description
            raise_error: (bool): write your description
        """
        self.set('text', text, raise_error)

    def set_back(self, back, raise_error=False):
        """
        Sets the back of the backend.

        Args:
            self: (todo): write your description
            back: (todo): write your description
            raise_error: (bool): write your description
        """
        self.set('back', back, raise_error)

    def set_style(self, style, raise_error=False):
        """
        Sets the style of this node.

        Args:
            self: (todo): write your description
            style: (str): write your description
            raise_error: (bool): write your description
        """
        self.set('style', style, raise_error)

    def set_fore(self, fore, raise_error=False):
        """
        Sets the foreground.

        Args:
            self: (todo): write your description
            fore: (todo): write your description
            raise_error: (bool): write your description
        """
        self.set('fore', fore, raise_error)

    def set_weight(self, weight, raise_error=False):
        """
        Sets weight.

        Args:
            self: (todo): write your description
            weight: (str): write your description
            raise_error: (bool): write your description
        """
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
        When default == NULL , it is raised an error when the attribute doesn't exist
        如果default为NULL，当不存在变量时会抛错
        """
        if default == NULL:
            return getattr(self.view, k)
        else:
            return getattr(self.view, k, default)

    def get_id(self, default=NULL):
        """
        Returns the id of the given id.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (bool): write your description
        """
        return self.get('id', default)

    def get_width(self, default=NULL):
        """
        Returns the width of the field.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (int): write your description
        """
        return self.get('width', default)

    def get_real_width(self, default=NULL):
        """
        Returns the width of the real real part.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (todo): write your description
        """
        return self.get('real_width', default)

    def get_visibility(self, default=NULL):
        """
        Returns the visibility of the user.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (str): write your description
        """
        return self.get('visibility', default)

    def get_gravity(self, default=NULL):
        """
        Return the default value of this node

        Args:
            self: (dict): write your description
            default: (todo): write your description
            NULL: (str): write your description
        """
        return self.get('gravity', default)

    def get_text(self, default=NULL):
        """
        Return the text of this node

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (todo): write your description
        """
        return self.get('text', default)

    def get_back(self, default=NULL):
        """
        Gets the default backends.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (todo): write your description
        """
        return self.get('back', default)

    def get_style(self, default=NULL):
        """
        Get the style

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (str): write your description
        """
        self.get('style', default)

    def get_fore(self, default=NULL):
        """
        Gets the default foreground.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (str): write your description
        """
        self.get('fore', default)

    def get_weight(self, default=NULL):
        """
        Gets the weight.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (array): write your description
        """
        self.get('weight', default)


class TextViewProxy(BaseViewProxy):

    def set_text(self, text, raise_error=False):
        """
        Sets the text text.

        Args:
            self: (todo): write your description
            text: (str): write your description
            raise_error: (bool): write your description
        """
        self.set('text', text, raise_error)

    def set_back(self, back, raise_error=False):
        """
        Sets the back of the backend.

        Args:
            self: (todo): write your description
            back: (todo): write your description
            raise_error: (bool): write your description
        """
        self.set('back', back, raise_error)

    def set_style(self, style, raise_error=False):
        """
        Sets the style of this node.

        Args:
            self: (todo): write your description
            style: (str): write your description
            raise_error: (bool): write your description
        """
        self.set('style', style, raise_error)

    def set_fore(self, fore, raise_error=False):
        """
        Sets the foreground.

        Args:
            self: (todo): write your description
            fore: (todo): write your description
            raise_error: (bool): write your description
        """
        self.set('fore', fore, raise_error)

    def set_weight(self, weight, raise_error=False):
        """
        Sets weight.

        Args:
            self: (todo): write your description
            weight: (str): write your description
            raise_error: (bool): write your description
        """
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

    def get_text(self, default=NULL):
        """
        Return the text of this node

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (todo): write your description
        """
        return self.get('text', default)

    def get_back(self, default=NULL):
        """
        Gets the default backends.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (todo): write your description
        """
        return self.get('back', default)

    def get_style(self, default=NULL):
        """
        Get the style

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (str): write your description
        """
        self.get('style', default)

    def get_fore(self, default=NULL):
        """
        Gets the default foreground.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (str): write your description
        """
        self.get('fore', default)

    def get_weight(self, default=NULL):
        """
        Gets the weight.

        Args:
            self: (todo): write your description
            default: (todo): write your description
            NULL: (array): write your description
        """
        self.get('weight', default)


class LayoutProxy(BaseViewProxy):
    def add_view(self, v):
        """
        Add a new view.

        Args:
            self: (todo): write your description
            v: (todo): write your description
        """
        self.view.add_view(v)

    def add_views(self, *views):
        """
        Add views.

        Args:
            self: (todo): write your description
            views: (todo): write your description
        """
        self.view.add_views(*views)

    def add_view_list(self, views):
        """
        Add a new view list.

        Args:
            self: (todo): write your description
            views: (todo): write your description
        """
        self.view.add_view_list(views)

    def insert_view(self, i, view):
        """
        Inserts the view.

        Args:
            self: (todo): write your description
            i: (todo): write your description
            view: (todo): write your description
        """
        self.view.insert(i, view)
