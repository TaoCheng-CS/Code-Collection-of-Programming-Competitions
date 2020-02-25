from sys import stdin
A=int(stdin.readline())
for i in range(A):
    a,b=list(map(int,stdin.readline().split(" ")))
    if a==b:
        print("0")
    elif a<b:
        if (b-a)%2==1:
            print("1")
        else:
            print("2")
    else:
        if (a-b)%2==1:
            print("2")
        else:
            print("1")