# Neighbor’s Neighbor

> Original problem: alice.io  
> (Problem statement reformatted into Markdown for readability)

---

## Problem

An undirected graph with **N** vertices is given. Each vertex i has an integer value **Aᵢ**. The graph has **M** edges, and all edges have length 1.

You want to choose two **distinct** vertices a and b that satisfy the following condition:

- There exists **at least one path of length exactly 2** between vertices a and b.  
  Note that if a and b are directly connected by an edge (i.e., their shortest distance is 1), the condition is satisfied as long as there exists at least one path of length 2 between them.
- The definition of a path is as follows: A path is a sequence of vertices such that every two consecutive vertices are connected by an edge. The length of a path is the number of edges it uses. A path may contain the same vertex multiple times.

Among all pairs of vertices (a, b) that satisfy the condition, **find the minimum possible value of |Aₐ + A_b|**.  
In other words, choose two distinct vertices that share a common neighbor so that the absolute value of the sum of their weights is as small as possible.

---

## (한국어 지문)

정점의 개수가 **N**개인 무방향 그래프가 주어진다. 각 정점 i에는 정수 **Aᵢ**가 부여되어 있다. 그래프에는 **M**개의 간선이 있으며, 모든 간선의 길이는 1이다.

당신은 아래 조건을 만족하는 **서로 다른** 두 정점 a, b를 선택하려고 한다.

- 정점 a와 b 사이에 **길이가 정확히 2인 경로**가 하나 이상 존재한다.  
  a와 b가 직접 간선으로 연결되어 있더라도(최단 거리가 1이어도), 길이 2 경로가 하나라도 존재하면 조건을 만족한다.
- 경로의 정의는 다음과 같다: 경로란 정점들을 차례대로 나열한 것으로, 이웃한 두 정점 사이마다 간선이 있는 것을 말한다. 경로의 길이는 지나가는 간선의 개수이다. 한 경로에는 같은 정점이 반복해서 포함될 수 있다.

조건을 만족하는 모든 정점 쌍 (a, b)에 대해서 **|Aₐ + A_b|의 최솟값을 구하여라**.  
즉 서로 다른 두 정점의 가중치의 합의 절댓값이 최소가 되도록 하여라.

---

## Input

1. The first line contains two integers **N** and **M**, the number of vertices and the number of edges.
2. The second line contains N integers **A1, A2 ... AN**, where **Aᵢ** is the value of vertex i.
3. Each of the next **M** lines contains two integers **u** and **v** (1 ≤ u < v ≤ N), indicating an undirected edge between vertices u and v.

---

## Output

- Print a single integer: the minimum value of **|Aₐ + A_b|** among all pairs of distinct vertices (a, b) such that there exists at least one path of length exactly 2 between a and b. It is guaranteed that at least one such pair (a, b) exists.

---

## Constraints

| Subtask | Points | Constraints |
|--------:|-------:|-------------|
| Subtask 1 | 40 | 3 ≤ N ≤ **100** |
| Subtask 2 | 20 | 3 ≤ N ≤ **2,000** |
| Subtask 3 | 20 | 3 ≤ N ≤ **100,000**; In this subtask, **all Aᵢ satisfies 0 ≤ Aᵢ** |
| Subtask 4 | 20 | 3 ≤ N ≤ **100,000** |

For all subtasks:

- **M satisfies 2 ≤ M ≤ 2N**, and all **Aᵢ** are guaranteed to be integers between **−10⁹** and **10⁹**, inclusive.
- It is also guaranteed that the given graph is **connected** and contains **no multiple edges or self-loops**.

- **Time Limit:** 2 seconds  
- **Memory Limit:** 2048 MB  
- **Stack Memory Limit:** 256 MB  

---

## Example

### Input1

    3 2
    4 3 5
    1 3
    2 3

### Output1

    7

There is a path of length 2 between vertices (1, 2), namely 1-3-2. On the other hand, there is no path of length 2 between (1, 3) or (2, 3), so the only valid pair (a, b) is (1, 2). In this case, |Aₐ + A_b| = 7.  
This example satisfies the conditions of all subtasks.

---

### Input2

    3 3
    -4 -3 5
    1 2
    1 3
    2 3

### Output2

    1

In this example, all pairs (1, 2), (1, 3), and (2, 3) have a path of length 2: 1-3-2, 1-2-3, and 2-1-3, respectively. In this case, the pair (a, b) that minimizes the absolute value of the sum of their weights is (1, 3), and the minimum value is 1.  
This example satisfies the conditions of Subtask 1, 2, and 4.

---

### Input3

    4 4
    -3 2 -4 7
    1 2
    2 3
    3 4
    1 4

### Output3

    7

In this example, only the two pairs (1, 3) and (2, 4) have a path of length 2 between them.  
This example satisfies the conditions of Subtask 1, 2, and 4.
