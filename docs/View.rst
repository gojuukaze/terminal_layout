View
=============

``View`` 的概念继承自安卓，一共有两种类型的View，分别是 ``Layout`` 与 ``Widget`` 。

此项目 ``Widget`` 只有 ``TextView`` ,目前支持的 ``Layout`` 有 ``TableLayout`` , ``TableRow``



.. py:class:: View

    View方法说明

    .. py:method:: __init__(id, width, height=1, visibility=Visibility.visible, gravity=Gravity.left)

        初始化

        .. py:attribute:: id

            view的唯一id

        .. py:attribute:: width

            view的宽度，可以是正整数，或者 Width.wrap，Width.fill

        .. py:attribute:: height

            view的高度，暂时没用，始终为1


        .. py:attribute:: visibility

            是否显示，可选值 ：Visibility.visible，Visibility.invisible，Visibility.gone

        .. py:attribute:: gravity

            view内部对其方式，可选值：Gravity.left，Gravity.center，Gravity.right


    .. py:method:: get_width()

        获取初始化时设置的width

    .. py:method:: get_real_width()

        最终显示的宽度

    .. py:method:: add_view(view)

        向view中添加一个view

    .. py:method:: insert(index, view)

        向view中每个位置插入一个view


Layout
-------

``Layout`` 是布局控制器，他控制每个 ``Widget`` 显示的位置。

TableLayout
+++++++++++++

表格布局

.. py:class:: TableLayout

    .. py:method:: __init__(id, width=Width.fill, height=1, visibility=Visibility.visible)

        init，**需要注意TableLayout的gravity总是为left**

    .. py:classmethod:: quick_init(id, data, width=Width.fill, height=1, visibility=Visibility.visible)

        快速初始化，

        .. py:attribute:: data

            初始的view list


    .. py:method:: add_view(view)

        向view中添加一个view

    .. py:method:: add_view_list(view_list)

        向view中添加多个view，


TableRow
+++++++++++++

行布局

.. py:class:: TableLayout

    .. py:method:: __init__(id, width=Width.fill, height=1, back=None, visibility=Visibility.visible, gravity=Gravity.left)

        init

        .. py:attribute:: back

            背景色

    .. py:classmethod:: quick_init(id, data, width=Width.fill, height=1, back=None, visibility=Visibility.visible, gravity=Gravity.left)

        快速初始化

        .. py:attribute:: data

            初始的view list


    .. py:method:: add_view(view)

        向view中添加一个view，只支持添加TextView

    .. py:method:: add_view_list(view_list)

        向view中添加多个view，只支持添加TextView

TextView
----------

用于显示文本

.. py:class:: TextView

    .. py:method:: __init__(id, text, fore=None, back=None, style=None, width=Width.wrap, height=1, weight=None, visibility=Visibility.visible, gravity=Gravity.left)

        初始化

        .. py:attribute:: text

            文本

        .. py:attribute:: fore

            颜色


        .. py:attribute:: back

            背景色


        .. py:attribute:: style

            字体样式

        .. py:attribute:: weight

            宽度比重

