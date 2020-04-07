from sys import stdin


def list2mat(N, list):
    mat = [[0 for _ in range(N)] for _ in range(N)]
    length = len(list)
    for i in range(length):
        mat[int(i / N)][i % N] = list[i]
    return (int(length / N), length % N), mat


def mat2list(mat):
    list = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 0:
                break
            list.append(mat[i][j])
    return mat


def generate_all_latin_squares(N, cur_List, store):
    if len(cur_List) == N * N:
        _, mat = list2mat(N, cur_List)
        store.append(mat)
        return

    else:
        (x, y), mat = list2mat(N, cur_List)
        candidate = [i + 1 for i in range(N)]
        for i in range(y):
            candidate[mat[x][i] - 1] = 0
        for i in range(x):
            candidate[mat[i][y] - 1] = 0
        for item in candidate:
            if item != 0:
                list = cur_List.copy()
                list.append(item)
                generate_all_latin_squares(N, list, store)


def generate_all_latin_squares_2(N, cur_List, store):
    if len(cur_List) == N * N:
        _, mat = list2mat(N, cur_List)
        store.append(mat)
        return

    else:
        # (x, y), mat = list2mat(N, cur_List)
        length = len(cur_List)
        x, y = (int(length / N), length % N)
        candidate = [i + 1 for i in range(N)]
        for i in range(y):
            candidate[cur_List[x * N + i] - 1] = 0
        for i in range(x):
            candidate[cur_List[i * N + y] - 1] = 0
        for item in candidate:
            if item != 0:
                list = cur_List.copy()
                list.append(item)
                generate_all_latin_squares(N, list, store)


def find_available(N, K):
    if (N, K) in value_dic:
        return value_dic[(N, K)]
    return None


