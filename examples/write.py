import sys
import time

f = open("write.out", "w")

while 1:
    print >> f, "hello"
    print "hello"
    time.sleep(1)
    
f.close()

    
