from terminal_layout import *
from terminal_layout.helper.class_helper import instance_variables
from terminal_layout.logger import logger


class StringStyle(object):

    def __init__(self, fore=None, back=None, style=None):
        self.fore = fore or ''
        self.back = back or ''
        self.style = style or ''

    def to_dict(self):
        return {
            'fore': self.fore,
            'back': self.back,
            'style': self.style
        }


class Choice(object):
    @instance_variables
    def __init__(self, title, choices, icon='> ', icon_style=StringStyle(fore=Fore.green), choices_style=StringStyle(),
                 selected_style=StringStyle(), loop=True):
        self.current = 0

    def get_choice(self):
        views = []
        for i, c in enumerate(self.choices):
            views.append(
                [TextView('icon%d' % i, self.icon, visibility=Visibility.invisible, **self.icon_style.to_dict()),
                 TextView('', c, **self.choices_style.to_dict())])

        views[0][0].visibility = Visibility.visible
        views[0][1] = TextView('', self.choices[0], **self.selected_style.to_dict())
        self.ctl = LayoutCtl.quick(TableLayout,
                                   views)
        self.ctl.draw()

        kl = KeyListener()
        kl.bind_key(Key.UP, Key.DOWN, self.change_current, decorator=False)
        kl.listen()

    def change_current(self, kl, event):
        temp = self.current
        if event.key == Key.UP:
            temp -= 1
        elif event.key == Key.DOWN:
            temp += 1
        if temp < 0:
            temp = len(self.choices) - 1
        if temp >= len(self.choices):
            temp = 0
        logger.info(event.key == Key.UP)
        self.ctl.find_view_by_id('icon%d' % self.current).set_visibility(Visibility.invisible)
        self.current = temp
        self.ctl.find_view_by_id('icon%d' % self.current).set_visibility(Visibility.visible)
