#!/usr/bin/env python3
# Created by: Daniel I
# Created on: March 22, 2022
# This program asks the user for the radius of 
# a circle in mm. It then calculates and displays
# the area and circumference.
import math

def main():
    # input
    radius = int(input("Enter the radius of the circle (mm): "))
    
    # process
    area = math.pi*radius**2
    perimeter = 2*math.pi*radius

    # output
    print("")
    print ("Area = {} mm^2". format (area))
    print ("Perimeter = {} mm". format (perimeter))


if __name__ == "__main__":
  main()
  