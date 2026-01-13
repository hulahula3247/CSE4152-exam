# Playing with Music Boxes

> Original problem: alice.io  
> (Problem statement reformatted into Markdown for readability)

---

## Problem

Jieun wants to play a musical score of length **N** using **K** (K ≤ N) music boxes. The score is a string of length N consisting of digits from 0 to 9. She plans to divide the score into K non-empty consecutive segments and assign each segment to one music box.

Each music box can only play a digit pattern that is stored in it, repeated infinitely. For example, if a music box stores `"123"`, then it will play the sequence `"123123123..."`.

For each segment, the assigned part of the score must exactly match a prefix of the infinitely repeated sequence played by that music box.

For instance, suppose a music box is assigned the segment `"12121"`. Patterns such as `"12"`, `"1212"`, or `"12121"` can be stored in the box to reproduce this segment, because repeating them produces a sequence whose prefix matches `"12121"`. However, storing `"121"` would result in `"121121..."`, which does not match the given segment.

The length of a pattern is defined as the number of digits it contains. For example, `"12"` has length 2, and `"1171"` has length 4.

Jieun wants to divide the score into K segments and assign an appropriate pattern to each music box so that the entire score is played correctly. However, if a music box must store a pattern that is too long, it may break. Therefore, **she wants to minimize the maximum length of the patterns** stored in the music boxes.

Your task is to determine the minimum possible value of the maximum pattern length, over all valid ways to divide the score into K segments and assign patterns to the music boxes.

---

## (한국어 지문)

지은이는 길이가 N인 악보를 K(K ≤ N)개의 오르골로 연주하려고 한다. 악보는 0부터 9까지의 숫자로 이루어진 길이 N의 문자열이다. 지은이는 이 악보를 연속한 K개의 비어있지 않은 구간으로 분할하고, 각 구간을 하나의 오르골에 담당시키려고 한다.

각 오르골은 자신에게 저장된 digit 패턴을 무한히 반복하여 재생한다. 예를 들어, 오르골에 `"123"`이 저장되어 있다면 실제 연주는 `"123123123..."`와 같은 형태가 된다. 이 때, 각 구간의 악보는 그 오르골이 재생하는 무한 반복 문자열의 앞부분(prefix)과 정확히 일치해야 한다.

예를 들어, 어떤 오르골에 할당된 악보가 `"12121"`이라면, 이 오르골에는 `"12"`, `"1212"`, `"12121"`와 같은 패턴은 저장 가능하다. 그러나 `"121"`을 저장하면 실제 연주는 `"121121..."`이 되어 할당된 악보와 일치하지 않는다.

패턴의 길이란, 오르골에 저장되는 digit의 개수를 의미한다. 예를 들면 `"12"`는 패턴의 길이가 2고, `"1171"`은 패턴의 길이가 4이다.

지은이는 악보를 K개로 분할하고 각 오르골에 적절한 패턴을 저장하여 악보를 완벽하게 연주하고자 한다. 단, 오르골에 저장해야 하는 패턴의 길이가 너무 길면 고장이 날 수 있으므로, **저장하는 패턴 길이들의 최댓값을 가능한 한 최소화**하고자 한다.

당신의 임무는 악보를 적절히 K개로 분할하고, 각 오르골에 저장할 적절한 패턴을 정했을 때, 저장된 패턴 길이들 중 최댓값을 최소로 하는 값을 구하는 것이다.

---

## Input

1. The first line contains two integers **N** and **K**, where N is the length of the musical score and K is the number of music boxes.
2. The second line contains a string of length N consisting of **digits** from 0 to 9, representing the musical score.

---

## Output

- Print a single integer: the minimum possible value of the maximum pattern length stored in any music box when the score is divided into K segments and each segment is assigned an appropriate repeating pattern.

---

## Constraints

| Subtask | Points | Constraints |
|--------:|-------:|-------------|
| Subtask 1 | 20 | 1 ≤ N ≤ **100**, **K = 1** |
| Subtask 2 | 10 | 1 ≤ N ≤ **100**, **K = 2** |
| Subtask 3 | 10 | 1 ≤ N ≤ **100** |
| Subtask 4 | 10 | 1 ≤ N ≤ **2,000**, **K = 1** |
| Subtask 5 | 10 | 1 ≤ N ≤ **2,000**, **K = 2** |
| Subtask 6 | 10 | 1 ≤ N ≤ **2,000** |
| Subtask 7 | 10 | 1 ≤ N ≤ **100,000**, **K = 1** |
| Subtask 8 | 10 | 1 ≤ N ≤ **100,000**, **K = 2** |
| Subtask 9 | 10 | 1 ≤ N ≤ **100,000** |

For all subtasks:

- **K satisfies 1 ≤ K ≤ N**

- **Time Limit:** 2 seconds  
- **Memory Limit:** 2048 MB  
- **Stack Memory Limit:** 256 MB  

---

## Example

### Input1

    5 1
    12121

### Output1

    2

“The music box can store patterns like `"12"`, `"1212"`, or `"12121"`. In this case, the shortest pattern is `"12"`.”  
This example satisfies the conditions of Subtask 1, 3, 4, 6, 7 and 9.

---

### Input2

    10 2
    1231232132

### Output2

    3

In this example, the optimal way to split the sheet music is into `"12312"` and `"32132"`, and in that case, it is optimal to store `"123"` and `"321"` in each music box, respectively.

Another optimal way is to split it into `"123123"` and `"2132"`, and then store `"123"` and `"213"` in each music box, respectively.

This example satisfies the conditions of Subtask 2, 3, 5, 6, 8 and 9.

---

### Input3

    20 3
    12121200700700121212

### Output3

    3

In this example, the optimal way to split the sheet music is into `"121212"`, `"00700700"` and `"121212"`, and in that case, it is optimal to store `"12"`, `"007"` and `"12"` in each music box, respectively.

This example satisfies the conditions of Subtask 3, 6 and 9.

---

한 학기 동안 수고 많으셨습니다. 😊
