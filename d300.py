#!/usr/bin/python3.4
from time import sleep
from gpiozero import LED
import sys

shatter = LED(2)
nframe = int(sys.argv[1])
exposure = int(sys.argv[2])
delay = int(sys.argv[3])
if len(sys.argv) != 4 or (nframe in range(1,300)) == False or (exposure in range(1,3000)) == False or (delay in range(1,60)) == False:
    print("please input valid arguments!\n")
    sys.exit()
print("nframe:" + sys.argv[1],"expoxure:" + sys.argv[2],"delay:" + sys.argv[3])

for i in range(nframe):
    shatter.off()
    sleep(2)
    shatter.on()
    sleep(exposure)
    shatter.off()
    sleep(delay)
