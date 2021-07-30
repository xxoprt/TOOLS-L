import os
from time import sleep

os.system('clear')

sleep(1)
print '====================Menu=============================='
print '(1)Kali'
print '(2)Ubuntu-18.04'
print '(3)Ubuntu-20.04'
print '(4)lainnya'
print '===================Mksh==============================='

pilih = input('Pilih installan>')

if pilih == 1:
    print 'wait'
    sleep(1)
    os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-xfce.sh | bash')
if pilih == 2:
      print 'wait'
      sleep(1)
      os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu/ubuntu-xfce.sh | bash')
if pilih == 3:
      print 'wait'
      sleep(1)
      os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-xfce.sh  | bash')

if pilih == 4:
    print '===================Menu2========================'
    print '(5).Debian'
    print '(6) Arch'
    print '(7)Lainya2'
    print '================================================'

pilih = input ('pilih insllan>')

if pilih == 5:
     print 'wait'
     sleep(1)
     os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-xfce.sh | bash')

if pilih == 6:
     print 'wait'
     sleep(1)
     os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-xfce.sh | bash')

if pilih == 7:
     print '======================================='
     print '(8) Manjaro'
     print '(9) Fedora'
     print '(10) Lainnya3'
     print '======================================='

pilih = input('pilih installan>')

if pilih == 8:
     print 'wait'
     sleep(1)
     os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-xfce.sh | bash')

if pilih == 9:
     print 'wait'
     sleep(1)
     os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-xfce.sh | bash')

if pilih == 10:
     print '============================================'
     print '(11) Void'
     print '(12) Alpine'
     print '(13) Exit'
     print '============================================'

pilih = input('pilih installan>')

if pilih == 11:
    print 'wait'
    sleep(1)
    os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-xfce.sh | bash')

if pilih == 12:
     print 'wait'
     sleep(1)
     os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpinexfce.sh | bash')