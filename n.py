#andrew math
import math

print('The nth roots of i...')

n = input('Enter your value for n: ')

nRoots = []
number = 0
print(n)
while number < int(n):
    x = number
    xComponentOfnRootOnGrid = cos((pi/(2*n)) + ((2*pi*x)/n))
    yComponentOfnRootOnGrid = sin((pi/(2*n)) + ((2*pi*x)/n))
    nRoot = str(xComponentOfnRootOnGrid) + ' + ' + str(yComponentOfnRootOnGrid) + 'i'
    nRoots.append(nRoot)
    number += 1
    print('here')


print('These are the ' + str(n) + ' roots of i...')
for key in nRoots:
    print(key + '\n')
