import sys; input = sys.stdin.readline
MIS = lambda: map(int, input().split())
II = lambda: int(input())
IS = lambda: input().strip()
from collections import *
import random

def check(task, N): #데이터 형태 체크
    if not isinstance(N, int): return False
    if task == 1:
        if not 1 <= N <= 1000: return False
        return True
    if task == 2:
        if not 1 <= N <= int(1e6): return False
        return True
    
def solve(N):
    ret = 0
    n = N
    for i in range(2, N+1):
        while n%i == 0:
            ret += i
            n //= i
    return ret

def solve2(N):
    import math
    INF = int(2e18)

    arr = []
    for i in range(1, int(math.sqrt(N))+5):
        if i*i >= N:
            if i*i == N: arr.append(i)
            break
        if N%i == 0:
            arr.append(i)
            arr.append(N//i)
    arr.sort()

    L = len(arr)
    dp = [INF]*L
    dp[0] = 0

    for i in range(L):
        cur = arr[i]
        for j in range(i):
            pv = arr[j]
            if cur%pv != 0: continue
            dp[i] = min(dp[i], dp[j] + cur//pv)
    
    return dp[-1]

tccnt = [0] * 10
def write_file(sub, N): #파일 입출력

    assert check(sub, N)
    tccnt[sub] += 1
    tdx = tccnt[sub]

    fin = open(f"testcase/subtask{sub}-{tdx}.in", "w")
    fout = open(f"testcase/subtask{sub}-{tdx}.out", "w")

    fin.write(f"{N}\n")
    ans = solve(N)
    if True:
        ans2 = solve2(N)
        assert ans == ans2
    fout.write(f"{ans}\n")

if __name__ == "__main__":

    write_file(1, 1)
    write_file(1, 2)
    write_file(1, 3)
    write_file(1, 4)
    write_file(1, 5)
    write_file(1, 6)
    write_file(1, 8)
    write_file(1, 361)
    write_file(1, 512)
    write_file(1, 991)
    write_file(1, 1000)
    ## sub1

    write_file(2, 1001)
    write_file(2, 7*7*7*13*13*17)
    write_file(2, 2*2*3*3*5*5*991)
    write_file(2, 2*3*5*7*11*13*17)
    write_file(2, 65535)
    write_file(2, 65536)
    write_file(2, 991*991)
    write_file(2, 991*997)
    write_file(2, 999979)
    write_file(2, 999983)
    write_file(2, int(1e6))
    ## sub2

    #Author: Geunsoo Song (hulahula3247)
    #hulahula3247@gmail.com
   