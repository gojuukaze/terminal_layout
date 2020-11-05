import threading
import time

from terminal_layout import *
from terminal_layout.extensions.progress.progress import Progress, SuffixStyle
from terminal_layout.helper.class_helper import instance_variables
from terminal_layout.logger import logger


class InfixChoices:
    style1 = ['-', '\\', '|', '/']
    style2 = ["◰", "◳", "◲", "◱"]
    style3 = ["◐", "◓", "◑", "◒"]
    style4 = [".", "o", "O", "°", "O", "o", "."]
    style5 = ['▁', '▂', '▃', '▅', '▆', '▇', ]
    style6 = ["ဝ", "၀"]
    style7 = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    style8 = ['◷', '◶', '◵', '◴']
    style9 = ['( ◐ ω ◐ )', '( ◓ ω ◓ )', '( ◑ ω ◑ )', '( ◒ ω ◒ )', ]
    style10 = ["( ^ . ^ )", "( ^ o ^ )", "( ^ O ^ )", "( ^ o ^ )"]


class Loading(Progress):
    ctl = None

    @instance_variables
    def __init__(self, prefix, max, refresh_time=0.2, delimiter=None, infix=None,
                 suffix_style=SuffixStyle.percent):
        """


        :param prefix: 
        :type prefix: str
        :param max: 
        :type max: int
        :param suffix_style: 
        :type suffix_style: SuffixStyle
        """
        if infix is None:
            self.infix = InfixChoices.style7
        if delimiter is None:
            self.delimiter = [' ', ' ']
        self.infix_index = 0
        self.current_progress = 0
        self.lock = threading.Lock()
        self.update_infix_thread = threading.Thread(
            target=self.update_infix,
            args=(self,)
        )
        self.update_infix_thread.daemon = True
        self.stop_flag = False

    @staticmethod
    def update_infix(loading):
        """
        Update infix. infix.

        Args:
            loading: (str): write your description
        """
        def run():
            """
            Run infix.

            Args:
            """
            progress_view = loading.ctl.find_view_by_id('progress')
            loading.infix_index += 1
            loading.infix_index %= len(loading.infix)
            progress_view.set_text(loading.infix[loading.infix_index])

        while True:
            if loading.stop_flag:
                break
            loading.run_with_lock(run)
            time.sleep(loading.refresh_time)

    def run_with_lock(self, func, args=None):
        """
        Runs a lock.

        Args:
            self: (todo): write your description
            func: (callable): write your description
        """
        if args == None:
            args = []
        self.lock.acquire()
        func(*args)
        self.lock.release()

    def add_progress(self, num):
        """
        Add a progress bar.

        Args:
            self: (todo): write your description
            num: (int): write your description
        """
        self.run_with_lock(super().add_progress, [num])

    def set_progress(self, num):
        """
        Set the progress bar.

        Args:
            self: (todo): write your description
            num: (int): write your description
        """
        self.run_with_lock(super().set_progress, [num])

    def update(self):
        """
        Update the view

        Args:
            self: (todo): write your description
        """

        self.ctl.find_view_by_id('suffix').set_text(self.get_suffix())

    def start(self):
        """
        Start the terminal.

        Args:
            self: (todo): write your description
        """
        prefix_width = len(self.prefix)
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

        self.update()
        self.stop_flag = False
        self.update_infix_thread.start()
        self.ctl.draw()

    def stop(self):
        """
        Stop the interface threads.

        Args:
            self: (todo): write your description
        """
        self.stop_flag = True
        if self.ctl:
            self.ctl.stop()
            self.ctl = None

    def is_finished(self):
        """
        Return true if the progress bar is finished.

        Args:
            self: (todo): write your description
        """
        return self.current_progress >= self.max

    def __enter__(self):
        """
        Enter the start and stop the call.

        Args:
            self: (todo): write your description
        """
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the given exception.

        Args:
            self: (todo): write your description
            exc_type: (todo): write your description
            exc_val: (todo): write your description
            exc_tb: (todo): write your description
        """
        self.stop()
