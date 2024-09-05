# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the MAX31865 thermocouple amplifier.
# Will print the temperature every second.

# fork SoratobuMacaroniPenguin
# for Micropython-1.23.0 later

import time
import machine as board
from machine import Pin , SoftSPI
#import digitalio
import max31865 as adafruit_max31865 
MISO =　16
MOSI = 5
SCK = 4
CS = 0

# Create sensor object, communicating over the board's default SPI bus
#spi = board.SPI()
spi = SoftSPI(baudrate=200000, polarity=1, phase=0, sck=Pin(SCK), mosi=Pin(MOSI), miso=Pin(MISO))
#cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
cs = CS
sensor = adafruit_max31865.Max31865(spi, cs , rtd_nominal=100, ref_resistor=430.0, wires=3,misoPin=MISO,mosiPin=MOSI,sckPin=SCK)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
# sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=2)

# Main loop to print the temperature every second.
while True:
    # Read temperature.
    temp = sensor.temperature
    # Print the value.
    print("Temperature: {0:0.3f}C".format(temp))
    # Delay for a second.
    time.sleep(1.0)
