from terminal_layout import *
from terminal_layout.extensions.input import *

title_style = {
    'width': 20,
    'gravity': Gravity.center,
    'fore': Fore.ex_dark_slate_gray_3,
    'back': Back.ex_dark_gray
}
table_color = {
    # 'fore': Fore.ex_dark_slate_gray_3,
    'back': Back.ex_deep_sky_blue_3a
}
ctl = LayoutCtl.quick(TableLayout,
                      [
                          # row_0:title
                          [TextView('step1', 'Step 1', **title_style),
                           TextView('step2', 'Step 2', **title_style),
                           TextView('step3', 'Step 3', **title_style)
                           ],
                          # row_1:tip
                          [TextView('tip1', '(your name)', **title_style),
                           TextView('tip2', '(your age)', **title_style),
                           TextView('tip3', '(confirm)', **title_style)
                           ],
                          # row_2:line
                          [
                              TextView('', '-' * 60)
                          ],
                          # row_3:input
                          [TextView('', '    input: ', ),
                           TextView('input', '', )
                           ],
                          # row_4:empty
                          [
                              TextView('', ' ', ),
                          ],
                          # row_5:table-name
                          [TextView('', '    '),
                           TextView('', 'name: ', width=7, gravity=Gravity.right, **table_color),
                           TextView('name', '', width=10, gravity=Gravity.left, **table_color),
                           ],
                          # row_6:table-age
                          [TextView('', '    '),
                           TextView('', 'age: ', width=7, gravity=Gravity.right, **table_color),
                           TextView('age', '', width=10, gravity=Gravity.left, **table_color),
                           ],
                          # row_7:line
                          [
                              TextView('', '-' * 60)
                          ],
                          # row_8:help
                          [
                              TextView('', '(press enter to confirm)')
                          ],

                      ])


def change_step(last_i, new_i):
    for i, back in [[last_i, title_style['back']], [new_i, Back.ex_slate_blue_3b], ]:
        v = ctl.find_view_by_id('step' + str(i))
        if not v:
            continue
        v.set_back(back)
        v = ctl.find_view_by_id('tip' + str(i))
        v.set_back(back)


def clear_input():
    v = ctl.find_view_by_id('input')
    v.set_text('')


def get_user():
    step = 1
    user = {}
    for i, key in enumerate(['name', 'age', ]):
        step += i
        clear_input()
        change_step(step - 1, step)
        ctl.re_draw()
        ok, v = InputEx(ctl).get_input('input')
        user[key] = v
    return user


def update_table(show_table, user):
    for id in ['root_row_3', 'root_row_4']:
        v = ctl.find_view_by_id(id)
        v.set_visibility(Visibility.gone if show_table else Visibility.visible)
    for id in ['root_row_5', 'root_row_6']:
        v = ctl.find_view_by_id(id)
        v.set_visibility(Visibility.visible if show_table else Visibility.gone)
        if id == 'root_row_5':
            v = ctl.find_view_by_id('name')
            v.set_text(user.get('name', ''))
        if id == 'root_row_6':
            v = ctl.find_view_by_id('age')
            v.set_text(user.get('age', ''))
    ctl.re_draw()


ctl.draw(auto_re_draw=False)
update_table(False, {})

user = get_user()
change_step(2, 3)
update_table(True, user)

kl = KeyListener()


@kl.bind_key(Key.ENTER)
def _(kl, e):
    print('\n', Fore.blue, '- Hello,', user['name'], Fore.reset, '\n')
    kl.stop()


kl.listen()
