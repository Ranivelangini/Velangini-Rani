# Enter your code here. Read input from STDIN. Print output to STDOUT
from numpy import array, transpose

arr = array([[int(x) for x in input().split()] for _ in range([int(x) for x in input().split()][0])])

print(transpose(arr), arr.flatten(), sep="\n")
