import os
import sys
import fileinput
import statistics

x1 = []
y1 = []

class Input:
    def __init__(self,name):
        self.name = name
        self.data = []
    def add(self,num):
        self.data.append(num)
        return self.data
def inputData():
    fileName = input('Please input the name of the file: ')
    inputFile = open(fileName,'r+')
    x_list = Input('x_list')
    y_list = Input('y_list')
    with open(fileName,'r+') as inputFile:
        for line in inputFile:
            splitLine = line.split()
            x = float(splitLine[0])
            x1 = x_list.add(x)
            y = float(splitLine[1])
            y1 = y_list.add(y)
    return x1 , y1
#input part

def mean(data):
    meanValue = statistics.mean(data)
    return meanValue
#mean value calculation

def stdDev(data):
    stdDev = (statistics.stdev(data))
    return stdDev
#standard deviation calculation

def CorCoe(x1,y1):
    Sx = stdDev(x1)
    Sy = stdDev(y1)
    length = len(y1)
    avgX = mean(x1)
    avgY = mean(y1)
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
    Sx = stdDev(x1)
    Sy = stdDev(y1)
    r = CorCoe(x1,y1)
    b = r*(Sy/Sx)
    return b

def intercept():
    avgX = mean(x1)
    avgY = mean(y1)
    b = slope()
    a = avgY - b*avgX
    return a

def Final():
    inputData()
    a = intercept()
    b = slope()
    print('Regression Line is: y = %.6f + %.6fx' % (a, b))

Final()

