# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
english=set(map(int,input().split()))

b=int(input())
french=set(map(int,input().split()))

    
common_students=english.difference(french)

print(len(common_students))
