# Segment Tree for Range Maximum and Count Queries

## Overview
This code implements a segment tree to efficiently answer range maximum queries (RMQ) along with the count of occurrences of the maximum value within the specified range. Each query returns two values: the maximum element in the range and the number of times it appears.
Another option allows you to find the maximum on a segment and change the element in the array

## Approach
- **Segment Tree Structure**: The tree is represented as an array where each node stores a tuple `(max_value, count)` and `max_value` in another variant. 
- **Tree Construction**: 
  - The tree is built in a bottom-up manner. Leaves correspond to elements of the input array, padded to the next power of two for a complete binary tree structure.
  - Internal nodes combine their children's values: if left and right max values are equal, their counts are summed; otherwise, the child with the higher max is chosen.
- **Query Handling**: 
  - Queries are processed recursively, checking segment overlap and combining results from left and right subtrees.

## Complexity
- **Time**:
  - Tree Construction: O(N)
  - Each Query: O(log N)
- **Space**: O(N) (allocates a tree of size ~4*N to handle padding for non-power-of-two sizes)

## Key Details
- **Indices**: Input queries use 1-based indexing, which are converted to 0-based in the code.
- **Padding**: If `N` is not a power of two, the tree is padded to the next power of two with `(-inf, 0)` values, ensuring a complete binary tree without affecting valid queries.
- **Efficiency**: The segment tree allows handling each query in logarithmic time, suitable for large input sizes.