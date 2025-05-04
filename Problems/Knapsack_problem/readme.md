# 0/1 Knapsack Problem Solution with Reconstruction

## Description
This Python script solves the 0/1 knapsack problem, which aims to select items (tools) with maximum total value without exceeding a given capacity. The solution includes reconstructing the indices of the selected items.

## Input Format
- **Line 1**: Two integers: `tools` (number of items) and `capacity` (max weight allowed).
- **Line 2**: `tools` integers representing the weights (`numbers`) of each item.
- **Line 3**: `tools` integers representing the values (`prices`) of each item.

## Output Format
- A space-separated list of 1-based indices of selected items in ascending order. If no solution exists, an empty line is printed.

## Approach
1. **Dynamic Programming (DP)**: 
   - A 2D DP array tracks the maximum value achievable for each capacity and item subset.
   - Each entry stores a tuple `(total_price, last_item_index)` to enable backtracking.
2. **Backward Update**: For each item, capacities are updated in reverse to avoid overwriting.
3. **Reconstruction**: After finding the maximum value, backtrack using stored indices to collect selected items.
