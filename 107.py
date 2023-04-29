# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')

nxm = str(input())
n = int(nxm.split(' ')[0])
m = int(nxm.split(' ')[1])

print(numpy.eye(n, m, k = 0))
