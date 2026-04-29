#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# import os


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# directory="Image"
# images=["1.png","2.png","3.png"]
# light_color=["RED","GREEN","ORANGE"]

# for i in range(3):
#     for j in range(3):
#         ev3.screen.load_image(os.path.join(directory,images[j]))
#         wait(300)
#         ev3.light.on(Color.RED)
#         wait(600)

for i in range(3):
    ev3.screen.load_image("Image/1.png")
    wait(300)
    ev3.light.on(Color.RED)
    wait(600)
    ev3.screen.load_image("Image/1.png")
    wait(300)
    ev3.light.on(Color.GREEN)
    wait(600)
    ev3.screen.load_image("Image/1.png")
    wait(300)
    ev3.light.on(Color.ORANGE)
    wait(600)
    ev3.speaker.play_file("Audio/Escape your love(Edit).wav")

# Write your program here.
ev3.speaker.beep()

for i in range(9):
    idx=i%3
    ev3.