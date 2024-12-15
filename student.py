#Name: Leslie Paola Ramon I
#Email: leslie.ramon44@myhunter.cuny.edu
#Date: December 15, 2024
#This program animate hurricane data.

import turtle
import pandas as pd

def animate(t,lat,lon,wind):
    if wind > 157:
        category = "Category 5"
    elif 130 <= wind <= 156:
        category = "Category 4"
    elif 111 <= wind <= 129:
        category = "Category 3"
    elif 96 <= wind <= 110:
        category = "Category 2"
    elif 74 <= wind <= 95:
        category = "Category 1"
    else:
        category = "No Hurricane"
    
    return category
        
   

def main():
    data = input("Enter file name:")
    t,wn = setup("Hurricane Animation")
    hurricane = pd.read_csv(data)
    
    for index,row in hurricane.iterrows():
        lat = int(row["Lat"])
        lon = int(row["Lon"])
        wind = row["Wind"]

        category = animate(lat, lon, wind)
        
        print(f"Lat: {lat}, Lon: {lon}, Wind: {wind}, Category: {category}")


if __name__ == "__main__":
    main()
    
