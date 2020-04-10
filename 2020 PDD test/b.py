from sys import stdin

N, M = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

mod_dic = {0: 1}
for i in range(M):
    mod_dic[i + 1] = 0


sum = 0
num = 0

for item in A:
    sum += item
    sum %= M
    num += mod_dic[sum]
    mod_dic[sum] += 1

print(num)