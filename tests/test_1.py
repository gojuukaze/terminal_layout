# -*- coding: utf-8 -*-

from terminal_layout.types import String
import six
import sys

if six.PY2:
    reload(sys)
    sys.setdefaultencoding('utf-8')


def test_view_string():
    s = String('aaa')
    assert len(s) == 3
    assert s[:2] == 'aa'
    if six.PY2:
        s = String(u'a啊啊')
        assert len(s) == 5
        assert s[:2] == 'a'

        assert s[:3] == u'a啊啊'[:2]
    else:
        s = String('a啊啊')
        assert len(s) == 5
        assert s[:2] == 'a'
        assert s[:3] == 'a啊'
