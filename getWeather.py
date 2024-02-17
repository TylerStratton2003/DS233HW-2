import os
import sys
import requests


"""
This is Home work 2, you are allowed to work in pairs, you can only use chatGPT or other AI model on the course discord public channel.

# Student Name 1: Meghan
# Student Name 2: Tyler

# Additional comment for this program, any bugs or creative functions?

"""


response = requests.get('https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=9tXHRpu5YkfMwpZt8ZC2XF2y0ZARlHQX')
data = response.json()
print(data)
api_key = ""

if len(sys.argv)<3:
    print("This script is going to collect weather data and store in a csv file:")
    print("python "+sys.argv[0]+" \"air quality\" airquality.csv")
    sys.exit(0)

keyword = sys.argv[1]
addrOut = sys.argv[2]

# put your code here 
