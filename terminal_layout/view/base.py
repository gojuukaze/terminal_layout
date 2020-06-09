# -*- coding: utf-8 -*-
from terminal_layout.view.params import Visibility, Gravity


class View(object):
    __slots__ = ('id', 'width', 'height', 'visibility', 'gravity',
                 'real_width', 'real_height', 'data')

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
            temp = v.find_view_by_id(id)
            if temp:
                break
        return temp

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
