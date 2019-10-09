
from tuning import Tuning
import usb.core
import usb.util
import time
from usb_pixel_ring_v2 import PixelRing
import usb.core

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

if dev:
    pixel_ring = PixelRing(dev)
    Mic_tuning = Tuning(dev)
    print Mic_tuning.direction
    while True:
        try:
            pixel_ring.wakeup(180)
            print Mic_tuning.direction
            time.sleep(1)
        except KeyboardInterrupt:
            pixel_ring.off()
            break

