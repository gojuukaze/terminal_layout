import time

from terminal_layout import *

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('title', '** Terminal Layout **', fore=Fore.black, width=Width.fill,
                                    gravity=Gravity.center, style=Style.ex_bold, )],

                          [TextView('', 'What can terminal_layout do for you?')],
                          [TextView('', '')],
                          # 1. set fore back style in terminal
                          [TextView('s1-1', ''),
                           TextView('s1-2', '', fore=Fore.ex_dark_slate_gray_3),
                           TextView('s1-3', '', back=Back.ex_dark_slate_gray_3),
                           TextView('', ' '),
                           TextView('s1-4', '', style=Style.ex_underlined),
                           TextView('', ' '),
                           TextView('s1-5', ''),
                           ],
                          # 2. print string char one by one
                          [TextView('s2', '')],
                          # 3. draw a table
                          [TextView('s3', '')],
                          # 3-1. add row
                          [TextView('s3-1', '')],
                          # 3-2. change text
                          [TextView('s3-2', '')],
                          # 3-3. set gravity and more
                          [TextView('s3-3', '')],
                          [TextView('', '')],
                          # s3 table
                          [TextView('s3-table', 'Table', width=20, gravity=Gravity.center, back=Back.ex_slate_blue_3b,
                                    visibility=Visibility.invisible)],
                          [TextView('s3-table-r1-1', 'No1', width=10, back=Back.ex_sky_blue_2,
                                    visibility=Visibility.invisible),
                           TextView('s3-table-r1-2', 'Bob', width=10, back=Back.ex_sky_blue_2,
                                    visibility=Visibility.invisible)],
                          [TextView('s3-table-r2-1', 'No2', width=10, back=Back.ex_sky_blue_2,
                                    visibility=Visibility.invisible),
                           TextView('s3-table-r2-2', 'Tom', width=10, back=Back.ex_sky_blue_2,
                                    visibility=Visibility.invisible)],

                      ]

                      )


def s1():
    """
    1. set fore back style in terminal
    :return:
    :rtype:
    """
    for i, s in enumerate(["1. Set", " Fore ", " Back ", "Style", " in terminal"]):
        ctl.find_view_by_id('s1-%d' % (i + 1)).delay_set_text(s, delay=0.1)


def s2():
    """
    2. print string char one by one
    :return: 
    :rtype: 
    """
    ctl.find_view_by_id('s2').delay_set_text('2. Print string char one by one', delay=0.1)


def s3():
    """
    3. draw a table
    :return: 
    :rtype: 
    """

    ctl.find_view_by_id('s3').delay_set_text('3. Draw a table', delay=0.1)

    table_ids = ['s3-table', 's3-table-r1-1', 's3-table-r1-2', 's3-table-r2-1', 's3-table-r2-2']
    for v_id in table_ids:
        ctl.find_view_by_id(v_id).set_visibility(Visibility.visible)
    time.sleep(0.2)
    # 3-1. add row
    ctl.find_view_by_id('s3-1').delay_set_text('   3-1. add row', delay=0.1)
    ctl.get_layout().add_view(
        TableRow.quick_init('', [TextView('s3-table-r3-1', 'No3', width=10, back=Back.ex_sky_blue_2, ),
                                 TextView('s3-table-r3-2', '小王', width=10, back=Back.ex_sky_blue_2, )]))

    time.sleep(0.2)
    # 3-2. change text
    ctl.find_view_by_id('s3-2').delay_set_text('   3-2. change text', delay=0.1)
    ctl.find_view_by_id('s3-table-r3-2').set_text('Wong')
    ctl.find_view_by_id('s3-table-r3-2').set_fore(Fore.black)

    time.sleep(0.2)

    # 3-3. set gravity and more
    ctl.find_view_by_id('s3-3').delay_set_text('   3-3. set gravity and more', delay=0.1)

    for v_id in ['s3-table-r1-1', 's3-table-r1-2', 's3-table-r2-1', 's3-table-r2-2', 's3-table-r3-1', 's3-table-r3-2']:
        ctl.find_view_by_id(v_id).set_gravity(Gravity.center)


print('')
ctl.find_view_by_id('root_row_0').set_width(40)
ctl.draw()

time.sleep(0.5)
s1()
time.sleep(0.2)
s2()
time.sleep(0.2)
s3()

ctl.stop()
print('')
