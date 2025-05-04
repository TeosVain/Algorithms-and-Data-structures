tools, capacity = map(int, input().split())
weights = list(map(int, input().split()))
prices = list(map(int, input().split()))
dp = [-1] * (capacity+1)  # Initializing an array to count options.
dp[0] = 0
for i in range(tools):
    for j in range(capacity-weights[i], -1, -1):  # Mark possible options in reverse.
        if dp[j] != -1 and dp[j] + prices[i] > dp[j+weights[i]]:
            dp[j+weights[i]] = dp[j] + prices[i]
print(max(dp))
