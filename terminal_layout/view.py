# -*- coding: utf-8 -*-
int()
class ViewText(object):

    length=None

    text_list=[]

    def __init__(self, text):
        text = text.replace('\n', ' ').replace('\t', ' ' * 4)

    def __len__(self):
        if self.length is None:
            pass

class View(object):

    def __init__(self, text, text_color='', back_color=''):
        """

        :param text:
        :param text_color: choices from choices
        :param back_color:
        """
        self.text = text
        self.view_text = None
        self.text_color = text_color
        self.back_color = back_color

    def get_original_text(self):
        return self.text

    def get_view_text(self):
        return self.view_text

    def __str__(self):
        return self.text_color + self.back_color + self.text

    def __setattr__(self, key, value: str):
        if key == 'text':
            view_text = value.replace('\n', ' '.replace('\t', ' ' * 4))
