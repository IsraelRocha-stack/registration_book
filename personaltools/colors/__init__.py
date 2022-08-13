def colorstring(a):
    """
Colorize  your strings easily:
<colors.colorstring(0)>  == White
<color.colorstring(1)> == Black
<color.colortring(2)> == Red
<color.colorstring(3)> == Green
<color.colorstring(4)> ==  Yellow
<color.colorstring(5)> == Blue
    :param a: Type a number between 0 and 5
    :return: return one color
    """
    print('\033[29m', end='')
    if a == 1:
        print('\033[30m', end='')
    elif a == 2:
        print('\033[31m', end='')
    elif a == 3:
        print('\033[32m', end='')
    elif a == 4:
        print('\033[33m', end='')
    elif a == 5:
        print('\033[34m', end='')
    elif a == 0:
        print('\033[38m', end='')
    return a


def title(msg):
    from time import sleep
    sleep(0.3)
    print('-' * 90)
    print(f'{msg.center(90)}'.upper())
    print('-' * 90)


def line(n):
    if n == 1:
        print('=' * 90)
    elif n == 2:
        print('~' * 90)
    elif n == 3:
        print('~=' * 45)
    else:
        print('-' * 90)

