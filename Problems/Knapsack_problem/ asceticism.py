'''One more variation for dp problem.'''
number_of_events, limit_of_change = map(int, input().split())
items = [0] * number_of_events
for i in range(number_of_events):
    name, value = input().split()
    items[i] = (name, int(value))
items.sort(key=lambda x: x[1])

max_force = items[-1][1]
dp = [float('inf')] * (max_force + 1)
dp[0] = 1
result_days = 0
last_ind = 0
names_list = []

for item in items:

    if item[1] <= limit_of_change:
        result_days += 1
        names_list.append(item[0])
        for dp_ind in range(min(last_ind, (len(dp)-item[1]-1)), -1, -1):
            if dp[dp_ind] != float('inf'):
                dp[dp_ind+item[1]] = dp[dp_ind] + 1
    elif (min_value := min(dp[item[1]-limit_of_change:item[1]])) != float('inf'):
        result_days += min_value
        names_list.append(item[0])
        for dp_ind in range(min(last_ind, (len(dp)-item[1]-1)), -1, -1):
            if dp[dp_ind] != float('inf'):
                dp[dp_ind+item[1]] = min(dp[dp_ind] + min_value, dp[dp_ind+item[1]])
    else:
        break
    last_ind += item[1]
print(len(names_list), result_days)
names_list.sort()
for line in names_list:
    print(line)