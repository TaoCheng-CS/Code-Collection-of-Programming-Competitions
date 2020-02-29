from sys import stdin
 
def find_closest(x,y):
    first=int(y/x)*x
    second=first+x
    if abs(first-y)>abs(second-y):
        return abs(second-y),second
    else:
        return abs(first-y),first

t=int(stdin.readline())
 
for i in range(t):
    a,b,c=list(map(int,stdin.readline().split(" ")))
    A=-1 
    B=-1
    C=-1
    ans=1000000000
    for cA in range(1,2*a+1):
        for cB in range(cA,2*b+1,cA):
            res,cC=find_closest(cB,c)
            if res+abs(cA-a)+abs(cB-b)<ans:
                ans=res+abs(cA-a)+abs(cB-b)
                A=cA
                B=cB
                C=cC
    print(str(ans))
    print(str(A)+" "+str(B)+" "+str(C))