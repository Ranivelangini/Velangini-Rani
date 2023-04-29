# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

N, M, P = map(int, input().split())

firstList = []
secondList = []

for i in range(N):
    tempList = list(map(int, input().split()))
    firstList.append(tempList)

for i in range(M):
    tempList = list(map(int, input().split()))
    secondList.append(tempList)
    
array_1 = numpy.array(firstList)
array_2 = numpy.array(secondList)

print(numpy.concatenate((array_1,array_2), axis=0))
