from sys import stdin

def cmp(key):
    return a[key]

def judge(index_sort,origin_index,p):
    first=0
    second=0
    if index_sort<origin_index:
        first,second=index_sort+1,origin_index+1
    else:
        first,second=origin_index+1,index_sort+1
    while(first!=second):
        if first in p :
            first+=1
        else:
            return False
    
    return True


t=int(stdin.readline())

for i in range(t):
    n,m=list(map(int,stdin.readline().split(" ")))
    a=list(map(int,stdin.readline().split(" ")))
    p_list=list(map(int,stdin.readline().split(" ")))
    p={}
    for item in p_list:
        p[item]=1

    a_sort_index=[i for i in range(n)]
    a_sort_index.sort(key=cmp)

    state=1
    for i in range(n):
        index_sort=a_sort_index.index(i)
        if not judge(index_sort,i,p):
            state=0
            break
    if state==1:
        print("YES")
    else:
        print("NO")