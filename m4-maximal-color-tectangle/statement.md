# Maximal Color Rectangle

> Original problem: alice.io  
> (Problem statement reformatted into Markdown for readability)

---

## Problem

You are given an **N × N** grid **A** where each cell contains an integer color ID **Aᵢⱼ**.

Your task is to find the **largest axis-aligned rectangle** whose cells all have the **same color**, and report its **area**.

- The rectangle must be **axis-aligned**.
- The rectangle must be **contiguous** in rows and columns.

(See the original page for the figure; in the shown example, the maximal area is **6**.)

---

## Input

1. The first line contains a single integer **N**, representing the size of the grid **A**.
2. The next **N** lines each contain **N** integers; each integer denotes the color ID **Aᵢⱼ**.

---

## Output

- Print a single integer: the maximal area satisfying the problem’s conditions.

---

## Constraints

| Subtask | Points | Constraints |
|--------:|-------:|-------------|
| Subtask 1 | 40 | 1 ≤ N ≤ 10; all color IDs **Aᵢⱼ** are either **0** or **1** |
| Subtask 2 | 15 | 1 ≤ N ≤ 2,000; all color IDs **Aᵢⱼ** are either **0** or **1** |
| Subtask 3 | 15 | 1 ≤ N ≤ 80; -10^6 ≤ **Aᵢⱼ** ≤ 10^6 |
| Subtask 4 | 15 | 1 ≤ N ≤ 400; -10^6 ≤ **Aᵢⱼ** ≤ 10^6 |
| Subtask 5 | 15 | 1 ≤ N ≤ 2,000; -10^6 ≤ **Aᵢⱼ** ≤ 10^6 |

- **Time Limit:** 3.5 seconds  
- **Memory Limit:** 2048 MB  
- **Stack Memory Limit:** 256 MB  

---

## Examples

(Examples include figures on the original page.)

### Example 1

#### Input

    4
    1 0 0 0
    1 0 1 0
    1 1 0 0
    0 1 1 0

#### Output

    4

This example satisfies the conditions of Subtask 1, 2, 3, 4 and 5.

---

### Example 2

#### Input

    4
    1 2 2 2
    1 2 2 2
    1 2 2 2
    3 3 0 -1

#### Output

    9

This example satisfies the conditions of Subtask 3, 4 and 5.

---

### Example 3

#### Input

    6
    1 1 2 2 2 4
    1 1 1 2 2 4
    3 1 1 2 2 2
    3 3 3 3 3 2
    4 4 4 4 4 4
    5 5 5 5 1 1

#### Output

    6

This example satisfies the conditions of Subtask 3, 4 and 5.

---

## Notes

- There are no partial scores within a subtask.
- You must pass all test cases in a subtask to earn the points assigned to it.

---
