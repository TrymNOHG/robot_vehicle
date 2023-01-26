#!/usr/bin/env pybricks-micropython

 #import
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import random


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.



# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

right_motor = Motor(Port.A)
left_motor = Motor(Port.D)
robot = DriveBase (right_motor, left_motor, wheel_diameter = 56, axle_track = 114)

cs1 = ColorSensor(Port.S1)
cs2 = ColorSensor(Port.S4)
us = UltrasonicSensor(Port.S3)




kp = 5

speed = 50


program_on = True
robo_on = True

time1 = time.time()

def f1():
    ev3.speaker.play_file("Isbil.wav")
    

def f2():
    robot.drive_time(100, 180, 8)
    

def f3():
    ev3.speaker.play_file(SoundFile.ELEPHANT_CALL)
    ev3.speaker.play_file(SoundFile.UH_OH)
    ev3.speaker.play_file(SoundFile.SHOUTING)   
    ev3.speaker.play_file(SoundFile.KUNG_FU) 
    ev3.speaker.play_file(SoundFile.SMACK)
    ev3.speaker.play_file(SoundFile.OUCH)
   
    
    

def f4():
    ev3.screen.print("Beep Boop Pivot Element")
    wait(5000)
    

f_list = [f1, f2, f3, f4]

while program_on == True:
    if ev3.buttons.pressed():
        
        ev3.speaker.say("Exercise 3")
        ref_limit1 = cs1.reflection()
        ref_limit2 = cs2.reflection()
        print(ref_limit1)
        print(ref_limit2)
        ev3.speaker.play_file("Isbil.wav")
        
        while robo_on == True:
            devi1 = ref_limit1 - cs1.reflection()
            devi2 = cs2.reflection() - ref_limit2 

            turn_r = kp * (devi1 + devi2)

            robot.drive(speed, turn_r)

            time2 = time.time()
            if time2 - time1 >= 10:
                robot.stop()
                time1 = time.time()
                rtall = random.randint(0,3)
                f_list[rtall]()
            
            if us.distance() < 190:
                robot.stop()
                ev3.speaker.play_file(SoundFile.CHEERING)
                robo_on = False
                program_on = False

            
        
            if ev3.buttons.pressed():
                ev3.speaker.say("Exercise done")
                robo_on = False
                program_on = False
            
            

# Create your objects here.

 
 
 




