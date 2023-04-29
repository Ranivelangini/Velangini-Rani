# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
a=list(map(int,input().split()))
my_arr=np.array(a)
print(np.reshape(my_arr,(3,3)))
