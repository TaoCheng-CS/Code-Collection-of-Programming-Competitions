from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
A.sort(reverse=True)

sum_value = 0
for i in range(int(len(A) / 3)):
    sum_value += A[i * 3]
    sum_value += A[i * 3 + 1]

index = int(len(A) / 3) * 3

sum_value += sum(A[index:])

print(sum_value)