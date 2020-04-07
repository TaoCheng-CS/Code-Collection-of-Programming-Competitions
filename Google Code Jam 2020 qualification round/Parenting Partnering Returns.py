from sys import stdin


def sort_by_start(item):
    return item[0]


T = int(stdin.readline())
for i in range(T):
    N = int(stdin.readline())
    time_list = []
    act_dic = {}

    for j in range(N):
        start, end = map(int, stdin.readline().split())
        time_list.append((start, end, j))

    time_list.sort(key=sort_by_start)

    state = 1
    depend_dic = {}

    for j in range(N):
        a = time_list[j]
        a_index = a[2]
        depend_dic[a_index] = []
        for k in range(j):
            b = time_list[k]
            b_index = b[2]
            if b[1] > a[0]:
                depend_dic[a_index].append(b_index)
                depend_dic[b_index].append(a_index)

    state = 1
    choose = [-1 for i in range(N)]
    for j in range(N):
        if choose[j] == -1:
            choose[j] = 0
            candidate = depend_dic[j]
            value = 0
            while candidate and state == 1:
                # scan and judge
                cur = []
                for index in candidate:
                    if choose[index] == -1:
                        choose[index] = 1 - value
                        cur += depend_dic[index]

                    elif choose[index] == value:
                        state = -1
                        break
                candidate = cur
                value = 1 - value

            if state == -1:
                break

    if state == -1:
        print("Case #%d: %s" % (i + 1, "IMPOSSIBLE"))
    else:
        string = ""
        for item in choose:
            if item:
                string += "C"
            else:
                string += "J"
        print("Case #%d: %s" % (i + 1, string))