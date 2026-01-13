# Matrix Addition

> Original problem: alice.io  
> (Problem statement reformatted into Markdown for readability)

---

## Problem

You are given an **N × N** matrix **A** initialized with arbitrary values.

You will receive **Q** operations, each defined by five integers **R1, C1, R2, C2, V**.  
For each operation, update the matrix by adding **V** to all elements in the submatrix with:

- rows **R1…R2**
- columns **C1…C2**

(Indices are 1-based, and 1 ≤ R1 ≤ R2 ≤ N, 1 ≤ C1 ≤ C2 ≤ N.)

---

## Input

1. The first line contains two integers **N** and **Q** — the matrix size and the number of operations.
2. The next **N** lines each contain **N** integers, forming the initial matrix **A**.
3. Each of the next **Q** lines contains five integers **R1, C1, R2, C2, V**, describing an operation to add **V** to every element in the submatrix with rows **R1…R2** and columns **C1…C2**.

---

## Output

Print the resulting matrix after performing all **Q** operations:

- **N** lines
- each line contains **N** integers separated by spaces

---

## Constraints

| Subtask | Points | Constraints |
|--------:|-------:|-------------|
| Subtask 1 | 60 | 1 ≤ N ≤ 1,000; 1 ≤ Q ≤ 10 |
| Subtask 2 | 20 | 1 ≤ N ≤ 1,000; 1 ≤ Q ≤ 10,000 |
| Subtask 3 | 20 | 1 ≤ N ≤ 1,000; 1 ≤ Q ≤ 200,000 |

For all subtasks:

- The initial matrix entries **Aij** and the update value **V** are integers between **0** and **100**, inclusive.

- **Time Limit:** 2 seconds  
- **Memory Limit:** 2048 MB  
- **Stack Memory Limit:** 256 MB  

---

## Example

### Input

    4 2
    0 0 0 5
    0 0 0 0
    0 0 0 0
    0 0 0 0
    1 1 3 2 1
    2 2 4 4 2

### Output

    1 1 0 5
    1 3 2 2
    1 3 2 2
    0 2 2 2

This example satisfies the conditions of Subtask 1, 2 and 3.

---

## Notes

- There are no partial scores within a subtask.
- You must pass all test cases in a subtask to earn the points assigned to it.

---