value_dic = {(2, 2): [[1, 2], [2, 1]], (2, 4): [[2, 1], [1, 2]], (3, 6): [[3, 2, 1], [2, 1, 3], [1, 3, 2]], (3, 3): [[1, 3, 2], [2, 1, 3], [3, 2, 1]], (3, 9): [[3, 2, 1], [1, 3, 2], [2, 1, 3]], (4, 4): [[1, 4, 3, 2], [4, 1, 2, 3], [3, 2, 1, 4], [2, 3, 4, 1]], (4, 6): [[2, 4, 3, 1], [4, 1, 2, 3], [3, 2, 1, 4], [1, 3, 4, 2]], (4, 8): [[4, 3, 2, 1], [2, 1, 4, 3], [3, 2, 1, 4], [1, 4, 3, 2]], (4, 10): [[4, 3, 2, 1], [3, 1, 4, 2], [2, 4, 1, 3], [1, 2, 3, 4]], (4, 9): [[4, 3, 2, 1], [2, 1, 3, 4], [3, 4, 1, 2], [1, 2, 4, 3]], (4, 7): [[3, 4, 2, 1], [2, 1, 3, 4], [4, 2, 1, 3], [1, 3, 4, 2]], (4, 12): [[4, 3, 2, 1], [3, 2, 1, 4], [2, 1, 4, 3], [1, 4, 3, 2]], (4, 11): [[4, 3, 2, 1], [3, 1, 4, 2], [1, 2, 3, 4], [2, 4, 1, 3]], (4, 13): [[4, 3, 2, 1], [2, 4, 1, 3], [1, 2, 3, 4], [3, 1, 4, 2]], (4, 14): [[4, 3, 2, 1], [3, 4, 1, 2], [2, 1, 3, 4], [1, 2, 4, 3]], (4, 16): [[4, 3, 2, 1], [3, 4, 1, 2], [2, 1, 4, 3], [1, 2, 3, 4]], (5, 14): [[5, 4, 3, 2, 1], [4, 3, 2, 1, 5], [2, 5, 1, 4, 3], [1, 2, 5, 3, 4], [3, 1, 4, 5, 2]], (5, 10): [[5, 4, 3, 2, 1], [4, 1, 2, 5, 3], [3, 2, 1, 4, 5], [2, 3, 5, 1, 4], [1, 5, 4, 3, 2]], (5, 5): [[1, 5, 4, 3, 2], [5, 1, 3, 2, 4], [4, 2, 1, 5, 3], [3, 4, 2, 1, 5], [2, 3, 5, 4, 1]], (5, 8): [[3, 5, 4, 2, 1], [5, 1, 2, 4, 3], [4, 2, 1, 3, 5], [2, 3, 5, 1, 4], [1, 4, 3, 5, 2]], (5, 9): [[4, 5, 3, 2, 1], [5, 1, 2, 4, 3], [3, 2, 1, 5, 4], [2, 3, 4, 1, 5], [1, 4, 5, 3, 2]], (5, 15): [[5, 4, 3, 2, 1], [4, 3, 5, 1, 2], [3, 2, 1, 5, 4], [2, 1, 4, 3, 5], [1, 5, 2, 4, 3]], (5, 12): [[5, 4, 3, 2, 1], [4, 2, 1, 5, 3], [3, 1, 2, 4, 5], [2, 3, 5, 1, 4], [1, 5, 4, 3, 2]], (5, 11): [[5, 4, 3, 2, 1], [4, 1, 5, 3, 2], [3, 2, 1, 5, 4], [2, 3, 4, 1, 5], [1, 5, 2, 4, 3]], (5, 13): [[5, 4, 3, 2, 1], [4, 2, 5, 1, 3], [2, 3, 1, 4, 5], [1, 5, 2, 3, 4], [3, 1, 4, 5, 2]], (5, 16): [[5, 4, 3, 2, 1], [4, 5, 2, 1, 3], [3, 2, 1, 5, 4], [2, 1, 4, 3, 5], [1, 3, 5, 4, 2]], (5, 17): [[5, 4, 3, 2, 1], [4, 3, 5, 1, 2], [1, 5, 2, 4, 3], [2, 1, 4, 3, 5], [3, 2, 1, 5, 4]], (5, 18): [[5, 4, 3, 2, 1], [4, 3, 5, 1, 2], [3, 2, 1, 5, 4], [1, 5, 2, 4, 3], [2, 1, 4, 3, 5]], (5, 19): [[5, 4, 3, 2, 1], [4, 3, 5, 1, 2], [3, 1, 2, 5, 4], [2, 5, 1, 4, 3], [1, 2, 4, 3, 5]], (5, 20): [[5, 4, 3, 2, 1], [4, 5, 2, 1, 3], [3, 2, 1, 5, 4], [1, 3, 5, 4, 2], [2, 1, 4, 3, 5]], (5, 7): [[2, 5, 4, 3, 1], [5, 1, 3, 2, 4], [4, 2, 1, 5, 3], [3, 4, 2, 1, 5], [1, 3, 5, 4, 2]], (5, 21): [[5, 4, 3, 2, 1], [4, 5, 2, 1, 3], [2, 1, 5, 3, 4], [3, 2, 1, 4, 5], [1, 3, 4, 5, 2]], (5, 22): [[5, 4, 3, 2, 1], [4, 5, 2, 1, 3], [3, 1, 5, 4, 2], [1, 2, 4, 3, 5], [2, 3, 1, 5, 4]], (5, 23): [[5, 4, 3, 2, 1], [3, 5, 2, 1, 4], [2, 1, 4, 5, 3], [1, 3, 5, 4, 2], [4, 2, 1, 3, 5]], (5, 25): [[5, 4, 3, 2, 1], [4, 5, 2, 1, 3], [3, 1, 5, 4, 2], [2, 3, 1, 5, 4], [1, 2, 4, 3, 5]]}

T = int(stdin.readline())

for i in range(T):
    N, K = map(int, stdin.readline().split())
    mat = find_available(N, K)
    if not mat:
        print("Case #%d: %s" % (i + 1, "IMPOSSIBLE"))
    else:
        print("Case #%d: %s" % (i + 1, "POSSIBLE"))
        for i in range(N):
            for item in mat[i]:
                print(item, end=" ")
            print("")