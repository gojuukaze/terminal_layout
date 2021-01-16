快速开始
============

欢迎使用terminal_layout，这个项目可以帮你告别单调的命令行输出，使你的输出富有色彩、结构。
你可以通过下面例子快速的了解这个项目

.. code-block:: python

    from terminal_layout import *

    ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('title', 'Student', fore=Fore.black, back=Back.blue, width=17,
                                    gravity=Gravity.center)],

                          [TextView('', 'No.', width=5, back=Back.blue),
                           TextView('', 'Name', width=12, back=Back.blue)],

                          [TextView('st1_no', '1', width=5, back=Back.blue),
                           TextView('st1_name', 'Bob', width=12, back=Back.blue)],

                          [TextView('st2_no', '2', width=5, back=Back.blue),
                           TextView('st2_name', 'Tom', width=12, back=Back.blue)],
                      ]

                      )

    ctl.draw()
    ctl.stop()

``LayoutCtl`` , ``TableLayout`` , ``TextView`` 是该项目重要的元素，接下来会一一介绍他们。

阅读 :doc:`/draw` ， :doc:`/keyListener` 熟悉如何使用terminal_layout