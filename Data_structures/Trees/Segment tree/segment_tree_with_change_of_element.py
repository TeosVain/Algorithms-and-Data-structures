from math import log2, floor


def make_tree(N, numbers, LG):
    tree_list = [float('-inf')] * (2**LG-1+2**LG)
    for i in range(N):
        tree_list[i+2**LG-1] = numbers[i]
    for j in range(2**LG-2, -1, -1):
        if tree_list[j*2 + 1] > tree_list[j*2 + 2]:
            tree_list[j] = tree_list[j*2 + 1]
        elif tree_list[j*2 + 1] < tree_list[j*2 + 2]:
            tree_list[j] = tree_list[j*2 + 2]
        else:
            tree_list[j] = tree_list[j*2 + 1]
    return tree_list


def get_max(left_bound, right_bound, query_l, query_r, tree, node=0):
    if query_r < left_bound or right_bound < query_l:
        return float('-inf')

    if query_l <= left_bound and right_bound <= query_r:
        return tree[node]

    mid = (left_bound + right_bound) // 2
    left_max = get_max(left_bound, mid, query_l, query_r, tree, 2 * node + 1)
    right_max = get_max(mid+1, right_bound, query_l, query_r, tree, 2 * node + 2)
    return max(left_max, right_max)


def change_element(index, value, LG, tree):
    node = 2**LG-1+index-1
    tree[node] = value
    node = (node-1)//2
    while node >= 0:
        tree[node] = max(tree[node*2+1], tree[node*2+2])
        node = (node-1)//2



N = int(input())
numbers = list(map(int, input().split()))
LG = floor(log2(N))+1

tree = make_tree(N, numbers, LG)
answer = []

Q = int(input())
for i in range(Q):
    command, num1, num2 = input().split()
    if command == 's':
        answer.append(get_max(0, 2**LG-1, int(num1)-1, int(num2)-1, tree))
    else:
        change_element(int(num1), int(num2), LG, tree)

print(*answer)
