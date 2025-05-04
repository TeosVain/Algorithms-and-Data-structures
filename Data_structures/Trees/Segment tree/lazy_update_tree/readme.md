# Segment Tree with Lazy Propagation for Range Updates and Maximum Queries

## Overview  
This code implements a segment tree with lazy propagation to efficiently handle **range addition updates** and **range maximum queries**. It supports two operations:  
1. Add a value to all elements in a specified range.  
2. Find the maximum value in a specified range.  

## Approach  
- **Segment Tree with Lazy Propagation**:  
  - Each node stores a tuple `(current_max, lazy_value)`.  
  - **Lazy Propagation**: Delays propagating updates to child nodes until necessary (during queries or subsequent updates), reducing redundant operations.  
- **Tree Construction**:  
  - Built to the next power of two for a complete binary tree structure. Leaf nodes represent the input elements; internal nodes store the maximum of their children.  
- **Range Updates**:  
  - Apply an addition to a range. Pending updates are tracked via `lazy_value` and propagated when accessing child nodes.  
- **Range Queries**:  
  - Retrieve the maximum value in a range. Lazy values are propagated during traversal to ensure accurate results.  

## Input Format  
- **First line**: Integer `N` (number of elements in the array).  
- **Second line**: `N` space-separated integers (the initial array).  
- **Third line**: Integer `Q` (number of queries).  
- **Next `Q` lines**:  
  - **Update Query**: `add l r value` – Add `value` to all elements in the 1-based range `[l, r]`.  
  - **Max Query**: `m l r` – Output the maximum value in the 1-based range `[l, r]`.  

## Output Format  
For each `m` query, the maximum value in the specified range. All results are printed space-separated after processing all queries.  

## Complexity  
- **Time**:  
  - Tree Construction: *O(N)*  
  - Range Update/Query: *O(log N)* per operation.  
- **Space**: *O(2^LG)*, where `LG` is the smallest integer such that `2^LG ≥ N` (padded to the next power of two).  

## Key Details  
- **1-based Indexing**: Input ranges are converted to 0-based indices internally.  
- **Padding**: The tree is padded to the next power of two size, ensuring a complete binary tree structure. Unused leaves are initialized with `-inf` but do not affect valid queries.  
- **Lazy Propagation**: Ensures efficient updates by deferring operations until required, minimizing redundant calculations.  

## Example  
**Input**:  
```  
5  
1 3 2 5 4  
3  
m 1 5  
add 2 4 3  
m 1 5  
```  
**Output**:  
```  
5 8  
```  
**Explanation**:  
- Initial maximum in `[1,5]` is `5`.  
- After adding `3` to elements `[2,4]` (values become `[1,6,5,8,4]`), the new maximum is `8`.  

This implementation is optimal for scenarios requiring frequent range modifications and maximum queries over large datasets.