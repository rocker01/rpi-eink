#!/usr/bin/python
# -*- coding:utf-8 -*-
#code adapted by Manu Narang
import sys
import os
import socket
import commands

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image, ImageDraw, ImageFont

epd = epd2in13_V2.EPD()
epd.init(epd.FULL_UPDATE)
#epd.Clear(0xFF)
#

font15 = ImageFont.truetype(os.path.join(picdir, 'Monaco.ttf'), 15)
font24 = ImageFont.truetype(os.path.join(picdir, 'Monaco.ttf'), 24)
font18 = ImageFont.truetype(os.path.join(picdir, 'Monaco.ttf'), 18)


image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame

draw = ImageDraw.Draw(image)

hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
ipAddress2 = commands.getoutput('ifconfig wlan0 | grep "inet " | cut -d " " -f10')

draw.text((0, 0), 'Hello!', font=font18, fill=0)
draw.text((0, 25), hostName + ' ' + ipAddress2, font=font18, fill=0)
draw.text((0, 50), time.strftime("%H:%M:%S %Y-%m-%d"), font=font18, fill=0)


epd.display(epd.getbuffer(image))

