#distance between 2 cities
import string

import math
#from math import sqrt

#calculation based on coordinates
print('Find the distance between 2 cities  ')
units = int(input('Please specify a unit distance in KM '))
print('1 unit is ', units , 'KM')

print('For first city enter the details')
x = int(input('latitude (horizontal)'))
y = int(input('longitude (vertical) '))

print('For Second city enter the details')
x1 = int(input('latitude '))
y1= int(input('longitude '))

results = math.sqrt(((x-x1)**2) + ((y-y1)**2))
#results = sqrt(((x-x1)**2) + ((y-y1)**2))

print('the no of units between these cities is ', results)
k = (results * units)
m = k *0.62

print ('The distance in KM is  {}'.format(k))
print ('The distance in Miles is  ', m)



