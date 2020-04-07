from sys import stdin


def cal_trace(mat, N):
    k = 0
    for i in range(N):
        k += mat[i][i]
    return k


def cal_row(mat, N):
    r = 0
    for row in mat:
        flag = [0 for i in range(N)]
        for item in row:
            flag[item - 1] += 1
            if flag[item - 1] > 1:
                r += 1
                break
    return r


def cal_col(mat, N):
    c = 0
    for i in range(N):
        flag = [0 for i in range(N)]
        for j in range(N):
            item = mat[j][i]
            flag[item - 1] += 1
            if flag[item - 1] > 1:
                c += 1
                break
    return c


T = int(stdin.readline())

for i in range(T):
    N = int(stdin.readline())
    mat = []
    for j in range(N):
        mat.append(list(map(int, stdin.readline().split())))

    k = cal_trace(mat, N)
    r = cal_row(mat, N)
    c = cal_col(mat, N)

    print("Case #%d: %d %d %d" % (i + 1, k, r, c))
