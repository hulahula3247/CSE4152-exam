# 2 Keys Keyboard

> Original problem: alice.io  
> (Problem statement reformatted into Markdown for readability)

---

## Problem

Imagine a very simple text editor that supports exactly two operations:

- **Copy All**: Copy the entire current screen content into the clipboard.  
  (Partial copy is **not** allowed.)
- **Paste**: Paste the content from the clipboard onto the screen.

Initially, the screen contains a single character **A**.

Your goal is to display exactly **N** characters **A** on the screen using the minimum number of operations possible.  
Find the minimum number of operations required when acting optimally.

---

## Input

- The first line contains a single integer **N**, representing the number of characters **A** to be displayed.

---

## Output

- Print a single integer: the minimum number of operations required.

---

## Constraints

| Subtask | Points | Constraints |
|--------:|-------:|-------------|
| Subtask 1 | 80 | 1 ≤ N ≤ 1,000 |
| Subtask 2 | 20 | 1 ≤ N ≤ 1,000,000 |

- **Time Limit:** 2 seconds  
- **Memory Limit:** 2048 MB  
- **Stack Memory Limit:** 256 MB  

---

## Example 1

### Input

    9

### Output

    6

### Explanation

1. Copy `A`
2. Paste → `AA`
3. Paste → `AAA`
4. Copy `AAA`
5. Paste → `AAAAAA`
6. Paste → `AAAAAAAAA`

Total steps = **6**

---

## Example 2

### Input

    1

### Output

    0

---

## Notes

- There are no partial scores within a subtask.
- All test cases in a subtask must be passed to earn the points assigned to it.
- During judging, a single trailing space at the end of each line and a single newline character  
  at the end of the output are ignored (Baekjoon-style evaluation).

---
