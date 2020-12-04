# Problem 1 -- Markov chain -- for Homework 7 of CS107
# Author: Max Li

import numpy as np

class Markov:

    def __init__(self, day_zero_weather = None): # You will need to modify this header line later in Part C
        self.data = None
        self.day_zero_weather = day_zero_weather
        self.weather_list = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy', 'hailing']

    def load_data(self, file_path='./weather.csv'):
        self.data =  np.genfromtxt(file_path,delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather): 
        current_day_weather = current_day_weather.lower()
        next_day_weather = next_day_weather.lower()
        
        if current_day_weather not in self.weather_list:
            raise Exception("The current day weather is not in the list.")
            
        if next_day_weather not in self.weather_list:
            raise Exception("The next day weather is not in the list.")
            
        row_index = self.weather_list.index(current_day_weather)
        col_index = self.weather_list.index(next_day_weather)
        
        return self.data[row_index][col_index]
    
    def __iter__(self):
        return MarkovIterator(self)
    
    def _simulate_weather_for_day(self, day):
        if day < 0:
            raise ValueError("day number must be positive.")
        
        elif day == 0:
            return self.day_zero_weather
        
        else:
            it = iter(self)
            
            for i in range(day):
                current = next(it)

        return current
                
    def get_weather_for_day(self, day, trials = 100):

        pred_weather_list = []
        for i in range(trials):
            pred_weather_list.append(self._simulate_weather_for_day(day))
            
        return pred_weather_list
        
    
class MarkovIterator:
    def __init__(self, markov):
        self.markov = markov
        self.current = markov.day_zero_weather       

    def __iter__(self):            
        return self
        
    def __next__(self):
        if self.current is None:
            raise ValueError("Please enter the current day.")
        
        weather_list = self.markov.weather_list
        self.current = np.random.choice(weather_list, p=self.markov.data[weather_list.index(self.current)])       
            
        return self.current
