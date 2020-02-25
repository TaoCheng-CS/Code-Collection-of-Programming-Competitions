from sys import stdin
t=int(stdin.readline())

def alpha_add(cur_sum,string):
    for button in string:
        cur_sum[ord(button)-ord('a')]+=1

def add(a,b):
    for i in range(len(a)):
        b[i]+=a[i]

for i in range(t):
    n,m=list(map(int,stdin.readline().split(" ")))
    a=stdin.readline()[:-1]
    p=list(map(int,stdin.readline().split(" ")))
    
    sum=[0 for i in range(26)]
    cur_sum=[0 for i in range(26)]
    p.sort()
    p.append(n)
    last_stop=0
    for stop in p:
        alpha_add(cur_sum,a[last_stop:stop])
        add(cur_sum,sum)
        last_stop=stop
    for number in sum:
        print(str(number)+" ",end="")
    print("")