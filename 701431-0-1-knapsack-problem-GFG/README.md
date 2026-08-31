# [0 - 1 Knapsack Problem](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1)
## Medium
Given two arrays,&nbsp;val[] and wt[], where each element represents the value and weight of an item respectively, and an integer&nbsp;W representing the maximum capacity of the knapsack (the total weight it can hold).
Put the items into the knapsack such that the total value obtained is maximum without exceeding the capacity W.
Note: You can either include an item completely or exclude it entirely — fractional selection of items is not allowed. Each item is available only once.
Examples :
Input: W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]Output: 3Explanation: Choose the last item, which weighs 1 unit and has a value of 3.
Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6] Output: 0Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Input: W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3] Output: 80Explanation: Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.
Constraints:1 ≤ val.size() = wt.size() ≤ 1031 ≤ W ≤ 1031 ≤ val[i] ≤ 1031 ≤ wt[i] ≤ 103