tools, capacity = map(int, input().split())
numbers = list(map(int, input().split()))
prices = list(map(int, input().split()))
dp = [[-1] * (capacity+1)]
dp[0][0] = (0, 0)  # Tuple storage (price, index number).
for i in range(tools):  # Initialization of a two-dimensional array.
    for j in range(capacity-numbers[i], -1, -1):
        if dp[i][j] != -1:
            if dp[i][j+numbers[i]] == -1:
                dp[i][j+numbers[i]] = (dp[i][j][0] + prices[i], i)
            else:
                if dp[i][j][0] + prices[i] > dp[i][j+numbers[i]][0]:
                    dp[i][j+numbers[i]] = (dp[i][j][0] + prices[i], i)
    if i != tools-1:
        dp.append(dp[i].copy())
max_price = (0, 0)
weight = 0
for weight in range(len(dp[-1])):  # Search for maximum value.
    if dp[-1][weight] != -1:
        if max_price[0] <= dp[-1][weight][0]:
            max_price = dp[-1][weight]
            weight = weight
if max_price == (0, 0):
    print('')
else:
    answer = []
    tool = max_price[1]
    answer.append(tool + 1)
    weight -= numbers[tool]
    while weight > 0:  # Restore the answer by moving backwards through the indices.
        tool = dp[tool - 1][weight][1]
        answer.append(tool + 1)
        weight -= numbers[tool]
    answer.reverse()
    print(*answer)
