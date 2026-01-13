import sys; input = sys.stdin.readline
MIS = lambda: map(int, input().split())
II = lambda: int(input())
IS = lambda: input().strip()
from collections import *
import random
M = 100

def check(task, N, Q, arr, query): #데이터 형태 체크
    if not isinstance(N, int): return False
    if not isinstance(Q, int): return False
    if len(arr) != N: return False
    for i in range(N):
        if len(arr[i]) != N: return False
        for j in range(N):
            if not isinstance(arr[i][j], int): return False
            if not 0 <= arr[i][j] <= M: return False
    if len(query) != Q: return False
    for i in range(Q):
        if len(query[i]) != 5: return False
        for j in range(5):
            if not isinstance(query[i][j], int): return False
        y1, x1, y2, x2, v = query[i]
        if y1 > y2 or x1 > x2: return False
        if not 1 <= y1 <= N: return False
        if not 1 <= x1 <= N: return False
        if not 1 <= y2 <= N: return False
        if not 1 <= x2 <= N: return False
        if not 0 <= v <= M: return False

    if not 1 <= N <= 1000: return False
    if task == 1:
        if not 1 <= Q <= 10: return False
        return True
    if task == 2:
        if not 1 <= Q <= 10000: return False
        return True
    if task == 3:
        if not 1 <= Q <= 200000: return False
        return True
    assert False

def solve(N, Q, arr, query):
    ans = [[0]*N for _ in range(N)]
    D = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans[i][j] = arr[i][j]

    for i in range(Q):
        r1, c1, r2, c2, v = query[i]
        r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1
        D[r1][c1] += v
        if c2 + 1 < N: D[r1][c2+1] -= v
        if r2 + 1 < N: D[r2+1][c1] -= v
        if r2 + 1 < N and c2 + 1 < N: D[r2+1][c2+1] += v

    for i in range(N):
        for j in range(1, N):
            D[i][j] += D[i][j-1]

    for j in range(N):
        for i in range(1, N):
            D[i][j] += D[i-1][j]

    for i in range(N):
        for j in range(N):
            ans[i][j] = arr[i][j] + D[i][j]
    return ans

def solve2(N, Q, arr, query):
    ans = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans[i][j] = arr[i][j]

    for r1, c1, r2, c2, v in query:
        for i in range(r1-1, r2):
            for j in range(c1-1, c2):
                ans[i][j] += v
    
    return ans

tccnt = [0] * 10
def write_file(sub, N, Q, arr, query): #파일 입출력

    assert check(sub, N, Q, arr, query)
    tccnt[sub] += 1
    tdx = tccnt[sub]

    fin = open(f"testcase/subtask{sub}-{tdx}.in", "w")
    fout = open(f"testcase/subtask{sub}-{tdx}.out", "w")

    fin.write(f"{N} {Q}\n")
    for i in range(N):
        for j in range(N-1):
            fin.write(f"{arr[i][j]} ")
        fin.write(f"{arr[i][-1]}\n")
    for i in range(Q):
        for j in range(4):
            fin.write(f"{query[i][j]} ")
        fin.write(f"{query[i][-1]}\n")

    ans = solve(N, Q, arr, query)
    if sub == 1:
        ans2 = solve2(N, Q, arr, query)
        assert ans == ans2

    for i in range(N):
        for j in range(N-1):
            fout.write(f"{ans[i][j]} ")
        fout.write(f"{ans[i][-1]}\n")

    fin.close()
    fout.close()

def random_data(N, Q):
    arr = [[random.randint(0, M) for _ in range(N)] for _ in range(N)]
    query = []
    for i in range(Q):
        x1 = random.randint(1, N)
        x2 = random.randint(1, N)
        y1 = random.randint(1, N)
        y2 = random.randint(1, N)
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        v = random.randint(0, M)
        query.append((y1, x1, y2, x2, v))
    return N, Q, arr, query

def max_data(N, Q):
    arr = [[random.randint(M-5, M) for _ in range(N)] for _ in range(N)]
    query = []
    for i in range(Q):
        x1 = random.randint(1, 5)
        x2 = random.randint(N-5, N)
        y1 = random.randint(1, 5)
        y2 = random.randint(N-5, N)
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        v = random.randint(M-5, M)
        query.append((y1, x1, y2, x2, v))
    return N, Q, arr, query

ex1 = [4, 2,
       [[0, 0, 0, 5],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],

        [[1, 1, 3, 2, 1],
         [2, 2, 4, 4, 2]]]

ex2 = [1, 1,
       [[0]],

       [[1, 1, 1, 1, 0]]]

ex3 = [1, 2,
       [[1]],

       [[1, 1, 1, 1, 2],
        [1, 1, 1, 1, 2]]]

ex4 = [2, 5,
       [[1, 2],
        [3, 4]],
        
        [[1, 1, 1, 1, 1],
         [1, 2, 1, 2, 2],
         [2, 1, 2, 1, 3],
         [2, 2, 2, 2, 4],
         [1, 1, 2, 2, 100]]]

ex5 = [3, 6,
       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],
        
        [[1, 1, 1, 3, 1],
         [1, 1, 3, 1, 2],
         [3, 1, 3, 3, 3],
         [1, 3, 3, 3, 4],
         [1, 1, 3, 3, 100],
         [2, 2, 2, 2, 5]]]


if __name__ == "__main__":

    write_file(1, *ex1)
    write_file(1, *ex2)
    write_file(1, *ex3)
    write_file(1, *ex4)
    write_file(1, *ex5)

    write_file(1, *random_data(1, 10))
    write_file(1, *random_data(10, 10))
    write_file(1, *random_data(100, 10))
    write_file(1, *random_data(999, 9))
    write_file(1, *random_data(1000, 10))

    write_file(2, *random_data(999, 9999))
    write_file(2, *random_data(999, 10000))
    write_file(2, *random_data(1000, 9999))
    write_file(2, *random_data(1000, 10000))
    write_file(2, *max_data(1000, 10000))

    write_file(3, *random_data(999, 199999))
    write_file(3, *random_data(999, 200000))
    write_file(3, *random_data(1000, 199999))
    write_file(3, *random_data(1000, 200000))
    write_file(3, *max_data(1000, 200000))

    #Author: Geunsoo Song (hulahula3247)
    #hulahula3247@gmail.com