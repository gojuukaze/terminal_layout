terminal_layout
===============

| The project help you to quickly build layouts in terminal
| (这个一个命令行ui布局工具)

.. raw:: html

   <img src="pic/demo.gif"  alt="demo.gif" width="400"/>

**Extensions**

-  `progress`_

|image0|

-  `choice`_

|image1|

--------------

|asciicast|

link
====

-  `All Demo`_
-  `GIthub`_
-  `Docs`_
-  `https://asciinema.org/a/226120`_

install
=======

.. code:: bash

   pip install terminal-layout

Usage
=====

-  easy demo:

.. code:: python

   import time
   from terminal_layout import *

   ctl = LayoutCtl.quick(TableLayout,
                         # table id: root
                         [
                             [TextView('t1', 'Hello World!', width=Width.fill, back=Back.blue)],  # <- row id: root_row_1,
                             [TextView('t2', '', fore=Fore.magenta)],  # <- row id: root_row_2,
                         ],
                         )

   # or layout=ctl.get_layout()
   layout = ctl.find_view_by_id('root')
   layout.set_width(20)

   # default: auto_re_draw=True
   ctl.draw()

   # call delay_set_text() must be set auto_re_draw=True,
   # otherwise you must start a thread to call re_draw() by yourself
   # 如果使用delay_set_text(), 必须把auto_re_draw设为True，否则你需要自己在线程中执行re_draw()
   ctl.find_view_by_id('t2').delay_set_text('你好,世界!', delay=0.2)

   time.sleep(0.5)
   row3 = TableRow.quick_init('', [TextView('t3', 'こんにちは、世界!')])
   layout.add_view(row3)

   # If you call draw() with auto_re_draw=True, you must stop()
   # 如果执行draw()时auto_re_draw=True，你必须执行stop()
   ctl.stop()

|image3|

-  use ``re_draw()``

.. code:: python

   import time
   from terminal_layout import *

   ctl = LayoutCtl.quick(TableLayout,
                         # table id: root
                         [
                             [TextView('t1', 'Hello World!', width=Width.fill, back=Back.blue)],  # <- row id: root_row_1,
                             [TextView('t2', '', fore=Fore.magenta)],  # <- row id: root_row_2,
                         ],
                         )


   layout = ctl.find_view_by_id('root')
   layout.set_width(20)

   ctl.draw(auto_re_draw=False)

   ctl.find_view_by_id('t2').set_text('你好,世界!')
   ctl.re_draw()

   time.sleep(0.5)
   row3 = TableRow.quick_init('', [TextView('t3', 'こんにちは、世界!')])
   layout.add_view(row3)
   ctl.re_draw()

   # don't need call stop()
   # 不需执行stop()
   # ctl.stop()


-  use python2 unicode

.. code:: python

   # -*- coding: utf-8 -*-
   from terminal_layout import *
   import sys
   reload(sys)
   sys.setdefaultencoding('utf-8')

   ctl = LayoutCtl.quick(TableLayout,
                         [
                             [TextView('', u'中文，你好', back=Back.cyan, width=Width.wrap)],
                             [TextView('', u'中文，你好', back=Back.cyan, width=6)],
                             [TextView('', u'日本語，こんにちは', ba

.. _progress: terminal_layout/extensions/progress/README.md
.. _choice: terminal_layout/extensions/choice/README.md
.. _All Demo: https://github.com/gojuukaze/terminal_layout/tree/master/demo
.. _GIthub: https://github.com/gojuukaze/terminal_layout
.. _Docs: https://terminal-layout.readthedocs.io
.. _`https://asciinema.org/a/226120`: https://asciinema.org/a/226120

.. |image0| image:: pic/progress.gif
.. |image1| image:: pic/choice.gif
.. |asciicast| image:: https://asciinema.org/a/226120.svg
   :target: https://asciinema.org/a/226120
.. |image3| image:: pic/hello.png
