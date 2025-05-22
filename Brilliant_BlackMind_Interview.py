'''
You are working on an app which displays current and historic weather forecasts. We want to know how often rain was accurately predicted on our app. In order to do this, you have been provided with two historical data sets as collections of strings:
* The predicted forecasts for each day
* The actual weather for each day

Write a function that takes in these data sets and returns the number of days where both the forecast and the actual weather included rain.

Example: 
forecasts1 = ["Cloudy with rain", "Mostly cloudy", "Sunny", "Rain"]
weather1 = ["Rain", "Cloudy with rain", "Sunny", "Cloudy"]
Expected Result: 1

forecasts2 = ["Rain", "Sunny", "Sunny", "rain"]
weather2 = ["Rain", "Sunny", "Sunny", "rain"]

forecasts3 = ["Partially cloudy", "Rain", "Sunny", "Rain at times heavy"]
weather3 = ["Rain", "Cloudy with rain", "Sunny", "rain"]

All Test Cases:
forecastAccuracy(forecasts1, weather1) -> 1
forecastAccuracy(forecasts2, weather2) -> 2
forecastAccuracy(forecasts3, weather3) -> 2

Complexity analysis variables
N = Number of days in the forecast/weather inputs
'''

def weather(forecast:list, weather:list)-> int:
    a = "rain"
    count = 0
    for i in range(len(forecast)):
        if a in forecast[i].lower() and a in weather[i].lower():
            count += 1
    return count

            
forecasts1 = ["Cloudy with rain", "Mostly cloudy", "Sunny", "Rain"]
weather1 = ["Rain", "Cloudy with rain", "Sunny", "Cloudy"]

forecasts2 = ["Rain", "Sunny", "Sunny", "rain"]
weather2 = ["Rain", "Sunny", "Sunny", "rain"]

forecasts3 = ["Partially cloudy", "Rain", "Sunny", "Rain at times heavy"]
weather3 = ["Rain", "Cloudy with rain", "Sunny", "rain"]


print(weather(forecasts1, weather1))
print(weather(forecasts2, weather2))
print(weather(forecasts3, weather3))