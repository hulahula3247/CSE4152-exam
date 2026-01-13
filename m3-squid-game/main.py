import sys; input = sys.stdin.readline
MIS = lambda: map(int, input().split())
II = lambda: int(input())
IS = lambda: input().strip()
from collections import *
import random
M = 1000
sys.setrecursionlimit(200005)

def check(task, N, K, A, B): #데이터 형태 체크
    if not isinstance(N, int): return False
    if not isinstance(K, int): return False
    if task == 1:
        if not 1 <= N <= 1000: return False
        if not K == 2: return False
    if task == 2:
        if not 1 <= N <= 100000: return False
        if not K == 2: return False
    if task == 3:
        if not 1 <= N <= 100000: return False
        if not 0 <= K <= 2: return False
    if task == 4:
        if not 1 <= N <= 100000: return False
        if not 0 <= K <= 4: return False
    if not len(A) == N: return False
    if not len(B) == N: return False
    for i in range(N):
        if not isinstance(A[i], int): return False
        if not isinstance(B[i], int): return False
        if task == 1 or task == 2:
            if not A[i] == 0: return False
        if not -M <= A[i] <= M: return False
        if not -M <= B[i] <= M: return False
    return True

def solve(N, K, A, B): #정해

    def re_dp(idx, k, fg):
        if idx == N: return 0
        if dp[idx][k][fg] != -INF: return dp[idx][k][fg]
        ret = -INF
        if k != 0: ret = max(ret, re_dp(idx, k-1, fg^1))
        if fg == 0: ret = max(ret, re_dp(idx+1, k, fg)+A[idx])
        else: ret = max(ret, re_dp(idx+1, k, fg)+B[idx])
        dp[idx][k][fg] = ret
        return ret

    INF = int(1e18)
    dp = [[[-INF]*2 for _ in range(K+1)] for _ in range(N+1)]
    return re_dp(0, K, 0)

def solve2(N, K, A, B): #검증용 naive
    assert K == 2
    pv = 0
    D = []
    for i in range(N):
        pv += A[i]
        D.append(B[i]-A[i])
    ans = 0; cur = 0
    for i in range(N):
        cur = max(cur+D[i], 0)
        ans = max(ans, cur)
    return pv+ans

tccnt = [0] * 10
def write_file(sub, N, K, A, B): #파일 입출력

    assert check(sub, N, K, A, B)
    tccnt[sub] += 1
    tdx = tccnt[sub]

    fin = open(f"testcase/subtask{sub}-{tdx}.in", "w")
    fout = open(f"testcase/subtask{sub}-{tdx}.out", "w")

    fin.write(f"{N} {K}\n")
    for i in range(N-1):
        fin.write(f"{A[i]} ")
    fin.write(f"{A[-1]}\n")
    for i in range(N-1):
        fin.write(f"{B[i]} ")
    fin.write(f"{B[-1]}\n")

    ans = solve(N, K, A, B)
    if K == 2:
        ans2 = solve2(N, K, A, B)
        assert ans == ans2

    fout.write(f"{ans}\n")

    fin.close()
    fout.close()

def make_random(N, K, a=True, b=True, rg=(-M, M)):
    A = [0]*N
    B = [0]*N
    if a: A = [random.randint(rg[0], rg[1]) for _ in range(N)]
    if b: B = [random.randint(rg[0], rg[1]) for _ in range(N)]
    return N, K, A, B

def sub1_zigzag(N, K, v1, v2):
    A = [0]*N
    B = [v1 if i%2 else v2 for i in range(N)]
    return N, K, A, B

