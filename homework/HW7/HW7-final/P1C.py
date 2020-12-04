# Problem 1C -- Markov chain -- for Homework 7 of CS107
# Author: Max Li

from Markov import Markov

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

city_weather_dict = {}

weather_data = Markov()
weather_data.load_data()

for city, init_weather in city_weather.items():
     markov = Markov(init_weather)
     markov.load_data()
     pred_weather_list = markov.get_weather_for_day(7, 100)
     
     weather_count_dict = {}
     
     for pred in pred_weather_list:
          if pred not in weather_count_dict:
               weather_count_dict[pred] = 1
          else:
               weather_count_dict[pred] += 1
               
     city_weather_dict[city] = weather_count_dict
     print(city + ": ", weather_count_dict)
     
print('\nMost likely weather in seven days')
print('----------------------------------')
     
for city, pred_dict in city_weather_dict.items():
     
     most_common_weather = max(pred_dict, key = pred_dict.get)
     print(city + ": ", most_common_weather)