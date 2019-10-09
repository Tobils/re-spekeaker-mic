# RESPEAKER USB 4 MIC ARRAY
https://respeaker.io/usb_4_mic_array/#how-to-control-the-rgb-led-ring
https://brookbach.com/iot/2017/12/27/play-respeaker-mic-array-en.html

## cara menggunakan respeaker
http://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/

## tuning
* git clone https://github.com/respeaker/usb_4_mic_array.git
* cd usb_4_mic_array
* python tuning.py -p

## control led
* git clone https://github.com/respeaker/pixel_ring.git
* cd pixel_ring
* sudo python setup.py install
* sudo python examples/usb_mic_array.py


## install portaudio
Sorry about the inappropriate answer last time, I will post the solution of the question. It might be helpful for Ubuntu distributions.

* First we need to install portaudio modules: sudo apt-get install libasound-dev
* Download the portaudio archive from: http://portaudio.com/download.html
* Unzip the archive: tar -zxvf [portaudio.tgz]
* Enter the directory, then run: ./configure && make
* Install: sudo make install
* And finally: sudo pip install pyaudio
* Check the version of pyaudio, it should be 0.2.9

## RECORD
arecord -D plughw:1,0 -f cd test.wav # record, please use the arecord -l to check the card and hardware first
aplay -D plughw:1,0 -f cd test.wav # play, please use the aplay -l to check the card and hardware first
arecord -D plughw:1,0 -f cd |aplay -D plughw:1,0 -f cd # record and play at the same time

sudo python get_index.py
output :
Input Device id  5  -  ReSpeaker 4 Mic Array (UAC1.0): USB Audio (hw:1,0)

ganti 
RESPEAKER_INDEX = 5  # refer to input device id


## ODAS
sudo apt-get install libfftw3-dev libconfig-dev libasound2-dev libgconf-2-4
sudo apt-get install cmake
git clone https://github.com/introlab/odas.git
mkdir odas/build
cd odas/build
cmake ..
make

## UPGRADE FIRMWARE
sudo apt-get update
sudo pip install pyusb click
git clone https://github.com/respeaker/usb_4_mic_array.git
cd usb_4_mic_array
sudo python dfu.py --download 6_channels_firmware.bin  # The 6 channels version 
sudo python dfu.py --download 1_channel_firmware.bin



