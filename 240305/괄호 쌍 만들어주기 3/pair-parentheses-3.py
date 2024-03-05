import sys
paranthesis = sys.stdin.readline()
cnt = 0
for i in range(len(paranthesis)) : 
    if paranthesis[i] == '(' : 
        for j in range(i+1, len(paranthesis)) :
            if paranthesis[j] == ')' : 
                cnt+=1

print(cnt)