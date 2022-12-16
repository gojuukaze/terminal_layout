# -*- coding: utf-8 -*-
from terminal_layout.view.params import Visibility, Gravity


class View(object):
    __slots__ = ('id', 'width', 'height', 'visibility', 'gravity',
                 'real_width', 'real_height', 'data', 'parent', '_is_show')

    def __init__(self, id, width, height=1, visibility=Visibility.visible, gravity=Gravity.left):
        """

        :param id:
        :param width:
        :param height: no used

        :type id:str
        :type width:
        :type height:int
        :type visibility:str
        :type gravity:str
        """

        self.data = []  # type: list[View]
        self.id = id
        self.width = width
        self.height = height
        self.visibility = visibility
        self.gravity = gravity

        self.real_width = None
        self.real_height = None
        self.parent = None

        # 是否显示在屏幕上。这个值用于： 当终端高度不够触发隐藏时，标识view是否显示在屏幕上。
        # 注意：你不应当主动修改这个值这是没意义的；另外is_show不会因visibility改变而改变。
        # 它只有下面两种情况才会被修改:
        # 1. tableLayout的overflow_vertical设为hidden_btm或hidden_top
        # 2. 使用scroll
        self._is_show = True

    def draw(self):
        pass

    def clear(self):
        pass

    def update_width(self, parent_width):
        pass

    def find_view_by_id(self, id):
        """

        :param id:
        :return:
        :rtype: View
        """
        if self.id == id:
            return self
        temp = None
        for v in self.data:
            # 这里不用判断v类型，textView的data是空list
            temp = v.find_view_by_id(id)
            if temp:
                break
        return temp

    def remove(self):
        """
        :rtype: bool
        """
        # 不能移除最外层view
        if not self.parent:
            return False
        return self.parent.remove_view_by_id(self.id)

    def remove_view_by_id(self, id):
        """
        :rtype: bool
        """
        if self.id == id:
            return self.remove()
        index = -1
        for i, v in enumerate(self.data):
            if v.id == id:
                index = i
                break
            # 这里不用判断v类型，textView的data是空list
            ok = v.remove_view_by_id(id)
            if ok:
                return ok
        if index == -1:
            return False
        self.data = self.data[:index]+self.data[index+1:]
        return True

    def get_width(self):
        """
        the width you set in __init__()
        初始化时设置的宽度

        :return:
        """
        return self.width

    def get_real_width(self):
        """

        the real width of the display
        实际显示的宽度

        :return:
        """
        return self.real_width

    def __getitem__(self, item):
        """

        :param item:
        :return:
        :rtype:View
        """
        return self.data[item]

    def insert(self, index, view):
        self.data.insert(index, view)

    def is_show(self):
        return self._is_show and self.visibility != Visibility.gone

    def _set_is_show(self, is_show):
        self._is_show = is_show

    terminal_w = 0
    terminal_h = 0

    def set_terminal_size(self, w, h):
        self.terminal_w = w
        self.terminal_h = h
