from math import floor, log2
'''
The second value in the node is a change promise marker,
the default value is set to zero. When elements change,
the value 0 is changed to the change value.
'''

def make_tree(N, numbers, LG):
    tree_list = [(float('-inf'), 0)] * (2**LG-1+2**LG)
    for i in range(N):
        tree_list[i+2**LG-1] = (numbers[i], 0)
    for j in range(2**LG-2, -1, -1):
        if tree_list[j*2 + 1][0] > tree_list[j*2 + 2][0]:
            tree_list[j] = (tree_list[j*2 + 1][0], 0)
        elif tree_list[j*2 + 1][0] < tree_list[j*2 + 2][0]:
            tree_list[j] = (tree_list[j*2 + 2][0], 0)
        else:
            tree_list[j] = (tree_list[j*2 + 1][0], 0)
    return tree_list


def change_elements(left_bound, right_bound, query_l, query_r, value, tree, node=0):
    if query_r < left_bound or right_bound < query_l:
        return tree[node][0]

    if query_l <= left_bound and right_bound <= query_r:
        tree[node] = (
            tree[node][0]+value, tree[node][1] if left_bound ==\
            right_bound else tree[node][1]+value
        )
        return tree[node][0]

    mid = (left_bound + right_bound) // 2

    if tree[node][1] != 0:
        tree[2*node+1] = (
            tree[2*node+1][0]+tree[node][1], 0 if left_bound + 1 ==\
            right_bound else tree[2*node+1][1]+tree[node][1]
        )
        tree[2*node+2] = (
            tree[2*node+2][0]+tree[node][1], 0 if left_bound + 1 ==\
            right_bound else tree[2*node+2][1]+tree[node][1]
        )
        tree[node] = (tree[node][0], 0) 

    left_max = change_elements(
        left_bound, mid, query_l, query_r, value, tree, 2 * node + 1
    )
    right_max = change_elements(
        mid+1, right_bound, query_l, query_r, value, tree, 2 * node + 2
    )
    tree[node] = (max(left_max, right_max), 0)
    return tree[node][0]


def get_max_element(left_bound, right_bound, query_l, query_r, tree, node=0):
    if query_r < left_bound or right_bound < query_l:
        return float('-inf')

    if query_l <= left_bound and right_bound <= query_r:
        return tree[node][0]

    if tree[node][1] != 0:
        tree[2*node+1] = (
            tree[2*node+1][0]+tree[node][1], 0 if left_bound + 1 ==\
            right_bound else tree[2*node+1][1]+tree[node][1]
        )
        tree[2*node+2] = (
            tree[2*node+2][0]+tree[node][1], 0 if left_bound + 1 ==\
            right_bound else tree[2*node+2][1]+tree[node][1]
        )
        tree[node] = (tree[node][0], 0)

    mid = (left_bound + right_bound) // 2
    left_max = get_max_element(
        left_bound, mid, query_l, query_r, tree, 2 * node + 1
    )
    right_max = get_max_element(
        mid+1, right_bound, query_l, query_r, tree, 2 * node + 2
    )
    return max(left_max, right_max)


N = int(input())
numbers = list(map(int, input().split()))
LG = log2(N)
if LG != floor(LG):
    LG = floor(LG) + 1
else:
    LG = floor(LG)

tree = make_tree(N, numbers, LG)
ans = []

Q = int(input())
for i in range(Q):
    command = input()
    if command[0] == 'm':
        com, l, r = command.split()
        ans.append(get_max_element(0, 2**LG-1, int(l)-1, int(r)-1, tree))
    else:
        com, l, r, value = command.split()
        change_elements(0, 2**LG-1, int(l)-1, int(r)-1, int(value), tree)
print(*ans)