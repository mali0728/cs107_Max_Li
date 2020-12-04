# Problem 1A -- Markov chain -- for Homework 7 of CS107
# Author: Max Li

from Markov import Markov 
import numpy as np

weather_today = Markov()
weather_today.load_data(file_path='./weather.csv')
# print(weather_today.get_prob('sunny', 'cloudy')) # This line should print 0.3
print("The probability that a windy day follows a cloudy day is: ", weather_today.get_prob('cloudy', 'windy')) 
# print("The probability that a windy day follows a cloudy day is: ", weather_today.get_prob('cloud', 'wind')) # raise exception
# print("The probability that a windy day follows a cloudy day is: ", weather_today.get_prob('Cloudy', 'WindY')) # upper case

