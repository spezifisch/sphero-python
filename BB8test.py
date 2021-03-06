#!/usr/bin/python
from bluepy import btle
import struct
import time
import BB8_driver
import sys
bb8 = BB8_driver.Sphero()
bb8.connect()


bb8.start()
bb8.join()

if False:
    print "dumpCharacteristics"
    bb8.bt.dumpCharacteristics()
    print "---"

print "RGB ..."
time.sleep(.2)
bb8.set_rgb_led(255,0,0,0,False)
time.sleep(.2)
bb8.set_rgb_led(0,255,0,0,False)
time.sleep(.2)
bb8.set_rgb_led(0,0,255,0,False)

print "Version"
bb8.get_version(True)
bb8.bt.waitForNotifications(1.0)
print "---"

print "L1 Diags"
bb8.run_l1_diags(True)
bb8.bt.waitForNotifications(1.0)
print "---"

time.sleep(5)
bb8.disconnect()
