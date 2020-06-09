import sys

from terminal_layout import *
from terminal_layout.helper.class_helper import instance_variables
from terminal_layout.logger import logger


class SuffixStyle:
    fraction = '{fraction}'  # "1/10"
    percent = '{percent}'  # "10%"
    none = ''


class ProgressWidth:
    fill = 'fill'
    half = 'half'  # half of terminal width


class Progress(object):
    ctl = None

    @instance_variables
    def __init__(self, prefix, max, reached=None, unreached='', delimiter=None, suffix_style=SuffixStyle.percent,
                 width=ProgressWidth.half):
        """

        :param prefix: 
        :type prefix: str
        :param max: 
        :type max: int
        :param reached: 
        :type reached: str
        :param unreached: 
        :type unreached: str
        :param suffix_style: 
        :type suffix_style: SuffixStyle
        :param width: ProgressWidth or width num. width=len(prefix)+len(progress)+len(delimiter)+len(suffix)
        """
        if delimiter is None:
            self.delimiter = [' |', '| ']
        assert self.max > 0
        self.current_progress = 0
        if self.reached is None:
            if sys.platform in ('win32', 'cygwin'):
                self.reached = '='
            else:
                self.reached = '█'

    def get_suffix(self):
        fraction = '%d/%d' % (self.current_progress, self.max)
        percent = '{:.0%}'.format(float(self.current_progress) / self.max)

        return self.suffix_style.format(fraction=fraction, percent=percent)

    def set_progress(self, num):
        if num > self.max:
            num = self.max
        elif num < 0:
            num = 0
        self.current_progress = num
        self.update()

    def add_progress(self, num):
        if num < 0:
            num = 0
        self.current_progress += num
        if self.current_progress > self.max:
            self.current_progress = self.max
        self.update()

    def update(self):
        progress_view = self.ctl.find_view_by_id('progress')
        w = progress_view.get_real_width()
        reached_num = int(float(self.current_progress) / self.max * w)
        s = self.reached * reached_num + self.unreached * (w - reached_num)
        progress_view.set_text(s)

        self.ctl.find_view_by_id('suffix').set_text(self.get_suffix())

    def start(self):
        prefix_width = len(self.prefix)
        delimiter_width = len(self.delimiter[0]) + len(self.delimiter[1])
        if self.suffix_style == SuffixStyle.percent:
            suffix_width = 4
        else:
            suffix_width = len(str(self.max)) * 2 + 1

        self.ctl = LayoutCtl.quick(TableLayout,
                                   [[TextView('prefix', self.prefix, width=prefix_width),
                                     TextView('', self.delimiter[0]),
                                     TextView('progress', ''),
                                     TextView('', self.delimiter[1]),
                                     TextView('suffix', self.get_suffix(), width=suffix_width, gravity=Gravity.right)]])

        if self.width == ProgressWidth.fill:
            self.ctl.find_view_by_id('progress').set_weight(1)
        else:
            terminal_width, _ = self.ctl.get_terminal_size()
            if self.width == ProgressWidth.half:
                progress_width = int((terminal_width - prefix_width - suffix_width - delimiter_width) / 2)
            else:
                progress_width = self.width - prefix_width - suffix_width - delimiter_width
            self.ctl.find_view_by_id('progress').set_width(progress_width)
        self.ctl.update_width()
        self.update()
        self.ctl.draw()

    def stop(self):
        if self.ctl:
            self.ctl.stop()
        self.ctl = None

    def is_finished(self):
        return self.current_progress >= self.max

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
