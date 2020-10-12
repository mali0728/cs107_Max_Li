# Problem 4_animation -- Movement of the Clock Hands -- for Homework 2 of CS107
# Author: Max Li

import numpy as np
import matplotlib.pyplot as plt
import datetime
import math

def make_clock(r):
    '''This function takes a float reprenting the length of the clock hand and later use it to generate the hand with the proper angle
    raise Value Error if the input is not allow (e.g. not a float)'''
    if not isinstance(r, float):
        raise ValueError("the length of the clock hand should be a float")
    
    def make_hand(theta):
        '''This function takes a float reprenting the angle of the clock hand and generate the hand with the proper angle
        raise Value Error if the input is not allow (e.g. not a float)'''
        if not isinstance(theta, float):
            raise ValueError("the angle of the clock hand should be a float")        
        
        theta_h = math.pi * theta / 180
        x = r * math.cos(theta_h)
        y = r * math.sin(theta_h)
        
        return (x, y)
    
    return make_hand

i = 0
fig = plt.figure(figsize=(6,6))

while i < 120:
    currentDT = datetime.datetime.now()
    hour = currentDT.hour
    minute = currentDT.minute
    second = currentDT.second
    
    # Calculate theta in degrees for each hand
    theta_hour = 90.0 - 30.0 * hour - minute / 2.0
    theta_minute = 90.0 - 6.0 * minute
    theta_second = 90.0 - 6.0 * second
    
    # Specify the length of hour, minute and second hands
    r_hour = 15.0
    r_minute = 25.0
    r_second = 35.0
    
    hour_hand = make_clock(r_hour)
    x_hour, y_hour = hour_hand(theta_hour)
    
    minute_hand = make_clock(r_minute)
    x_minute, y_minute = minute_hand(theta_minute)
    
    second_hand = make_clock(r_second)
    x_second, y_second = second_hand(theta_second)
    
    # Plot the clock
    plt.cla()
    plt.plot([0,x_hour], [0,y_hour], linewidth = 7.0)
    plt.plot([0,x_minute], [0,y_minute], linewidth = 5.0)
    plt.plot([0,x_second], [0,y_second], linewidth = 2.0)
    
    plt.axis([-50, 50, -50, 50])    
    fig.canvas.draw() 

    plt.pause(0.1)
    i+=1

