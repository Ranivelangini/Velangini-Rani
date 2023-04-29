# Enter your code here. Read input from STDIN. Print output to STDOUT
class OddStream():
    current = -1
    def get_next(self):
        self.current += 2
        return self.current
    
class EvenStream(OddStream):
    current = -2
    

def print_from_stream(n, stream=None):
    if not stream: stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())
        
        
N = int(input())
for _ in range(N):
    stream_name, n = input().split()
    
    if stream_name == 'odd':
        print_from_stream(int(n), OddStream())
    else:
        print_from_stream(int(n))
