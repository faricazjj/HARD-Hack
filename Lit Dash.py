# DragonBoard Code
# gpio example in python using mraa
#
# Author: Manivannan Sadhasivam <manivannan.sadhasivam@linaro.org>
# Modified by: Team 3 UCSD HARD Hacks 2018
# Usage: Toggles GPIO 23 and 24
#
# Execution: sudo python mraa_gpio.py

import json
import urllib2
#import urllib.parse
#import urllib.request
import mraa
import time

# ========================SET-UP=========================
BASE_URL = "http://proxoshop.com:3001/directions"

# Left LED Block
L1_led = mraa.Gpio(23)
L2_led = mraa.Gpio(24)
L3_led = mraa.Gpio(27)

# Right LED Block
R1_led = mraa.Gpio(26)
R2_led = mraa.Gpio(25)
R3_led = mraa.Gpio(30)

# U-turn LED Block
U1_led = mraa.Gpio(29)
U2_led = mraa.Gpio(32)
U3_led = mraa.Gpio(31)

# set LEFT LED to output
L1_led.dir(mraa.DIR_OUT)
L2_led.dir(mraa.DIR_OUT)
L3_led.dir(mraa.DIR_OUT)

# set right_led to output
R1_led.dir(mraa.DIR_OUT)
R2_led.dir(mraa.DIR_OUT)
R3_led.dir(mraa.DIR_OUT)

# set u_led to output
U1_led.dir(mraa.DIR_OUT)
U2_led.dir(mraa.DIR_OUT)
U3_led.dir(mraa.DIR_OUT)


def light_up(dir_num):
    """
    This function light's up certain LED blocks based on the direction number:
    - nothing: 0
    - left: 1
    - right: 2
    - u-turn: 3
    """

    all_off()
    if dir_num == 1:
        L1_led.write(1)

    elif dir_num == 2:
        L1_led.write(1)
        L2_led.write(1)

    elif dir_num == 3:
        L1_led.write(1)
        L2_led.write(1)
        L3_led.write(1)

    elif dir_num == 4:
        R1_led.write(1)

    elif dir_num == 5:
        R1_led.write(1)
        R2_led.write(1)

    elif dir_num == 6:
        R1_led.write(1)
        R2_led.write(1)
        R3_led.write(1)

    elif dir_num == 7:
        U1_led.write(1)

    elif dir_num == 8:
        U1_led.write(1)
        U2_led.write(1)

    elif dir_num == 9:
        U1_led.write(1)
        U2_led.write(1)
        U3_led.write(1)

    elif dir_num == 10:
        L1_led.write(1)
        U1_led.write(1)

    elif dir_num == 11:
        L1_led.write(1)
        U1_led.write(1)
        L2_led.write(1)
        U2_led.write(1)

    elif dir_num == 12:
        L1_led.write(1)
        U1_led.write(1)
        L2_led.write(1)
        U2_led.write(1)
        L3_led.write(1)
        U3_led.write(1)


def all_off():
    """Turns off all the leds"""
    L1_led.write(0)
    L2_led.write(0)
    L3_led.write(0)

    R1_led.write(0)
    R2_led.write(0)
    R3_led.write(0)

    U1_led.write(0)
    U2_led.write(0)
    U3_led.write(0)


def get_result(url):
    response = None
    try:
        response = urllib2.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()


if __name__ == "__main__":

    # place_holder = 0
    while True:
        recent_result = get_result(BASE_URL)
        direction = recent_result[0]["direction"]
        # if the direction is -1, break  out of the while loop
        if direction == -1:
            break

            # else, call light_up function passing in the direction
        light_up(direction)
        # print("alrighty, i got the result. here it is:", recent_result)
        # input("stall") #for stalling the while loop













