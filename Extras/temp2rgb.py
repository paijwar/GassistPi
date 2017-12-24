#!/usr/bin/env python
import math

int red, green, blue

def colourtemp2rgb(kelvin):
temp=kelvin/100
if( temp <= 66 ):
red = 255
green = 99.4708025861 * math.log10(temp) - 161.1195681661
if( temp <= 19):
blue = 0
else:
blue = 138.5177312231 * math.log10(temp-10) - 305.0447927307
else:
red = 329.698727446 * math.pow(temp - 60, -0.1332047592)
green = 288.1221695283 * math.pow(temp - 60, -0.0755148492 )
blue = 255
