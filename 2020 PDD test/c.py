from sys import stdin
import copy


def cal_cost(number, index, K, string):
    if number[index] >= K:
        return 0, string

    else:
        cost = 0
        K -= number[index]
        for i in range(1, 10):
            if index + i < 10:
                num = min(K, number[index + i])
                string = string.replace(str(index + i), str(index), num)
                cost += (num * i)
                K -= num
            if index - i >= 0:
                num = min(K, number[index - i])
                string = string[::-1].replace(str(index - i), str(index), num)
                string = string[::-1]
                cost += (num * i)
                K -= num
            if K == 0:
                break
        return cost, string


def return_first_item(item):
    return item[0]


N, K = map(int, stdin.readline().split())

original_string = stdin.readline()[:-1]

number = [0 for i in range(10)]

for item in original_string:
    number[ord(item) - ord('0')] += 1

list = []

for i in range(10):
    cost, best_choice = cal_cost(number, i, K, copy.copy(original_string))
    list.append((cost, best_choice))

list.sort(key=return_first_item)

min_value, string = list[0]

for item in list:
    if item[0] > min_value:
        break
    string = min(string, item[1])

print(min_value)
print(string)