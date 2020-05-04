import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import time

import numpy as np
import matplotlib.pyplot as plt

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


# Main program loop.
start_time = time.time()
values = []
for _ in range(20000):
    values.append(mcp.read_adc(0))
finish_time = time.time()
print (values)
print (f"1000 samples collected in {finish_time - start_time} seconds, rate of {1000/(finish_time - start_time)})")

plt.plot(values)
plt.show()
