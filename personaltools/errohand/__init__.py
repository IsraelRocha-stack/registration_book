from personaltools import colors


def loadings():
    from time import sleep
    colors.colorstring(4)
    print('Processing...')
    colors.colorstring(0)
    sleep(0.5)


def int_error(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            colors.colorstring(2)
            print(f'Invalid method, please, type a entire number!'.upper())
            colors.colorstring(0)
            continue
        except KeyboardInterrupt:
            colors.colorstring(4)
            print('\noperation stopped by user'.upper())
            colors.colorstring(5)
            print('Goodbye! =D')
            colors.colorstring(0)
            quit()
            return 0
        else:
            return n


def float_error(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            colors.colorstring(2)
            print('Invalid chapter, please, type a float number'.upper())
            colors.colorstring(0)
            continue
        except KeyboardInterrupt:
            colors.colorstring(2)
            print('\nOperation stopped by user')
            colors.colorstring(0)
            loadings()
            colors.colorstring(5)
            print('GoodBye')
            colors.colorstring(0)
            quit()
            return 0
        else:
            return n


def menu(lista):
    cont = 0
    for c in range(1, 4):
        print(f'[ {c} ] {lista[cont]}       ', end='')
        cont += 1
    opc = int_error('\nYour option: ')
    return opc
