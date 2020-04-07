from sys import stdin
import math
t = int(stdin.readline())


# depth_dic = {}
# depth_dic[0] = {0:1}
# depth_dic[1] = {0:1}
# for i in range(2, 50):
#     depth_dic[i]={}
#     for j in range(0, int((i-1)/2)+1):
#         dict1 = depth_dic[j]
#         dict2 = depth_dic[i - 1 - j]

#         for value1 in dict1:
#             for value2 in dict2:
#                 sum_value = value1 + value2 + i - 1
#                 depth_dic[i][sum_value] = 1
# print("Finished")

depth_dic = {}
depth_dic[0] = (0, 0)
depth_dic[1] = (0, 0)

item = 1
time=2
for i in range(2, 5000 + 1):
    left_last_value, right_last_value = depth_dic[i - 1]

    right_value = right_last_value + i - 1
    if time > 0:
        time -= 1
    else:
        item += 1
        time = math.pow(2, item) - 1
    left_value = left_last_value + item
    depth_dic[i] = (left_value, right_value)


for _ in range(t):
    n, d = list(map(int, stdin.readline().split(" ")))

    left_bond, right_bond = depth_dic[n]
    if d < left_bond or d > right_bond:
        print("NO")
    else:
        print("YES")
        