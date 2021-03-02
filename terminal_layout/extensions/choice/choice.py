from terminal_layout import *
from terminal_layout.helper.class_helper import instance_variables


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
        self.result = None

    def get_choice(self):
        views = [[TextView('', self.title)]]
        for i, c in enumerate(self.choices):
            views.append(
                [TextView('icon%d' % i, self.icon, visibility=Visibility.invisible, **self.icon_style.to_dict()),
                 TextView('value%d' % i, c, **self.choices_style.to_dict())])

        views[1][0].visibility = Visibility.visible
        views[1][1] = TextView('value0', self.choices[0], **self.selected_style.to_dict())
        self.ctl = LayoutCtl.quick(TableLayout,
                                   views)
        self.ctl.draw(auto_re_draw=False)

        kl = KeyListener()
        kl.bind_key(Key.UP, Key.DOWN, self.change_current, decorator=False)
        kl.bind_key(Key.ENTER, self.select, decorator=False)

        kl.listen()
        return self.result

    def update_style(self, view, style):
        view.set_back(style.back)
        view.set_style(style.style)
        view.set_fore(style.fore)

    def change_current(self, kl, event):
        temp = self.current
        if event.key == Key.UP:
            temp -= 1
        elif event.key == Key.DOWN:
            temp += 1
        if temp < 0:
            temp = len(self.choices) - 1 if self.loop else 0
        if temp >= len(self.choices):
            temp = 0 if self.loop else len(self.choices) - 1
        self.ctl.find_view_by_id('icon%d' % self.current).set_visibility(Visibility.invisible)
        self.update_style(self.ctl.find_view_by_id('value%d' % self.current), self.choices_style)

        self.current = temp
        self.ctl.find_view_by_id('icon%d' % self.current).set_visibility(Visibility.visible)
        self.update_style(self.ctl.find_view_by_id('value%d' % self.current), self.selected_style)

        self.ctl.re_draw()

    def select(self, kl, event):
        self.result = (self.current, self.choices[self.current])
        kl.stop()
