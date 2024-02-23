import sys
import requests
import csv


"""
This is Home work 2, you are allowed to work in pairs, you can only use chatGPT or other AI model on the course discord public channel.

# Student Name 1: Meghan
# Student Name 2: Tyler

# Additional comment for this program, any bugs or creative functions?

# This program takes in three arguments: Column Name, Keyword to access specific data, and CSV filename.

"""

api_key = "https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=9tXHRpu5YkfMwpZt8ZC2XF2y0ZARlHQX"


print("This script is going to collect weather data and store in a csv file:")
print("First, enter a column name for the data requested:")
colName = input("Column name:")
print("Next, enter the keyword for the wind data you want. Options are windSpeed, windGust and windDirection.")
keyword = input("Keyword:")
print("Finally, type the name for your CSV file. (Remember to add \".csv\" to the end)")
addrOut = input("CSV name:")
#print("python "+sys.argv[0]+" \"Column_Name\" windSpeed windData.csv")
#sys.exit(0)

#colName = sys.argv[1]
#keyword = sys.argv[2]
#addrOut = sys.argv[3]

# put your code here
response = requests.get(api_key)
data = response.json()

# dictionary with only hourly data
hourly_data = data["timelines"]["hourly"]

# new dictionary to hold extracted information about Wind
windData = {"Date": [], "Time": [], colName: []}

# iterates through each hour in the API
for i in range(len(hourly_data)):
    # timeline retrieves line to get info on Date and Time
    timeline = hourly_data[i]["time"]

    # this grabs the specific date and time for the i entry and adds to windSpeed
    date = timeline[0:10]
    time = timeline[12:19]
    windData["Date"].append(date)
    windData["Time"].append(time)

    # this adds the wind direction for the given entry into the dictionary
    windData[colName].append(hourly_data[i]["values"][keyword])


csv_file = addrOut

with open(csv_file, 'w', newline='') as file:
    fieldnames = windData.keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # write the header
    writer.writeheader()

    # write the data
    for row in zip(*windData.values()):
        writer.writerow(dict(zip(fieldnames, row)))

print("csv file was successfully created")
