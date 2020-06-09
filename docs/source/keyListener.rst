监听键盘按键
=======================

绑定键盘事件
-------------------------------
实例化一个 :class:`KeyListener` 对象，通过 ``bind_key`` 绑定key


.. code-block:: python

    from terminal_layout import *
    
    key_listener = KeyListener()
    
    @key_listener.bind_key(Key.UP)
    def _(kl, e):
        print(e)
    
    @key_listener.bind_key(Key.DOWN, 'a', '[0-9]')
    def _(kl, e):
        if e.key == 'a':
            print('Press a')
        elif e.key == Key.DOWN:
            print('Press DOWN')
        elif e.key == '0':
            print('Press 0')
        else:
            print('Press 1-9')
    
    def stop(kl, e):
        print('Press', e.key, 'stop!')
        kl.stop()
    
    key_listener.bind_key(Key.ENTER,Key.F1, stop, decorator=False)
    
    key_listener.listen(stop_key=[Key.CTRL_A])

bind_key
--------------

``bind_key`` 绑定的key有三种类型：

- Key的成员变量
- 正则表达式
- "any"（任意按键）

其有两种用法，装饰器模式和非装饰器模；

非装饰器模式下，倒数第二个参数为回调的函数，最后一个参数必须是 ``decorator=False``


允许的Key
---------------

======== ==============================================================
name     keys
======== ==============================================================
Arrows   UP， DOWN， LEFT， RIGHT
Control+ CTRL_A， CTRL_B， CTRL_D， CTRL_E， CTRL_F， CTRL_X， CTRL_Z
F        F1， F2， F3， F4， F5， F6， F7， F8
Other    ENTER， TAB， BACKSPACE， ESC
======== ==============================================================

.. note::
   
   不支持绑定 CTRL_C

   如果需要绑定 ESC ，记得修改stop_key。

停止监听
--------------

有两种方法可以停止监听

1. 回调函数中调用 ``stop()``

2. 开启监听时设置 ``stop_key`` ，如果不设置默认为 [Key.ESC]

绑定不在列表中的key
----------------------

bind_key的参数是非常宽松的，因此你可以绑定不在支持列表中的key

.. code-block:: python

    from terminal_layout import *
    from terminal_layout.readkey.key import KeyInfo
    
    kl = KeyListener()
    
    ctrl_g = KeyInfo('ctrl_g', '\x07')
    
    @kl.bind_key(ctrl_g)
    def _(kl, e):
        print('按下 ctrl_g', e)
    
    
    # or
    ctrl_h_code = '\x08'
    
    @kl.bind_key(ctrl_h_code)
    def _(kl, e):
        print('按下 ctrl_h', e)
    
    
    kl.listen()

