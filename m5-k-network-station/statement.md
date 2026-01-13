# K Network Stations

> Original problem: alice.io  
> (Problem statement reformatted into Markdown for readability)

---

## Problem

The city of “문해프” consists of **N** buildings and **N−1** roads, forming a **tree** structure  
(i.e., every pair of buildings is connected by exactly one simple path, and there are no cycles).  
All roads are bidirectional and have their own lengths.

The newly appointed mayor plans to divide the city into **K** regions (**K is 1 or 2**) by removing **K−1** roads.  
(If **K = 1**, a single region covers the entire city.)  
Then, one Network Station will be built in each region to facilitate communication among the buildings within that region.

Each region contains multiple buildings (vertices). The **communication complexity** of a region is defined as:

- **sum(dist(a, b))** over every pair of buildings **(a, b)** within that region.

In other words, it is the **total sum of distances between all pairs of buildings in that region**.

The goal is to **minimize the maximum communication complexity** among all regions.  
Find the minimum possible value of this maximum communication complexity when the city is divided optimally.

---

## Input

1. The first line contains two integers **N** and **K**, the number of buildings and the number of regions.
2. Each of the next **N−1** lines contains three integers **aᵢ, bᵢ, cᵢ**, indicating a bidirectional road between buildings **aᵢ** and **bᵢ** with length **cᵢ**.

---

## Output

- Print a single integer: the minimum possible value of the maximum communication complexity among all regions.

---

## Constraints

| Subtask | Points | Constraints |
|--------:|-------:|-------------|
| Subtask 1 | 50 | 1 ≤ N ≤ 400; **K = 1** |
| Subtask 2 | 10 | 1 ≤ N ≤ 2,000; **K = 1** |
| Subtask 3 | 10 | 1 ≤ N ≤ 100,000; **K = 1** |
| Subtask 4 | 10 | K ≤ N ≤ 400; **K ∈ {1, 2}** |
| Subtask 5 | 10 | K ≤ N ≤ 2,000; **K ∈ {1, 2}** |
| Subtask 6 | 10 | K ≤ N ≤ 100,000; **K ∈ {1, 2}** |

For all subtasks:

- All **cᵢ** are integers between **1** and **100**, inclusive.
- The given graph forms a **tree**.

- **Time Limit:** 4 seconds  
- **Memory Limit:** 2048 MB  
- **Stack Memory Limit:** 256 MB  

---

## Examples

(Examples include figures on the original page.)

### Example 1

#### Input

    4 1
    2 1 1
    2 3 2
    2 4 4

#### Output

    21

Since **K = 1**, Region 1 represents the entire city. The communication complexity of Region 1 is:

- dist(1, 2) + dist(1, 3) + dist(1, 4) + dist(2, 3) + dist(2, 4) + dist(3, 4)  
= 1 + 3 + 5 + 2 + 4 + 6  
= 21

This example satisfies the conditions of all subtasks.

---

### Example 2

#### Input

    5 2
    1 2 1
    1 3 2
    1 4 10
    4 5 3

#### Output

    6

In this example, dividing the regions as shown in the figure is optimal, and the answer is:

- max(communication complexity of Region 1, communication complexity of Region 2) = 6

This example satisfies the conditions of Subtask 4, 5, and 6.

---

### Example 3

#### Input

    1 1

#### Output

    0

The communication complexity of Region 1 is 0.

This example satisfies the conditions of all subtasks.

---

## Notes

- There are no partial scores within a subtask.
- You must pass all test cases in a subtask to earn the points assigned to it.

---
