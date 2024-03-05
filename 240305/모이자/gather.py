import sys
N = int(sys.stdin.readline())
num_written = [int(x) for x in sys.stdin.readline().split()]

min = 10000000
curr = 0
for i in range(N) : 
    sums = 0
    for j in range(N) : 
        sums += abs(j-i)*num_written[j]
    if min > sums : 
        min=sums

print(min)