输出文字
=======================

基本概念
--------------
- **LayoutCtl** ：layout管理器，负责绘制所有元素
- **View** ： 基础控件，Layout 与 TextView 其实都属于 View

  - Layout ： 布局控制器，控制 TextView 显示的位置。 目前支持的Layout有两种 TableLayout(表格布局)， TableRow(行布局)

  - TextView ： 用于显示文字的view。


显示view
----------

执行下列代码绘制layout

.. code-block:: python

    from terminal_layout import *

    table = TableLayout('id1', width=Width.fill)
    
    row1 = TableRow('row1')
    row1.add_view(TextView('text1', 'hello',fore=Fore.red))
    
    table.add_view(row1)
    table.add_view_list([TableRow('row2'), TableRow('row3')])
    
    ctl = LayoutCtl()
    ctl.set_layout(table)
    ctl.draw()
    ctl.stop()

.. note::
   TableLayout，TableRow，TextView的第一个参数是view的id
   


使用quick init
---------------

每次手动创建layout，text_view会很麻烦，这里为 TableRow，TableLayout，LayoutCtl 提供了quick_init()函数帮助快速创建

TableRow
~~~~~~~~~~~~~~~~

.. code-block:: python

    from terminal_layout import *

    row = TableRow.quick_init('row1', [TextView('title', 'Title', width=Width.wrap)], width=20,
                              gravity=Gravity.center)
    
    ctl = LayoutCtl(row)
    ctl.draw()
    ctl.stop()

.. note::
   LayoutCtl()接受的参数是View，因此直接把TableRow放到ctl中。

   你也可以把TextView直接放入LayoutCtl()，如::

      ctl = LayoutCtl(TextView('title', 'Title', width=10, back=Back.blue))


TableLayout
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from terminal_layout import *

    row1 = TableRow.quick_init('row1', [TextView('title', 'Title', width=Width.wrap)], width=10,
                               gravity=Gravity.center)
    
    data1_view = TextView('data1', '1.', width=3)
    data2_view = TextView('data2', 'foo', width=5)
    row2 = TableRow.quick_init('row2', [data1_view, data2_view])
    
    table_layout = TableLayout.quick_init('', [row1, row2], width=10)
    
    ctl = LayoutCtl(table_layout)
    ctl.draw()
    ctl.stop()

v3.0.0+ data支持 ``[[TextView]]`` 这样的形式，且可以通过 ``row_id_formatter`` 修改row的默认id。（ ``row_id_formatter`` 说明见下方 **LayoutCtl.quick** 部分）

.. code-block:: python

    from terminal_layout import *

    table = TableLayout.quick_init('root',
                               [ # table id: root
                                   [TextView('', '1')], # row id: root_row_0
                                   [TextView('', '2')]  # row id: root_row_1
                               ] , 
                               row_id_formatter='{table_id}_row_{index}'
                               )


LayoutCtl
~~~~~~~~~~~~~~~~
.. code-block:: python

    from terminal_layout import *
    ctl = LayoutCtl.quick(TableLayout,
                          # table id: root
                          [
                              [TextView('title', 'Title', width=Width.wrap)],  # row id: root_row_0
                              [TextView('data1', '1.', width=3), TextView('data2', 'foo', width=5)],  # row id: root_row_1
                          ],
                          id="root",
                          row_id_formatter='{table_id}_row_{index}'
                          )
    ctl.draw()
    ctl.stop()

.. note::

   v3.0.0开始，可以通过 ``id`` 配置最外层的layout id。

   创建 ``TableLayout`` 时可通过 ``row_id_formatter`` 配置 row id。其支持的展位符如下：

   - table_id ：即 id 设置的值
   - index

修改view的属性
----------------

- 使用find_view_by_id获取view并修改（对于重复的id只能获取第一个view）

.. code-block:: python

    import time
    from terminal_layout import *
    
    ctl = LayoutCtl.quick(TableLayout,
                          [
                              [TextView('title', 'Title')],  # row id: root_row_0
                              [TextView('data1', '1.',width=3), TextView('data2', 'foo',width=5)],  # row id: root_row_1
                          ]
                          )
    ctl.draw()
    
    row = ctl.find_view_by_id('root_row_0')
    row.set_width(10)
    row.set_gravity(gravity=Gravity.center)
    
    time.sleep(0.3)
    ctl.find_view_by_id('data1').set_text('2.')
    
    time.sleep(0.3)
    ctl.find_view_by_id('data2').delay_set_text('FOO')
    
    ctl.stop()

* 给layout添加view

.. code-block:: python

    from terminal_layout import *

    from terminal_layout import *

    ctl = LayoutCtl.quick(TableLayout, [])
    
    table = ctl.find_view_by_id('root')
    # append
    table.add_view(TableRow(''))
    table.add_view_list([TableRow(''), TableRow('')])
    
    # insert 用法和list相同
    table.insert(3, TableRow(''))

.. note::

    因为 ``TextView`` 也属于 ``View`` ，因此你可以把 ``TextView`` 加入 ``TableLayout`` 中而不报错。
    如：

    .. code-block:: python

        table = TableLayout('id1')
        table.add_view(TextView('', 'text'))

    这样某些情况下做相当于

    .. code-block:: python

        table = TableLayout('id1')
        row = TableRow.quick_init('', [TextView('', 'text') ] )
        table.add_view(row)

    但第一种方式将不能正确处理某些 ``TextView`` 的自有属性（非基础 ``View`` 的属性）。
    除非你知道你在做什么，否则建议使用第二种方式。

移除view
---------------------

- 你可以使用remove或remove_view_by_id移除view


.. code-block:: python

    from terminal_layout import *
    ctl = LayoutCtl.quick(TableLayout,
                          # table id: root
                          [
                              [TextView('title', 'Title', width=Width.wrap)],  # row id: root_row_0
                              [TextView('data1', '1.', width=3), TextView('data2', 'foo', width=5)],  # row id: root_row_1
                          ]
                          )
    # remove title
    ctl.remove_view_by_id('title')


自动刷新
-------------

v2开始会启动线程自动刷新，因此结束程序时必须手动调用stop()。  

如果你不需要，则设置 auto_re_draw为False 禁用，此时你需要手动调用re_draw()

.. code-block:: python

    from terminal_layout import *
    
    ctl = LayoutCtl(TextView('title', 'Title', width=10))
    ctl.draw(auto_re_draw=False)
    time.sleep(0.5)
    ctl.find_view_by_id('title').set_fore(Fore.red)
    
    ctl.re_draw()

.. note::
   如果禁用了自动刷新，delay_set_text()函数就无效了

View的属性
------------
View的属性包括： ``width`` , ``visibility`` , ``gravity``

TextView在上述基础上增加了：``text`` , ``back`` , ``style`` , ``fore`` , ``weight`` , ``weight`` ,

关于属性的说明参照：:doc:`/Properties`

