import getpass
import os

def daemonize():
    pid = os.fork()
    
    if pid != 0:
        os._exit(0)

    print('it works!');

username = raw_input('Enter username: ')
passwd = getpass.getpass('Enter passwd: ')

pid = os.fork()

if pid != 0:
    os._exit(0)

print('Create daemon!');
os.system('nohup python rp.py '+username+' '+passwd+' &');
