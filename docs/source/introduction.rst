introduction
============

欢迎使用terminal_layout，这个项目可以帮你告别单调的命令行输出，使你的输出富有色彩、结构。
你可以通过下面例子快速的了解这个项目

.. code-block:: python

    from terminal_layout import *

    ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('title', 'Student', fore=Fore.black, back=Back.yellow, width=17,
                                    gravity=Gravity.center)],

                          [TextView('', 'No.', width=5, back=Back.yellow),
                           TextView('', 'Name', width=12, back=Back.yellow)],

                          [TextView('st1_no', '1', width=5, back=Back.yellow),
                           TextView('st1_name', 'Bob', width=12, back=Back.yellow)],

                          [TextView('stw_no', '2', width=5, back=Back.yellow),
                           TextView('st1_name', 'Tom', width=12, back=Back.yellow)]
                      ]

                      )

    ctl.draw()

``LayoutCtl`` , ``TableLayout`` , ``TextView`` 是该项目重要的元素，接下来会一一介绍他们。

让我们从安装开始吧 :doc:`/installation`