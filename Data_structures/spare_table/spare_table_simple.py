from math import log2, floor


N = int(input())
numbers = list(map(int, input().split()))
LG = floor(log2(N))

s_table = [[0] * N for _ in range(LG + 1)]

for i in range(N):
    s_table[0][i] = (numbers[i], i+1)

for i in range(1, LG+1):
    for j in range(N-(2**i) + 1):
        if s_table[i-1][j][0] >= s_table[i-1][j+2**(i-1)][0]:
            s_table[i][j] = s_table[i-1][j]
        elif s_table[i-1][j][0] < s_table[i-1][j+2**(i-1)][0]:
            s_table[i][j] = s_table[i-1][j+2**(i-1)]



Q = int(input())
for k in range(Q):
    r, l = map(int, input().split())
    long = l - r + 1
    LGQ = floor(log2(long))
    print(max(s_table[LGQ][r-1], s_table[LGQ][l-2**LGQ], key=lambda x: x[0])[1])