# [Number of Distinct Islands](https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1)
## Medium
Given a grid grid[][] of size n × m, consisting of characters 'L' and 'W', where 'L' represents Land and 'W' represents Water, find the number of distinct islands in the grid. An island is a group of one or more land cells connected horizontally or vertically.

Two islands are considered distinct if their shapes are different.
Two islands have the same shape if one can be translated to match the other exactly. Rotation and reflection are not allowed.

Examples :
Input: grid[][] = [['L', 'W', 'W'], ['W', 'W', 'L'], ['L', 'W', 'W']]Output: 1
Explanation: The grid contains three islands. All these islands have the same shape (a 1 × 1 block of land), so they are counted as a single distinct island. 
Input: grid[][] = [['L', 'L', 'W', 'L', 'L'], ['L', 'W', 'W', 'W', 'W'], ['W', 'W', 'L', 'W', 'L'], ['L', 'W', 'W', 'L', 'L']]Output: 4
Explanation: There are five islands in the grid. Two islands have the same shape (a 1 × 1 block of land), while the other three have different shapes. Therefore, the number of distinct island shapes is 4.

Constraints:1 ≤ n, m ≤ 500grid[i][j] == L or grid[i][j] == W