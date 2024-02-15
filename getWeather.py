import os
import sys


"""
This is Home work 2, you are allowed to work in pairs, you can only use chatGPT or other AI model on the course discord public channel.

# Student Name 1:
# Student Name 2:

# Additional comment for this program, any bugs or creative functions?

"""
api_key = ""

if len(sys.argv)<3:
    print("This script is going to collect weather data and store in a csv file:")
    print("python "+sys.argv[0]+" \"air quality\" airquality.csv")
    sys.exit(0)

keyword = sys.argv[1]
addrOut = sys.argv[2]

# put your code here 
