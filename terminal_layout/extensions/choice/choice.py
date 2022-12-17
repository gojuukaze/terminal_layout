from terminal_layout import *
from terminal_layout.helper.class_helper import instance_variables
from terminal_layout.extensions.scroll import *


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
                 selected_style=StringStyle(), loop=True, default_index=0, stop_key=None):
        self.current = self.get_default_index(default_index)
        self.result = None
        if not stop_key:
            self.stop_key = ['q']

    def get_default_index(self, default_index):
        if default_index < 0 or default_index > len(self.choices):
            return 0
        return default_index

    h_cache = None

    def hidden_choices(self):
        """
        适配高度，当高度不够时隐藏部分choices
        """
        if self.h_cache is None:
            _, self.h_cache = self.ctl.get_terminal_size()
            # 最后一行要留着显示光标，不能输出因此-1
            # title不能隐藏，因此再-1
            self.h_cache -= 2

        if self.h_cache >= len(self.choices) + 1:
            return

        # 优先显示current下面部分，还有剩余高度时从current上面补
        show_start = self.current
        show_end = len(self.choices)
        if show_end - show_start > self.h_cache:
            show_end = show_start + self.h_cache
        left = self.h_cache - show_end + show_start
        if left > 0:
            show_start -= left
        row_id_p = 'root_row_'
        for i in range(len(self.choices)):
            if i >= show_start and i < show_end:
                self.ctl.find_view_by_id(
                    row_id_p + str(i + 1)).set_visibility(Visibility.visible)
            else:
                self.ctl.find_view_by_id(
                    row_id_p + str(i + 1)).set_visibility(Visibility.gone)

    def get_choice(self):
        views = [[TextView('', self.title)]]
        for i, c in enumerate(self.choices):
            views.append(
                [TextView('icon%d' % i, self.icon, visibility=Visibility.invisible, **self.icon_style.to_dict()),
                 TextView('value%d' % i, c, **self.choices_style.to_dict())])
        views[self.current + 1][0].visibility = Visibility.visible
        views[self.current + 1][1] = TextView('value%d' % self.current, self.choices[self.current],
                                              **self.selected_style.to_dict())
        self.ctl = LayoutCtl.quick(TableLayout, views)
        # self.hidden_choices()
        # self.ctl.draw(auto_re_draw=False)

        self.scroll = Scroll(self.ctl, scroll_box_start=1, default_scroll_start=self.default_index,
                             up_key=None, down_key=None, stop_key=None, btm_text='')

        kl = self.scroll.init_kl()
        self.scroll.draw()
        kl.bind_key(Key.UP, Key.DOWN, self.change_current, decorator=False)
        kl.bind_key(Key.ENTER, self.select, decorator=False)

        kl.listen(self.stop_key)
        return self.result

    def update_style(self, view, style):
        view.set_back(style.back)
        view.set_style(style.style)
        view.set_fore(style.fore)

    def change_current(self, kl, event):
        temp = self.current
        loop_tigger = False
        if event.key == Key.UP:
            temp -= 1
        elif event.key == Key.DOWN:
            temp += 1
        if temp < 0:
            if self.loop:
                loop_tigger = True
                temp = len(self.choices) - 1
            else:
                temp = 0
        if temp >= len(self.choices):
            if self.loop:
                loop_tigger = True
                temp = 0
            else:
                temp = len(self.choices) - 1
        self.ctl.find_view_by_id(
            'icon%d' % self.current).set_visibility(Visibility.invisible)
        self.update_style(self.ctl.find_view_by_id('value%d' %
                                                   self.current), self.choices_style)

        self.current = temp
        self.ctl.find_view_by_id(
            'icon%d' % self.current).set_visibility(Visibility.visible)
        self.update_style(self.ctl.find_view_by_id('value%d' %
                                                   self.current), self.selected_style)
        # self.hidden_choices()
        self.scroll.loop = loop_tigger
        if event.key == Key.UP:
            self.scroll.up()
        else:
            self.scroll.down()
        self.ctl.re_draw()

    def select(self, kl, event):
        self.result = (self.current, self.choices[self.current])
        self.scroll.stop(kl)
