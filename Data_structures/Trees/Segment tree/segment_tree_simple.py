from math import log2, floor


'''
A tree of segments that allows you to quickly find out
the maximum and the number of maxima on a segment.
'''
def build_tree(N, log2ofN):
    tree_list = [(float('-inf'), 0)] * (2**log2ofN-1+2**log2ofN)
    for i in range(N):
        tree_list[i+2**log2ofN-1] = (numbers[i], 1)
    for j in range(2**log2ofN-2, -1, -1):
        if tree_list[j*2 + 1][0] > tree_list[j*2 + 2][0]:
            tree_list[j] = tree_list[j*2 + 1]
        elif tree_list[j*2 + 1][0] < tree_list[j*2 + 2][0]:
            tree_list[j] = tree_list[j*2 + 2]
        else:
            tree_list[j] = (
                tree_list[j*2 + 1][0], tree_list[j*2+1][1]+tree_list[j*2+2][1]
            )
    return tree_list


def get_max(left_bound, right_bound, query_l, query_r, node=0):
    if query_r < left_bound or right_bound < query_l:
        return (float('-inf'), 0)
    
    if query_l <= left_bound and right_bound <= query_r:
        return tree_list[node]
    
    mid = (left_bound + right_bound) // 2
    left_max = get_max(left_bound, mid, query_l, query_r, 2 * node + 1)
    right_max = get_max(mid+1, right_bound, query_l, query_r, 2 * node + 2)
    if left_max[0] > right_max[0]:
        return left_max
    elif left_max[0] < right_max[0]:
        return right_max
    else:
        return (left_max[0], right_max[1]+left_max[1])


N = int(input())
numbers = list(map(int, input().split()))

log2ofN = floor(log2(N))+1
tree_list = build_tree(N, log2ofN)

requests = int(input())

for _ in range(requests):
    left, right = map(int, input().split())
    print(*get_max(0, 2**log2ofN-1, left-1, right-1))