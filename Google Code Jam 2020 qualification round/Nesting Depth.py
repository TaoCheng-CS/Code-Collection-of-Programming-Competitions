from sys import stdin

T = int(stdin.readline())

for i in range(T):
    input = list(map(int, stdin.readline()[:-1]))
    string = ""
    for item in input:
        string += ("(" * item)
        string += str(item)
        string += (")" * item)

    while True:
        cur_string = string.replace(")(", "")
        if len(cur_string) == len(string):
            break
        string = cur_string

    print("Case #%d: %s" % (i + 1, string))