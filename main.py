#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import os, time, _thread

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Initialize the EV3 Brick.
ev3=EV3Brick()

# Initialize the motors.
left_motor=Motor(Port.B)
right_motor=Motor(Port.D)

# Initialize the drive base.
#robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
robot=DriveBase(left_motor,right_motor,55.5,104)

'''
ev3.speaker.beep()
for _ in range(3):
    ev3.screen.load_image("cat1.png")
    wait(300)
    ev3.light.on(Color.RED)
    wait(600)
    ev3.screen.load_image("cat1.png")
    wait(300)
    ev3.light.on(Color.GREEN)
    wait(600)
    ev3.screen.load_image("cat1.png")
    wait(300) #0.3秒
    ev3.light.on(Color.ORANGE)
    wait(600)

ev3.speaker.beep()
'''

#要輪播的圖片清單
IMAGES=[]
for root,dirs,files in os.walk("Image"):
    for filename in files:
        IMAGES.append(os.path.join(root, filename))

#要輪播的燈光清單
LIGHTS=[Color.GREEN,Color.RED,Color.ORANGE]

#音樂播放
def play_music():
    ev3.speaker.play_file("Audio/BAILA MEJOR.wav")

# 輪播圖片函式
def slideshow():
    while True:
        for image in IMAGES:
            ev3.screen.load_image(image)
            time.sleep(1) #1秒

def light():
    while True:
        for light in LIGHTS:
            ev3.light.on(light)
            time.sleep(1)

def move_robot():
    while True:

        #前進2秒
        left_motor.run(300)
        right_motor.run(300)
        time.sleep(2)

        left_motor.stop(Stop.BRAKE)
        right_motor.stop(Stop.BRAKE)
        time.sleep(1)

        #後退2秒
        left_motor.run(-300)
        right_motor.run(-300)
        time.sleep(2)

        left_motor.stop(Stop.BRAKE)
        right_motor.stop(Stop.BRAKE)
        time.sleep(1)


# 建立執行緒
#_thread.start_new_thread(play_music, ())
_thread.start_new_thread(slideshow, ())
_thread.start_new_thread(light, ())
_thread.start_new_thread(move_robot, ())


# 主程式保持運行，避免結束
while True:
    time.sleep(1)
