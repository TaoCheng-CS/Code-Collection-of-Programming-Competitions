from sys import stdin


def change_state(index, not_same_index, same_index, ans):
    if same_index != None:
        x = same_index
        print(x + 1, flush=True)
        value = int(stdin.readline())
        if value != ans[x]:
            for i in range(index):
                ans[i] ^= 1
                ans[99 - i] ^= 1

    if not_same_index != None:
        x = not_same_index
        print(x + 1, flush=True)
        value = int(stdin.readline())
        if value != ans[x]:
            for i in range(index):
                ans[i], ans[99 - i] = ans[99 - i], ans[i]

    # normalization
    if (same_index == None) or (not_same_index == None):
        print(1, flush=True)
        value = int(stdin.readline())


T, B = map(int, stdin.readline().split())

for _ in range(T):
    ans = [0 for i in range(B)]
    if B == 10:
        for i in range(10):
            print(i + 1, flush=True)
            value = int(stdin.readline())
            ans[i] = value
    elif B == 20:
        # inspect
        for i in range(10):
            print(i + 1, flush=True)
            value = int(stdin.readline())
            ans[i] = value

            print(20 - i, flush=True)
            value = int(stdin.readline())
            ans[19 - i] = value

        cur = []
        for i in range(10):
            print(i + 1, flush=True)
            value = int(stdin.readline())
            cur.append(value)

        for j in range(10):
            if (1 ^ cur[j]) == (ans[j] ^ ans[19 - j]):
                ans[j] = cur[j]
                ans[19 - j] = 1
            else:
                ans[j] = cur[j]
                ans[19 - j] = 0

    elif B == 100:

        not_same_index = None
        same_index = None
        num = 0
        for i in range(0, 50):
            print(i + 1, flush=True)
            value1 = int(stdin.readline())
            ans[i] = value1

            print(100 - i, flush=True)
            value2 = int(stdin.readline())
            ans[99 - i] = value2

            if value1 == value2:
                same_index = i
            else:
                not_same_index = i
            num += 2

            if num % 10 == 0:
                change_state(i + 1, not_same_index, same_index, ans)
                num += 2

    string = ""
    for item in ans:
        string += str(item)
    print(string, flush=True)

    # clean buffer
    re = stdin.readline()[:-1]
    assert (re == "Y")