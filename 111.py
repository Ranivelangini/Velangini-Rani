# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy


row, column = map(int, input().split(' '))

array = []

for i in range(row):
    array.append(list(map(int, input().split(' '))))
    
min_axis_one = numpy.min(array, axis = 1)

print(numpy.max(min_axis_one))
