terminal_layout
===============

| The project help you to quickly build layouts in terminal
| (这个一个命令行ui布局工具)

.. image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/demo.gif
   :width: 450

--------------

**Some extensions base on terminal_layout**

-  `progress <terminal_layout/extensions/progress/README.md>`__

|progress.gif|

-  `choice <terminal_layout/extensions/choice/README.md>`__

|choice.gif|

--------------

\*\* video demo \*\*

.. image:: https://asciinema.org/a/226120.svg
   :width: 550
   :target: https://asciinema.org/a/226120


link
====

-  `All
   Demo <https://github.com/gojuukaze/terminal_layout/tree/master/demo>`__
-  `Github <https://github.com/gojuukaze/terminal_layout>`__
-  `Docs <https://terminal-layout.readthedocs.io>`__
-  `https://asciinema.org/a/226120 <https://asciinema.org/a/226120>`__

install
=======

.. code:: bash

   pip install terminal-layout

Dependencies
============

-  Python 2.7, 3.5+ (maybe 3.4)
-  Linux, OS X, and Windows systems.

Usage
=====

-  easy demo:

.. code:: python

   import time
   from terminal_layout import *

   ctl = LayoutCtl.quick(TableLayout,
                         # table id: root
                         [
                             [TextView('t1', 'Hello World!', width=Width.fill, back=Back.blue)],  # <- row id: root_row_0,
                             [TextView('t2', '', fore=Fore.magenta)],  # <- row id: root_row_1,
                         ],
                         )

   # or layout=ctl.get_layout()
   layout = ctl.find_view_by_id('root')
   layout.set_width(20)

   # default: auto_re_draw=True
   ctl.draw()

   # call delay_set_text() must be set auto_re_draw=True,
   # otherwise you must start a thread to call re_draw() by yourself
   ctl.find_view_by_id('t2').delay_set_text('你好,世界!', delay=0.2)

   time.sleep(0.5)
   row3 = TableRow.quick_init('', [TextView('t3', 'こんにちは、世界!')])
   layout.add_view(row3)

   # If you call draw() with auto_re_draw=True, you must stop()
   ctl.stop()

|image2|

-  disable auto_re_draw

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
                             [TextView('', u'日本語，こんにちは', back=Back.cyan, width=Width.wrap)],
                         ]

                         )

   ctl.draw()

|image3|

Properties
----------

-  fore & back

.. code:: python

   TextView('','fore',fore=Fore.red)
   TextView('','back',back=Back.red)


.. image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/color.jpeg
   :width: 560

-  style

.. code:: python

   TextView('','style',style=Style.dim)


.. image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/style.jpeg
   :width: 560

-  width

.. code:: python

   TextView('','width',width=10)


.. image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/width.jpeg
   :width: 560

-  weight

.. code:: python

   TextView('','weight',weight=1)


.. image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/weight.jpeg
   :width: 560

-  gravity

.. code:: python

   TextView('','gravity',gravity=Gravity.left)


.. image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/gravity.jpeg
   :width: 560


-  visibility

.. code:: python

   TextView('','',visibility=Visibility.visible)


.. image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/visibility.jpeg
   :width: 560

-  ex_style (not support windows)

.. code:: python

   TextView('','ex_style',style=Style.ex_blink)


.. image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/ex_style.jpeg
   :width: 560

-  ex_fore & ex_back (not support windows)

.. code:: python

   TextView('','ex_fore',fore=Fore.ex_red_1)
   TextView('','ex_back',back=Back.ex_red_1)


.. image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/ex_color.jpeg
   :width: 560

LICENSE
=======

`GPLv3 <https://github.com/gojuukaze/terminal_layout/blob/master/LICENSE>`__

Thanks
======

-  `colorama <https://github.com/tartley/colorama>`__ : Simple
   cross-platform colored terminal text in Python
-  `colored <https://gitlab.com/dslackw/colored>`__ : Very simple Python
   library for color and formatting in terminal

.. |progress.gif| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/progress.gif
.. |choice.gif| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/choice.gif
.. |image2| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/hello.png
.. |image3| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/py2.png
