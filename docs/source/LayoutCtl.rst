LayoutCtl
=============

``LayoutCtl`` 是控制 ``View`` ，绘制 ``View`` 的总控制器，你所有的 ``draw()`` ,``re_draw()`` , ``find_view_by_id()`` 等
都应该通过 ``LayoutCtl`` 。

.. py:class:: LayoutCtl

    .. py:method:: __init__(layout=None)

        初始化

    .. py:method:: quick(layout_class, data)

        快速初始化，layout_class只支持TableLayout,TableRow

    .. py:method:: set_layout(layout)

        设置layout

    .. py:method:: get_layout()

        获取layout

    .. py:method:: update_width()

        更新所有layout的宽度

    .. py:method:: draw()

        绘制

    .. py:method:: re_draw()

        重绘

    .. py:method:: find_view_by_id(id)

        获取view