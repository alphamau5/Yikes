# GasHam
This project displays all sorted gas station prices based on user entered address, city, area, and preferred travel distance to gas station. Built with Python, the Urllib, Geocoder, and re libraries are used to web-scrape real-time data and append to a JSON file (not included yet -- in progress).

The URLs and data are scraped from GasBuddy: https://www.gasbuddy.com/ -- it is not my data. For information on the Geocoder library: https://geocoder.readthedocs.io/

The travel distance to each gas station listed is calculated using the Pythagorean Theorem which is only accurate at small distances because it measures distance in a straight line.

After choosing an area and answering a few questions on travel distance, the output will look like this snippet:
```
117.7 --> Husky at 221 Limeridge Road which is about 5.23 km away
123.6 --> Husky at 869 Mohawk Road which is about 10.96 km away
125.9 --> Petro-Canada at 813 Upper James which is about 5.74 km away
125.9 --> Esso at 528 Mohawk Road which is about 8.89 km away
126.6 --> Pioneer at 1822 Upper James which is about 6.62 km away
126.6 --> Pioneer at 386 Upper Gage which is about 5.83 km away
```
These prices are from user data directly inserted into GasBuddy. Because of this, sometimes the prices are missing or outdated. When they aren't however, they are usually correct.
Future projects include increasing the amount of cities the program works for, optimizing the runtime, graphing gas prices over a set time utilizing the JSON file data, and more. 
