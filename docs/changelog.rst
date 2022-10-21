changelog
=============

2.1.3
---------
* 解决 ``readkey()`` 函数在 Win PowerShell 下无法识别方向键 bug ( `#22 <https://github.com/gojuukaze/terminal_layout/issues/22>`__ )
* choice扩展适配高度不够情况，当高度不够时隐藏部分选项 ( `#21 <https://github.com/gojuukaze/terminal_layout/issues/21>`__ )
* choice扩展支持设置stop_key，默认为 ``['q']``

2.1.2
---------
* 增加input扩展，可以获取文字输入了（不支持windows）
* TextView 增加 ``overflow`` 属性，用户文本过长时隐藏左边还是右边
* view 增加 parent 属性
* ctl自动重绘可通过设置 ``refresh_thread_stop`` 停止重绘


2.0.0
---------
* auto refresh 增加自动刷新功能
* add ``delay_set_text()`` 增加渐进显示字符的函数 ``delay_set_text()``
* ``find_view_by_id()`` 返回 ``ViewProxy`` ，不再直接返回view
* 增加扩展 extensions
* 增加按钮监听功能
* 修复python2 bug

1.0.0
--------
