from tuning import Tuning
import usb.core
import usb.util
import time
from usb_pixel_ring_v2 import PixelRing
import usb.core

import pyaudio
import wave
import numpy as np

RESPEAKER_RATE      = 16000
RESPEAKER_CHANNELS  = 6 # change base on firmwares, 1_channel_firmware.bin as 1 or 6_channels_firmware.bin as 6
RESPEAKER_WIDTH     = 2
# run getDeviceInfo.py to get index
RESPEAKER_INDEX     = 5  # refer to input device id
CHUNK               = 1024
RECORD_SECONDS      = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(
            rate     = RESPEAKER_RATE,
            format   = p.get_format_from_width(RESPEAKER_WIDTH),
            channels = RESPEAKER_CHANNELS,
            input    = True,
            input_device_index = RESPEAKER_INDEX,
            )

print("* recording")

frames = []
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

if dev:
    pixel_ring = PixelRing(dev)
    Mic_tuning = Tuning(dev)
    print Mic_tuning.direction
    while True:
        try:
            print Mic_tuning.direction
            pixel_ring.wakeup(180)
            data = stream.read(CHUNK)   
            
            if Mic_tuning.is_voice() == 1:
                frames.append(data)
            
        except KeyboardInterrupt:
            pixel_ring.off()
            print("* done recording")
            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(RESPEAKER_CHANNELS)
            wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
            wf.setframerate(RESPEAKER_RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            break


# record saat vad saja, kalo silent tidak di detect