def sub1_make_island(N, K, link=False):
    A = [0]*N
    B = [random.randint(-M, -1) for _ in range(N)]

    pv = random.randint(N//4, N//4*3)

    B[pv-5] = 200
    B[pv-4] = -1
    B[pv-3] = 3
    B[pv-2] = -1
    B[pv-1] = 200

    B[pv] = -402
    if link: B[pv] = -400

    B[pv+1] = 200
    B[pv+2] = -1
    B[pv+3] = 3
    B[pv+4] = -1
    B[pv+5] = 200

    return N, K, A, B


def zigzag(N, K, v1, v2, gap=2):
    A = [v2 if i%gap < gap//2  else v1 for i in range(N)]
    B = [v1 if i%gap >= gap//2 else v2 for i in range(N)]
    return N, K, A, B

def make_island(N, K, link=0, it=20):
    A = [random.randint(-500, 500) for _ in range(N)]
    D = [random.randint(-500, -1) for _ in range(N)]

    pv = random.randint(N//4, N//4*3)

    for i in range(1, it):
        pv = N//4 + i*6
        D[pv-5] = 200
        D[pv-4] = -1
        D[pv-3] = 3
        D[pv-2] = -1
        D[pv-1] = 200

        if link == 0: D[pv] = -402
        if link == 1: D[pv] = (-400 if i%10 else -407)
        if link == 2: D[pv] = (-400 if i%10 else -417)
        if link == 3: D[pv] = -400

    B = [A[i]+D[i] for i in range(N)]
    return N, K, A, B

def make_goodside(N, K, cent=0):
    A = [random.randint(-400, 400) for _ in range(N)]
    D = [1]*500 + [-1]*(N-1000) + [1]*500
    if cent == 1: D[N//2] = 499
    if cent == 2: D[N//2] = 501
    B = [A[i]+D[i] for i in range(N)]
    return N, K, A, B

ex11 = [6, 2, 
        [0, 0, 0, 0, 0, 0],
        [3, -9, 5, -2, 8, -5]]

ex12 = [6, 2, 
        [0, 0, 0, 0, 0, 0],
        [-1, -2, -1, -2, -1, -2]]

ex13 = [1, 2,
        [0],
        [1]]

ex14 = [1, 2,
        [0],
        [0]]

ex15 = [1, 2,
        [0],
        [-1]]

ex16 = [2, 2,
        [0, 0],
        [2, 2]]

ex17 = [2, 2,
        [0, 0],
        [2, -2]]

ex18 = [2, 2,
        [0, 0],
        [-2, 2]]

ex19 = [2, 2,
        [0, 0],
        [-2, -2]]

if __name__ == "__main__":

    random.seed(42)

    write_file(1, *ex11)
    write_file(1, *ex12)
    write_file(1, *ex13)
    write_file(1, *ex14)
    write_file(1, *ex15)
    write_file(1, *ex16)
    write_file(1, *ex17)
    write_file(1, *ex18)
    write_file(1, *ex19)

    N = 1000
    write_file(1, *make_random(N-1, 2, a=False))
    write_file(1, *make_random(N, 2, a=False))
    write_file(1, *make_random(N, 2, a=False))
    write_file(1, *make_random(N, 2, a=False))
    write_file(1, *make_random(N, 2, a=False))

    write_file(1, *make_random(N, 2, a=False, rg=(0, M)))
    write_file(1, *make_random(N, 2, a=False, rg=(-M, 0)))
    write_file(1, *make_random(N, 2, a=False, rg=(-M, 5)))
    write_file(1, *make_random(N, 2, a=False, rg=(-M//10, M)))
    write_file(1, *make_random(N, 2, a=False, rg=(-M, M//10)))
    write_file(1, *make_random(N, 2, a=False, rg=(-M, M//5)))
    write_file(1, *make_random(N, 2, a=False, rg=(-M, M//2)))

    write_file(1, *make_random(N, 2, a=False, rg=(-M, -M)))
    write_file(1, *make_random(N, 2, a=False, rg=(-M, -M+1)))
    write_file(1, *make_random(N, 2, a=False, rg=(0, 0)))
    write_file(1, *make_random(N, 2, a=False, rg=(M, M)))
    write_file(1, *make_random(N, 2, a=False, rg=(M-1, M)))
    write_file(1, *make_random(N, 2, a=False, rg=(-1, 1)))

    write_file(1, *sub1_zigzag(N, 2, -M, M))
    write_file(1, *sub1_zigzag(N, 2, 0, 1))
    write_file(1, *sub1_zigzag(N, 2, -1, 1))
    write_file(1, *sub1_make_island(N, 2, False))
    write_file(1, *sub1_make_island(N, 2, True))

    write_file(1, N, 2, [0]*N, [100, -1]*(N//4) + [-100, 1]*(N//4))
    write_file(1, N, 2, [0]*N, [-100, 1]*(N//4) + [100, -1]*(N//4))
    write_file(1, N, 2, [0]*N, [0]*(N-1)+[-1])
    #sub 1


    N = 100000
    write_file(2, *make_random(N-1, 2, a=False))
    write_file(2, *make_random(N, 2, a=False))
    write_file(2, *make_random(N, 2, a=False))
    write_file(2, *make_random(N, 2, a=False))
    write_file(2, *make_random(N, 2, a=False))

    write_file(2, *make_random(N, 2, a=False, rg=(0, M)))
    write_file(2, *make_random(N, 2, a=False, rg=(-M, 0)))
    write_file(2, *make_random(N, 2, a=False, rg=(-M, 5)))
    write_file(2, *make_random(N, 2, a=False, rg=(-M//10, M)))
    write_file(2, *make_random(N, 2, a=False, rg=(-M, M//10)))
    write_file(2, *make_random(N, 2, a=False, rg=(-M, M//5)))
    write_file(2, *make_random(N, 2, a=False, rg=(-M, M//2)))

    write_file(2, *make_random(N, 2, a=False, rg=(-M, -M)))
    write_file(2, *make_random(N, 2, a=False, rg=(-M, -M+1)))
    write_file(2, *make_random(N, 2, a=False, rg=(0, 0)))
    write_file(2, *make_random(N, 2, a=False, rg=(M, M)))
    write_file(2, *make_random(N, 2, a=False, rg=(M-1, M)))
    write_file(2, *make_random(N, 2, a=False, rg=(-1, 1)))

    write_file(2, *sub1_zigzag(N, 2, -M, M))
    write_file(2, *sub1_zigzag(N, 2, 0, 1))
    write_file(2, *sub1_zigzag(N, 2, -1, 1))
    write_file(2, *sub1_make_island(N, 2, False))
    write_file(2, *sub1_make_island(N, 2, True))

    write_file(2, N, 2, [0]*N, [100, -1]*(N//4) + [-100, 1]*(N//4))
    write_file(2, N, 2, [0]*N, [-100, 1]*(N//4) + [100, -1]*(N//4))
    write_file(2, N, 2, [0]*N, [0]*(N-1)+[-1])
    write_file(2, N, 2, [0]*N, [-1]*N)
    #sub2

    write_file(3, 6, 2, [3, 3, 3, 2, 1, 7], [1, 2, 1, 7, 7, 2])
    write_file(4, 6, 4, [1, 9, 0, 6, 6, 6], [9, 1, 9, 1, 7, 3])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 or j == 0: continue
            for k in [0, 1, 2, 3]:
                write_file((3 if k <= 2 else 4), 1, k, [5*i], [5*j])

    N = 100000

    write_file(3, N, 1, [0]*(N-1)+[-1], [0]*(N-1)+[-1])
    write_file(4, N, 4, [0]*(N-1)+[-1], [0]*(N-1)+[-1])

    for k in range(5):
        sub = (3 if k <= 2 else 4)
        write_file(sub, *make_random(2, k))
        write_file(sub, *make_random(3, k))
        write_file(sub, *make_random(4, k))
        write_file(sub, *make_random(5, k))
        write_file(sub, *make_random(N-1, k))
        write_file(sub, *make_random(N, k))
        if k == 1 or k == 3: write_file(sub, *make_random(N, k, rg=(-M, -M)))
        if k == 1 or k == 4: write_file(sub, *make_random(N, k, rg=(0, 0)))
        if k == 1 or k == 4: write_file(sub, *make_random(N, k, rg=(M, M)))

        if k == 0: continue

        write_file(sub, N, k, [-100, 1]*(N//4) + [100, -1]*(N//4), [100, -1]*(N//4) + [-100, 1]*(N//4))
        write_file(sub, N, k, [100, -1]*(N//4) + [-100, 1]*(N//4), [-100, 1]*(N//4) + [100, -1]*(N//4))
        write_file(sub, N, k, [999, -1]*(N//4) + [-111, 2]*(N//4), [1]*N)

        write_file(sub, *zigzag(N, k, -M+1, M, 2))
        write_file(sub, *zigzag(N, k, M, -M+1, 150))
        write_file(sub, *make_goodside(N, k, cent=0))
        write_file(sub, *make_goodside(N, k, cent=1))
        write_file(sub, *make_goodside(N, k, cent=2))

        if k == 1: continue

        write_file(sub, *make_island(N, k, it=20, link=0))
        write_file(sub, *make_island(N, k, it=10000, link=0))
        write_file(sub, *make_island(N, k, it=10000, link=1))
        write_file(sub, *make_island(N, k, it=10000, link=2))
        write_file(sub, *make_island(N, k, it=10000, link=3))


    #sub 3 and 4

    #Author: Geunsoo Song (hulahula3247)
    #hulahula3247@gmail.com