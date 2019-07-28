import epaper4in2
from machine import Pin, SPI

sck = Pin(18)
miso = Pin(19)
mosi = Pin(23)
dc = Pin(17)
cs = Pin(5)
rst = Pin(16)
busy = Pin(4)
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=sck, miso=miso, mosi=mosi)

e = epaper4in2.EPD(spi, cs, dc, rst, busy)
e.init()

w = 400
h = 300
x = 0
y = 0

# use a frame buffer
# 400 * 300 / 8 = 15000 - thats a lot of pixels
import adafruit_framebuf as framebuf
buf = bytearray(w * h // 8)
fb = framebuf.FrameBuffer(buf, w, h, buf_format=framebuf.MHMSB)
fb.rotation = 3
print('Frame buffer things')
fb.fill(True)
fb.text('Hello World',30,0,False)
fb.pixel(30, 10, True)
fb.line(30, 70, 40, 80, False)
fb.rect(30, 90, 10, 10, False)
fb.fill_rect(30, 110, 10, 10, False)
for row in range(0,36):
	fb.text(str(row),0,row*8,False)
fb.text('Line 36',0,288,False)
e.display_frame(buf)