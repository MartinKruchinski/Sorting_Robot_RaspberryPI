#!/usr/bin/env python3

# TODO Add more details about your overall instrument implementation in the docstring below
"""
Simple musical instrument.
"""


from math import degrees
from utils.brick import  EV3UltrasonicSensor, EV3ColorSensor, Motor, configure_ports
from utils import sound
import datetime
from time import sleep
import brickpi3
from brickpi3 import *
# Add any additional imports in this area, at the top of the file

COLOUR_SENSOR = configure_ports(PORT_1=EV3ColorSensor)
BP = brickpi3.BrickPi3()
BELT_MOTOR_1 = BP.PORT_A
ARM_MOTOR = BP.PORT_B
DROP_MOTOR = BP.PORT_C
PUSH_MOTOR = BP.PORT_D

# Define your classes and functions here. You may use other files, but you don't have to

class  sorter:

    DELAY_SEC = 0.1  #DELAY BETWEEN TOUCH SENSOR POLLING
    COLOURS = ["Green", "Red", "Blue", "Yellow", "Orange", "Purple"]
    location = 0   
    degree_location = 0
    BP = brickpi3.BrickPi3()
    col = None
    purple = None
    sleeping = 0

    def poll_US(self):
        BP.set_motor_position_relative(PUSH_MOTOR, 150)
        sleep(0.1)
        BP.set_motor_position_relative(PUSH_MOTOR, -110)
        waiting = datetime.datetime.now()
        print("Starting")
        try:   
            while True:
                BP.set_motor_power(BELT_MOTOR_1, -12)
                temp = COLOUR_SENSOR.get_rgb()
                rgb_r = temp[0] #First value of RGB
                rgb_g = temp[1] #Second value of RGB
                #Check Colors
                #RED
                #print(temp)
                if rgb_r > 119 and rgb_r < 219 and rgb_g > 17 and rgb_g < 32:
                    print("Red")
                    self.col = "Red";
                    sleep(0.75)
                    BP.set_motor_power(BELT_MOTOR_1, 0)
                    self.sort()
                #ORANGE
                if rgb_r > 185 and rgb_r < 289 and rgb_g > 63 and rgb_g < 92:
                    print("Orange")
                    self.col = "Orange";
                    sleep(0.75)
                    BP.set_motor_power(BELT_MOTOR_1, 0)
                    self.sort()
                #YELLOW
                if rgb_r > 207 and rgb_r < 243 and rgb_g > 191 and rgb_g < 226:
                    print("Yellow")
                    self.col = "Yellow";
                    sleep(0.75)
                    BP.set_motor_power(BELT_MOTOR_1, 0)
                    self.sort()
                #GREEN
                if rgb_r > 14 and rgb_r < 26 and rgb_g > 83 and rgb_g < 142:
                    print("Green")
                    self.col = "Green";
                    sleep(0.75)
                    BP.set_motor_power(BELT_MOTOR_1, 0)
                    self.sort()
                #BLUE
                if rgb_r > 12 and rgb_r < 26 and rgb_g > 26 and rgb_g < 55:
                    print("Blue")
                    self.col = "Blue";
                    sleep(0.75)
                    BP.set_motor_power(BELT_MOTOR_1, 0)
                    self.sort()
                #PURPLE
                if rgb_r > 32 and rgb_r < 56 and rgb_g > 30 and rgb_g < 49:
                    sleep(0.15)
                    temp = COLOUR_SENSOR.get_rgb()
                    print("this is " + str(temp))
                    rgb_r = temp[0] #First value of RGB
                    rgb_g = temp[1] #Second value of RGB
                    if rgb_r > 100 and rgb_r < 300 and rgb_g > 70 and rgb_g < 300:
                        print("Yellow")
                        sleep(0.75)
                        BP.set_motor_power(BELT_MOTOR_1, 0)
                        self.col = "Yellow"
                        self.sort()
                    else:
                        sleep(0.1)
                        temp = COLOUR_SENSOR.get_rgb()
                        print(temp)
                        rgb_r = temp[0] #First value of RGB
                        rgb_g = temp[1] #Second value of RGB
                        if rgb_r > 100 and rgb_r < 290 and rgb_g > 70 and rgb_g < 265:
                            print("Yellow")
                            sleep(0.6)
                            BP.set_motor_power(BELT_MOTOR_1, 0)
                            self.col = "Yellow"
                            self.sort()
                        else:
                            print("Purple")
                            self.col = "Purple"
                            sleep(0.6)
                            BP.set_motor_power(BELT_MOTOR_1, 0)
                            self.sort()
                if (waiting + datetime.timedelta(0,4)) < datetime.datetime.now() : #If cube takes more than 4 seconds to get scanned, push again cause something went wrong
                    self.poll_US()

        except Exception as e:
            print(e)
            self.poll_US()
            
   
    def sort(self):
        sleep(0.2)
        print("Sorting")
        if self.col == "Green":
            self.location = 1
            print("Location " + str(self.location) + " " + self.col)
            
        elif  self.col == "Red":
            self.location = 2
            print("Location " + str(self.location) + " " + self.col)
            
        elif self.col == "Blue":
            self.location = 3
            print("Location " + str(self.location) + " " + self.col)
        
        elif self.col == "Yellow":
            self.location = 4
            print("Location " + str(self.location) + " " + self.col)
            
        elif self.col == "Orange":
            self.location = 5
            print("Location " + str(self.location) + " " + self.col)
            
        elif self.col == "Purple":
            self.location = 6
            print("Location " + str(self.location) + " " + self.col)
        #sleep(3)   
        self.deposit()   

    def deposit(self):
        BP.offset_motor_encoder(ARM_MOTOR,BP.get_motor_encoder(ARM_MOTOR))
        BP.set_motor_limits(ARM_MOTOR, 40, 40)
        print(str(self.location))
        while True:
            if self.location == 1:
                self.degree_location = 0
                self.sleeping = 0
                BP.set_motor_position_relative(ARM_MOTOR,0)
            elif self.location == 2:
                self.degree_location = -45
                BP.set_motor_position_relative(ARM_MOTOR,-45)
                self.sleeping = 2.5
                sleep(2)
            elif self.location == 3:
                self.degree_location = -75
                BP.set_motor_position_relative(ARM_MOTOR,-75)
                self.sleeping = 3
                sleep(2.5)
            elif self.location == 4:
                self.degree_location = -110
                BP.set_motor_position_relative(ARM_MOTOR,-110)
                self.sleeping = 3.5
                sleep(3)
            elif self.location == 5:
                self.degree_location = -140
                BP.set_motor_position_relative(ARM_MOTOR,-140)
                self.sleeping = 4.5
                sleep(3.9)
            elif self.location == 6:
                self.degree_location = -175
                BP.set_motor_position_relative(ARM_MOTOR,-175)
                self.sleeping = 5
                sleep(4.5)
            break
        """""""""
        Function to make the motor drop the cube in the bin
        """""""""
        BP.set_motor_position_relative(DROP_MOTOR,90)
        sleep(1)
        BP.set_motor_position_relative(DROP_MOTOR, -90)
        self.degree_location = self.degree_location * (-1)
        BP.set_motor_position_relative(ARM_MOTOR, self.degree_location)
        sleep(self.sleeping)
        self.poll_US()
if __name__ == "__main__":
    # this import needs to be here to allow sound module to load properly
    ins = sorter()
    ins.poll_US()
    
