from terminal_layout.view.text_view import TextView

from terminal_layout.view.layout import TableLayout


def is_layout(view):
    return not isinstance(view, TextView)
