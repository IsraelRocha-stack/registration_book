from personaltools import colors, moeda


def file_exist(arch):
    try:
        link = open(arch, 'rt')
        link.close()
    except FileNotFoundError:
        return False
    else:
        return True


def mkdir(arch):
    try:
        link = open(arch, 'wt+')
        link.close()
    except:
        colors.colorstring(2)
        print("There's a problem with archive creation.")
        colors.colorstring(0)
    else:
        colors.colorstring(4)
        print(f"Archive {arch} has ben successfully created")
        colors.colorstring(0)


def readtext(arch):
    global a
    try:
        a = open(arch, 'rt')
    except:
        colors.colorstring(2)
        print("Can't open the archive.txt")
        colors.colorstring(0)
    else:
        colors.colorstring(4)
        colors.title('list of clients')
        colors.colorstring(0)
        for lin in a:
            data = lin.split('R$')
            data[1] = data[1].replace('\n', ' ')
            print(f'\033[0;30;43m{data[0]:.<77}{moeda.coin()}{data[1]:>10}\033[m')
        colors.line(3)
    finally:
        a.close()


def addlist(arch, name='unknown', price=0):
    try:
        link = open(arch, 'at')
    except:
        colors.colorstring(2)
        print('There is a problem to open <archive .txt>')
        colors.colorstring(0)
    else:
        try:
            link.write(f"{name.capitalize()}R${price:.2f}\n")
        except:
            colors.colorstring(2)
            print("There's a problem to write the document")
            colors.colorstring(0)
        else:
            colors.colorstring(3)
            print(f'Client has ben success add.'.center(90))
            colors.colorstring(0)
            link.close()
