from sys import stdin
n=int(stdin.readline())
R=list(map(int,stdin.readline().split(" ")))
B=list(map(int,stdin.readline().split(" ")))
Bionic_win=0
Robo_win=0
for i in range(n):
    if R[i]==0 and B[i]==1:
        Bionic_win+=1
    elif R[i]==1 and B[i]==0:
        Robo_win+=1
if Robo_win==0:
    print("-1")
else:
    p=int(Bionic_win/Robo_win)
    print(str(p+1))
    