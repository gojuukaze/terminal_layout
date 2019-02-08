terminal_layout
===============

| The project help you to quickly build layouts in terminal
| (这个一个命令行ui布局工具)

|image0|

|asciicast|

link
====

-  `All Demo`_
-  `Doc`_
-  https://asciinema.org/a/226120

install
=======

.. code:: bash

   pip install terminal_layout

Usage
=====

-  easy demo:

.. code:: python

   import time
   from terminal_layout import *

   ctl = LayoutCtl(TextView('id1', 'hello world!', width=20, fore=Fore.red, back=Back.green))

   ctl.draw()

   time.sleep(2)

   view = ctl.find_view_by_id('id1')
   view.text = 'hi world'
   ctl.re_draw()

|image2|

-  use table layout:

.. code:: python

   from terminal_layout import *

   ctl = LayoutCtl(TableLayout,
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

|image3|

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

|image4|

params
------

属性说明

-  fore & back

.. code:: python

   TextView('','fore',fore=Fore.red)
   TextView('','back',back=Back.red)

|image5|

-  style

.. code:: python

   TextView('','style',style=Style.dim)

|image6|

-  width

.. code:: python

   TextView('','width',width=10)

|image7|

-  weight

.. code:: python

   TextView('','weight',weight=1)

|image8|

-  gravity

.. code:: python

   TextView('','gravity',gravity=Gravity.left)

|image9|

-  visibility

.. code:: python

   TextView('','',visibility=Visibility.visible)

|image10|

-  ex_style

**not support windows**

.. code:: python

   from terminal_layout import *
   TextView('','ex_style',style=Style.ex_blink)

|image11|

-  ex_fore & ex_back

**not support windows**

.. code:: python

   from terminal_layout import *
   TextView('','ex_fore',fore=Fore.ex_red_1)
   TextView('','ex_back',back=Back.ex_red_1)

|image12|

.. _All Demo: https://github.com/gojuukaze/terminal_layout/tree/master/demo
.. _Doc: https://github.com/gojuukaze/terminal_layout

.. |image0| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/demo.gif
.. |asciicast| image:: https://asciinema.org/a/226120.svg
   :target: https://asciinema.org/a/226120
.. |image2| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/hello.png
.. |image3| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/table.png
.. |image4| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/py2.png
.. |image5| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/color.jpeg
.. |image6| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/style.jpeg
.. |image7| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/width.jpeg
.. |image8| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/weight.jpeg
.. |image9| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/gravity.jpeg
.. |image10| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/visibility.jpeg
.. |image11| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/ex_style.jpeg
.. |image12| image:: https://github.com/gojuukaze/terminal_layout/raw/master/pic/ex_color.jpeg