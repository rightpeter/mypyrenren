#-*-coding:utf-8-*-

# 人人刷人品脚本

import time
import signal
import getpass
import sys
import os

from datetime import datetime
from pyrenren import RenRen

def SignalHandler(sig, id):
    if sig == signal.SIGHUP:
        print 'received signal HUP'

signal.signal(signal.SIGHUP, SignalHandler)

username = sys.argv[1]
passwd = sys.argv[2]

print(username)
print(passwd)

renren = RenRen( username, passwd )

pid = os.fork()

if pid != 0:
    os._exit(0)

print('Create daemon!')

while True:
    print str(datetime.now()), 'refresh index'
    renren.get('http://www.renren.com')
    time.sleep(60*10)
