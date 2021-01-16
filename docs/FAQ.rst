FAQ
=====

如何获取 ``View`` 的宽度
--------------------------------

View的宽度有两种，``width``, ``real_width``

* ``width`` : 初始化时设置的宽度值
* ``real_width`` : 真正绘制的宽度。注意！在绘制之前这个值都不是有效的值

如果需要在绘制之前获取 ``real_width`` ，可以调用 ``LayoutCtl.update_width()`` 更新宽度后再获取
``real_width`` 不是固定的，终端宽度发生变化这个值就会改变。
因此你可能会需要每次获取 ``real_width`` 之前都调用 ``update_width()``

具体参照 https://github.com/gojuukaze/terminal_layout/blob/master/demo/demo6(get_width).py


屏幕闪烁
--------------------------------

输出的文本太大会出现界面闪烁的情况，这时要调大sys.stdout的缓冲区。具体情况见： https://github.com/gojuukaze/terminal_layout/issues/3

可通过 ``ctl.set_buffer_size()`` 函数调大缓冲区。（建议在draw之前调用）



