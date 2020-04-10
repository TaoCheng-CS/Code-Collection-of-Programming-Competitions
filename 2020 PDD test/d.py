from sys import stdin

N, K = map(int, stdin.readline().split())
C = list(map(int, stdin.readline().split()))

dp = [[0 for i in range(N + 1)] for j in range(K + 1)]

dp[0][0] = 0
dp[0][1] = 1
for i in range(1, N + 1):
    if C[i - 1] == C[i - 2]:
        dp[0][i] = dp[0][i - 1] + 1
        if dp[0][i] >= N - K:
            print(N - K)
            exit()

    else:
        dp[0][i] = 1

for i in range(1, K + 1):
    dp[i][0] = 0
    dp[i][1] = 1
    for j in range(2, N + 1):
        dp[i][j] = 1
        for k in range(min(i + 1, j)):
            if C[j - 1] == C[j - k - 2]:
                dp[i][j] = max(dp[i][j], dp[i - k][j - k - 1] + 1)

print(max(dp[K]))
