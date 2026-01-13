import sys; input = sys.stdin.readline
MIS = lambda: map(int, input().split())
II = lambda: int(input())
IS = lambda: input().strip()
from collections import *
import random
sys.setrecursionlimit(int(2e5))
M = 1000

def check(task, N, K, A, B):  # 데이터 형태 & 범위 체크
    # 타입 체크
    if not isinstance(task, int): 
        return False
    if not isinstance(N, int): 
        return False
    if not isinstance(K, int): 
        return False
    if not isinstance(A, list): 
        return False
    if not isinstance(B, list): 
        return False

    # 길이 체크
    if len(A) != N: 
        return False
    if len(B) != N: 
        return False

    # 기본 조건 체크
    if not (2 <= N <= 100_000):
        return False

    # 문제에서: 항상 K ≤ N-1 이고, 유효하려면 K ≥ 1이어야 함
    if not (1 <= K <= N - 1):
        return False

    # 값 범위 체크: -1000 ~ 1000
    for x in A:
        if not isinstance(x, int):
            return False
        if x < -1000 or x > 1000:
            return False

    for x in B:
        if not isinstance(x, int):
            return False
        if x < -1000 or x > 1000:
            return False

    # 서브태스크별 제한
    # task: 1, 2, 3 중 하나라고 가정
    if task == 1:
        # Subtask 1: 2 ≤ N ≤ 400
        if not (2 <= N <= 100):
            return False
    elif task == 2:
        # Subtask 2: 2 ≤ N ≤ 2,000
        if not (2 <= N <= 3000):
            return False
    elif task == 3:
        # Subtask 3: 2 ≤ N ≤ 100,000
        if not (2 <= N <= 100_000):
            return False
    else:
        return False

    return True

def solve(N, K, A, B):
    preA = [0]*(N+1)
    preB = [0]*(N+1)
    for i in range(N):
        preA[i+1] = preA[i] + A[i]
        preB[i+1] = preB[i] + B[i]

    # interval sums
    L = N-K+1
    A_sum = [0]*L
    B_sum = [0]*L
    for i in range(L):
        A_sum[i] = preA[i+K] - preA[i]
        B_sum[i] = preB[i+K] - preB[i]

    # prefix max of A_sum
    prefix = [0]*L
    prefix[0] = A_sum[0]
    for i in range(1, L):
        prefix[i] = max(prefix[i-1], A_sum[i])

    ans = -10**18
    # choose b >= 1
    for b in range(1, L):
        best_a = prefix[b-1]
        ans = max(ans, best_a + B_sum[b])
    return ans

def solve2(N, K, A, B):

    preA = [0]*(N+1)
    preB = [0]*(N+1)
    for i in range(N):
        preA[i+1] = preA[i] + A[i]
        preB[i+1] = preB[i] + B[i]

    ans = -int(1e18)
    for a in range(N-K+1):
        sumA = preA[a+K] - preA[a]
        for b in range(a+1, N-K+1):
            sumB = preB[b+K] - preB[b]
            ans = max(ans, sumA + sumB)
    return ans

def solve3(N, K, A, B):
    ans = -int(1e18)
    for a in range(N-K+1):
        for b in range(a+1, N-K+1):
            cur = 0
            for i in range(a, a+K):
                cur += A[i]
            for j in range(b, b+K):
                cur += B[j]
            ans = max(ans, cur)
    return ans

tccnt = [0] * 10
def write_file(N, K, A, B, sub=-1): #파일 입출력

    if N <= 100: sub = 1
    elif N <= 3000: sub = 2
    else: sub = 3

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
    if N <= 3000:
        assert ans == solve2(N, K, A, B)
    if N <= 100:
        assert ans == solve3(N, K, A, B)

    fout.write(f"{ans}\n")
    fin.close()
    fout.close()

ex1 = [4, 2, [3, 4, 5, 6], [10, 1, 1, 1]]
ex2 = [2, 1, [1, 2], [3, 4]]
ex3 = [6, 3, [1, 1, 10, 10, 10, 1], [-50, -50, -1, -1, -1, -50]]
ex4 = [2, 1, [0, 0], [0, 0]]
ex5 = [3, 2, [-M, -M, M], [M, -M, -M]]

def rd(N, l=-M, r=M):
    arr = [random.randint(l, r) for _ in range(N)]
    return arr

if __name__ == "__main__":

    random.seed(3247)

    write_file(*ex1)
    write_file(*ex2)
    write_file(*ex3)
    write_file(*ex4)
    write_file(*ex5)

    for n in [100, 3000, 100000]:
        write_file(n, n//2, rd(n), rd(n))
        write_file(n, n//2, rd(n), rd(n))
        write_file(n, n//2, rd(n, -10, 20), rd(n, -20, 10))
        write_file(n, n//2, rd(n, -1, 1), rd(n, -1, 1))
        write_file(n, n//2, rd(n, -50, 500), rd(n, 0, 0))
        write_file(n, n//2, rd(n, 0, 0), rd(n, -M, M))
        write_file(n, n//4, rd(n), rd(n))
        write_file(n, 3*n//4, rd(n), rd(n))
        write_file(n, n-1, rd(n, M, M), rd(n, M, M))
        write_file(n, n-1, rd(n, -M, -M), rd(n, -M, -M))
        write_file(n, 1, rd(n), rd(n))
        write_file(n, 2, rd(n), rd(n))
        write_file(n, n-2, rd(n), rd(n))
        write_file(n, n-1, rd(n), rd(n))
        write_file(n, n//2, rd(n, 0, M), rd(n, -M, 0))
        write_file(n, n//4, rd(n, 0, M), rd(n, -M, 0))
        write_file(n, 3*n//4, rd(n, 0, M), rd(n, -M, 0))
        write_file(n, n//2, rd(n, -M, 0), rd(n, 0, M))
        write_file(n, n//4, rd(n, -M, 0), rd(n, 0, M))
        write_file(n, 3*n//4, rd(n, -M, 0), rd(n, 0, M))