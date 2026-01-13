# Ahead Subarrays

> Original problem: alice.io  
> (Problem statement reformatted into Markdown for readability)

---

## Problem

You are given two integer arrays **A** and **B**, each of length **N**.

You want to select one contiguous subarray of length **K** from each array in order to maximize the sum of the elements in the two chosen subarrays.  
However, the starting position of the subarray chosen from array A must be **strictly earlier** than the starting position of the subarray chosen from array B.

Formally, for integers a, b satisfying **1 ≤ a < b ≤ N−K+1** define

S(a,b) = \sum_{i=a}^{a+K-1} A_i + \sum_{i=b}^{b+K-1} B_i

Your task is to find the maximum possible value of S(a, b)

---

## (한국어 지문)

길이 **N**인 두 정수 수열 **A**, **B**가 주어진다.

당신은 각 수열에서 길이가 **K**인 연속 부분수열을 하나씩 선택하여, 두 부분수열에 포함된 원소들의 합을 최대화하고자 한다.  
단, 수열 A에서 선택한 부분수열의 시작 위치는 수열 B에서 선택한 부분수열의 시작 위치보다 **앞서야 한다**.

수식으로 표현하면, **1 ≤ a < b ≤ N−K+1**를 만족하는 정수 a, b에 대해

S(a,b) = \sum_{i=a}^{a+K-1} A_i + \sum_{i=b}^{b+K-1} B_i

로 정의할 때, S(a, b)의 최댓값을 구하여라.

---

## Input

1. The first line contains two integers **N** and **K**.
2. The second line contains N integers **A1, A2 ... AN**.
3. The third line contains N integers **B1, B2 ... BN**.

---

## Output

- Print a single integer: the maximum possible value of S(a, b) under the given conditions.

---

## Constraints

| Subtask | Points | Constraints |
|--------:|-------:|-------------|
| Subtask 1 | 40 | 2 ≤ N ≤ **100** |
| Subtask 2 | 40 | 2 ≤ N ≤ **3,000** |
| Subtask 3 | 20 | 2 ≤ N ≤ **100,000** |

For all subtasks, it is guaranteed that **1 ≤ K ≤ N−1**, so there always exists at least one valid choice of a and b.  
All values in arrays A and B are integers between **−1000** and **1000**, inclusive.

- **Time Limit:** 2 seconds  
- **Memory Limit:** 2048 MB  
- **Stack Memory Limit:** 256 MB  

---

## Example

### Input1

    4 2
    3 4 5 6
    10 1 1 1

### Output1

    11

In the example above, choosing a and b as illustrated yields the optimal result, and the value of S(a, b) is 4+5+1+1 = 11.  
This example satisfies the conditions of all subtasks.

---

### Input2

    2 1
    1 2
    3 4

### Output2

    5

This example satisfies the conditions of all subtasks.

---

### Input3

    6 3
    1 1 10 10 10 1
    -50 -50 -1 -1 -1 -50

### Output3

    18

This example satisfies the conditions of all subtasks.
