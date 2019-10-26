#Getting needed files
import math

import os

#Function to find total gallons of paint
def CalculateGallons(wallWidth, wallHeight, totalDoors):
    doorMeasurement = 14

    wallArea = wallWidth * wallHeight

    totalDoorsSquareFt = totalDoors * doorMeasurement

    totalWallArea = wallArea - totalDoorsSquareFt

    totalGallons = totalWallArea / 350

    return(totalGallons)

#Function to calculate price
def FindMyPrice(totalGallons, paintPrice):
    if totalGallons > 0:
        totalPrice = math.ceil(totalGallons) * paintPrice
        return(totalPrice)
    else:
        totalPrice = 0
        print('Error: Cannot have less than 0 gallons of paint')
        print('\n')
        return(totalPrice)

#Getting inputs
print('Please input the width of the wall you are painting:')
wallWidth = float(input())
print('\n')

print('Please input the height of the wall you are painting:')
wallHeight = float(input())
print('\n')

print('Please input the price of one gallon the paint you will be using:')
paintPrice = float(input())
print('\n')

print('Please input the number of doors on the wall:')
totalDoors = int(input())
print('\n')

#Calculating Paint Needed
totalGallons = CalculateGallons(wallWidth, wallHeight, totalDoors)

totalGallonsRounded = math.ceil(totalGallons)

#Calculate Price
totalPrice = FindMyPrice(totalGallons, paintPrice)

#Outputs
if totalPrice > 0:
    print('You will need %f gallons of paint for this job' %(totalGallons))
    print('\n')

    print('This can be done with %d gallon can(s)' %(totalGallonsRounded))
    print('\n')

    print('This will cost around', '$' + format(totalPrice, ',.2f'), 'dollars')

    os.system("PAUSE")
    
