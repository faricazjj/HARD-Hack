#DragonBoard Code
# gpio example in python using mraa
#
# Author: Manivannan Sadhasivam <manivannan.sadhasivam@linaro.org>
# Modified by: Team 3 UCSD HARD Hacks 2018
# Usage: Toggles GPIO 23 and 24
#
# Execution: sudo python mraa_gpio.py

import mraa
import time

#========================SET-UP=========================
#ON/OFF for Left and Right
rl_bool = 0    #initially starts with 0 value for OFF
ll_bool = 0    #initially starts with 0 value for OFF
ul_bool = 0    #initially starts with 0 value for OFF
nothing_bool = 0 #initially starts with 0 value for OFF



#Left LED Block
L1_led = mraa.Gpio(23)
L2_led = mraa.Gpio(24)
L3_led = mraa.Gpio(25)


#Right LED Block
R1_led = mraa.Gpio(26)
R2_led = mraa.Gpio(27)
R3_led = mraa.Gpio(29)


#U-turn LEd Block
U1_led = mraa.Gpio(30)
U2_led = mraa.Gpio(31)
U3_led = mraa.Gpio(32)

# set LEFt LED to output
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

"""
nothing: 0
left: 1
right: 2
u-turn: 3
"""

def light_up(dir_num: int):
  if dir_num == 0: 	#do nothing 
		all_off()
    
  elif dir_num == 1:
  	L1_led.write(1)
    
  elif dir_num == 2:
    L2_led.write(1)
    
  elif dir_num == 3:
    L3_led.write(1)
    
  elif dir_num == 4:
  	R1_led.write(1)
    
  elif dir_num == 5:
    R2_led.write(1)
    
  elif dir_num == 6:
    R3_led.write(1)
    
  elif dir_num == 7:
  	U1_led.write(1)
    
  elif dir_num == 8:
    U2_led.write(1)
    
  elif dir_num == 9:
    U3led.write(1)
    
  elif dir_num == 10:
  	L1_led.write(1)
    U1_led.write(1)
    
  elif dir_num == 11:
    L2_led.write(1)
    U2_led.write(1)
    
  elif dir_num == 12:
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


if __name__ == "__main__":
	#=========TESTING==========
  time.sleep(2)
  
  for i in range (3):
    #Turn Left Sequence
  	light_up(1)     
    time.sleep(2)
    light_up(2)
    time.sleep(2)
    light_up(3)
    time.sleep(2)
    
    #Reset Lights
    light_up(0)
    time.sleep(3)
    
  	#Turn Right Sequence
  	light_up(4)     
    time.sleep(2)
    light_up(5)
    time.sleep(2)
    light_up(6)
    time.sleep(2)
    
    #Reset Lights
    light_up(0)
    time.sleep(3)
    
    
    #U-Turn Sequence
  	light_up(4)     
    time.sleep(2)
    light_up(5)
    time.sleep(2)
    light_up(6)
    time.sleep(2)
    
    #Reset Lights
    light_up(0)
    time.sleep(3)
    
    
    
    
    
    
    
    
    
    

  



  
