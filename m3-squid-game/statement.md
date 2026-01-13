# Squid Game: Two Bridges

> Original problem: alice.io  
> (Problem statement reformatted into Markdown for readability)

---

## Problem

Sogang agent is participating in **“Squid Game: Two Bridges.”**

There are two parallel bridges, **A** and **B**, each consisting of **N** steps. Each step has a score.  
The player starts at the beginning and moves to the end for **N** rounds. The player can only move forward along the bridge.

In each round, the player can either:

1. jump to the next step on the same bridge without using any energy, or
2. spend one unit of energy to jump to the next step on the other bridge.

When the player lands on a step, the step’s score is added to the total.

Unlike the original *Squid Game*, there is no danger of dying in this version, and the agent will always finish the game.

Specifically, the agent starts on the starting point of the **left bridge (A)** with an initial score of **0** and initial energy **K**.

Given the score sequences **A** (left bridge) and **B** (right bridge), and the initial energy **K**, determine the **maximum score** the Sogang agent can achieve.

The agent does not have to use all of the energy — it is also possible to use none at all.

---

## Input

1. The first line contains two integers **N** and **K**, the number of turns and the agent’s initial energy.
2. The second line contains **N** integers, representing the left bridge's score sequence **A**.
3. The third line contains **N** integers, representing the right bridge's score sequence **B**.

---

## Output

- Print a single integer: the maximum score the Sogang agent can achieve.

---

## Constraints

| Subtask | Points | Constraints |
|--------:|-------:|-------------|
| Subtask 1 | 40 | 1 ≤ N ≤ 1,000; K = 2; all Aᵢ = 0 |
| Subtask 2 | 20 | 1 ≤ N ≤ 100,000; K = 2; all Aᵢ = 0 |
| Subtask 3 | 20 | 1 ≤ N ≤ 100,000; 0 ≤ K ≤ 2 |
| Subtask 4 | 20 | 1 ≤ N ≤ 100,000; 0 ≤ K ≤ 4 |

For all subtasks:

- All **Aᵢ** and **Bᵢ** are integers between **-1000** and **1000**, inclusive.

- **Time Limit:** 2 seconds  
- **Memory Limit:** 2048 MB  
- **Stack Memory Limit:** 256 MB  

---

## Examples

(Examples include figures on the original page.)

### Example 1

#### Input

    6 2
    0 0 0 0 0 0
    3 -9 5 -2 8 -5

#### Output

    11

T
