from personaltools import colors, errohand, archives
from time import sleep

arch = 'list_of_clients.txt'

if not archives.file_exist(arch):
    archives.mkdir(arch)

colors.colorstring(5)
colors.title('''
██████╗░███████╗░██████╗░██╗░██████╗████████╗██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔════╝██╔════╝░██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██████╔╝█████╗░░██║░░██╗░██║╚█████╗░░░░██║░░░██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
██╔══██╗██╔══╝░░██║░░╚██╗██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║░░██║███████╗╚██████╔╝██║██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝            
██████╦╝██║░░██║██║░░██║█████═╝░    
██╔══██╗██║░░██║██║░░██║██╔═██╗░
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗               Version: 1.0.0b
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝''')
colors.colorstring(0)
print('By: \033[33mIsrael Rocha\033[m')
sleep(4)

for c in range(0, 3):
    print('')

while True:
    opt = errohand.menu(['LIST OF CLIENTS', 'REGISTER CLIENT', '\033[31mQUIT\033[m'])
    if opt == 1:
        # List the archive contains.
        archives.readtext(arch)
    elif opt == 2:
        # Add new client.
        name = str(input('Client name: '))
        price = errohand.float_error('R$ ')
        archives.addlist(arch, name, price)
    elif opt == 3:
        colors.title('Ending program...')

        colors.colorstring(5)
        sleep(2)
        print('GoodBye =D')
        colors.colorstring(0)
        break
    else:
        colors.colorstring(2)
        print('Wrong chapter, type a number between 1 and 3')
        colors.colorstring(0)
