
"""
This code attempts to control a servo motor with a USB controller


Helpful resources:
https://www.youtube.com/watch?v=xfhzbw93rzw&t=118s
"""

import usb.core

dev = usb.core.find(idVendor=0x0079, idProduct=0x0006)
ep = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)

dev.set_configuration()
eaddr = ep.bEndpointAddress

r = dev.read(eaddr, 1000)
print(r)
