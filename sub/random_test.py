#!/bin/python

#import random
import random
arr=[]
t=0
while t<5000:
    arr.append(1)
    t=t+1

while t<10000:
    arr.append(2)
    t=t+1

#print arr
random.shuffle(arr)

print arr
