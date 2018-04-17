import os
import sys
import fileinput
import statistics

x_list = []
y_list = []

def inputData():
    fileName = input('Please input the name of the file: ')
    inputFile = open(fileName,'r+')
    with open(fileName,'r+') as inputFile:
        for line in inputFile:
            splitLine = line.split()
            x = float(splitLine[0])
            x_list.append(x)
            y = float(splitLine[1])
            y_list.append(y)
    return x_list , y_list
#input part

def mean(data):
    meanValue = statistics.mean(data)
    return meanValue
#mean value calculation

def stdDev(data):
    stdDev = (statistics.stdev(data))
    return stdDev
#standard deviation calculation

def CorCoe(x_list,y_list):
    Sx = stdDev(x_list)
    Sy = stdDev(y_list)
    length = len(y_list)
    avgX = mean(x_list)
    avgY = mean(y_list)
    sum_xy = 0
    for i in range (length):
       xi = x_list[i]
       yi = y_list[i]
       x = (xi - avgX)/Sx
       y = (yi - avgY)/Sy
       sum_xy += x*y
    r = sum_xy / (length-1)
    return r
#coefficient calculation

def slope():
    Sx = stdDev(x_list)
    Sy = stdDev(y_list)
    r = CorCoe(x_list,y_list)
    b = r*(Sy/Sx)
    return b

def intercept():
    avgX = mean(x_list)
    avgY = mean(y_list)
    b = slope()
    a = avgY - b*avgX
    return a

def Final():
    inputData()
    a = intercept()
    b = slope()
    print('Regression Line is: y = %.6f + %.6fx' % (a, b))

Final()

