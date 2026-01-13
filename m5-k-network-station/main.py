import sys; input = sys.stdin.readline
MIS = lambda: map(int, input().split())
II = lambda: int(input())
IS = lambda: input().strip()
from collections import *
import random
sys.setrecursionlimit(int(2e5))
import time
M = 100

def check(task, N, K, arr): #데이터 형태 체크

    def root(x):
        if pa[x] == x: return pa[x]
        pa[x] = root(pa[x]); return pa[x]
    
    def merge(x, y):
        x = root(x); y = root(y)
        if x != y: pa[y] = x

    if not isinstance(N, int): return False
    if not isinstance(K, int): return False
    if task == 1 or task == 2 or task == 3:
        if not K == 1: return False
    if task == 4 or task == 5 or task == 6:
        if not 1 <= K <= 2: return False
    if task == 1 or task == 4:
        if not K <= N <= 400: return False
    if task == 2 or task == 5:
        if not K <= N <= 2000: return False
    if task == 3 or task == 6:
        if not K <= N <= 100000: return False

    if not len(arr) == N-1: return False
    G = [[] for _ in range(N)]
    pa = [i for i in range(N)]
    s = set()

    mergecnt = 0
    for i in range(N-1):
        a, b, c = arr[i]
        if not isinstance(a, int): return False
        if not isinstance(b, int): return False
        if not isinstance(c, int): return False
        if not 1 <= a <= N: return False
        if not 1 <= b <= N: return False
        if not 1 <= c <= M: return False
        if a == b: return False
        a -= 1; b -= 1
        if a > b: a, b = b, a
        if (a, b) in s: return False
        s.add((a, b))
        G[a].append(b)
        G[b].append(a)
        
        if root(a) != root(b):
            mergecnt += 1
            merge(a, b)

    if mergecnt != N-1: return False
    return True

def solve(N, K, arr): #정해

    def tr_dp(cur):
        S, D, W = 1, 0, 0
        for nn, nd in G[cur]:
            if vst[nn]: continue
            vst[nn] = 1
            ss, dd, ww = tr_dp(nn)
            news = S+ss
            newd = D+dd+ss*nd
            neww = W+ww+D*ss+(dd+ss*nd)*S
            S, D, W = news, newd, neww
        return S, D, W
    
    def tr_dp2(a, b):
        key = dic[(a, b)]
        if dp[key][0] != -1: return dp[key]
        S, D, W = 1, 0, 0
        for nn, nd in G[b]:
            if nn == a: continue
            ss, dd, ww = tr_dp2(b, nn)
            news = S+ss
            newd = D+dd+ss*nd
            neww = W+ww+D*ss+(dd+ss*nd)*S
            S, D, W = news, newd, neww
        dp[key] = S, D, W
        return dp[key]

    G = [[] for _ in range(N)]
    kdx = 0
    dic = defaultdict(int)
    for a, b, c in arr:
        G[a-1].append((b-1, c))
        G[b-1].append((a-1, c))
        dic[(a-1, b-1)] = kdx; kdx += 1
        dic[(b-1, a-1)] = kdx; kdx += 1
    dp = [[-1]*3 for _ in range(kdx)]

    vst = [0]*N
    vst[0] = 1
    finalS, finalD, finalW = tr_dp(0)
    if K == 1:
        return finalW

    else:
        ans = int(1e18)
        pvt = 225

        for i in range(N):
            if len(G[i]) > pvt:
                S, D, W = 1, 0, 0
                for nn, nd in G[i]:
                    ss, dd, ww = tr_dp2(i, nn)
                    news = S+ss
                    newd = D+dd+ss*nd
                    neww = W+ww+D*ss+(dd+ss*nd)*S
                    S, D, W = news, newd, neww
                for nn, nd in G[i]:
                    ss, dd, ww = tr_dp2(i, nn)
                    saveS = S-ss
                    saveD = D-dd-ss*nd
                    saveW = W-ww-saveD*ss-(dd+ss*nd)*saveS
                    key = dic[(nn, i)]
                    dp[key] = [saveS, saveD, saveW]

        for a, b, c in arr:
            s1, d1, w1 = tr_dp2(a-1, b-1)
            s2, d2, w2 = tr_dp2(b-1, a-1)
            ans = min(ans, max(w1, w2))
        return ans

def solve2(N, K, arr): #검증용 naive
    G = [[] for _ in range(N)]
    for a, b, c in arr:
        G[a-1].append((b-1, c))
        G[b-1].append((a-1, c))

    if K == 1:
        ans = 0
        for i in range(N):
            que = deque()
            dis = [-1]*N
            dis[i] = 0
            que.append(i)
            while que:
                cur = que.popleft()
                for nn, nd in G[cur]:
                    if dis[nn] == -1:
                        dis[nn] = dis[cur]+nd
                        que.append(nn)
            ans += sum(dis)
        return ans//2
    
    if K == 2:
        ret = int(1e18)
        for i in range(N-1):
            a, b, c = arr[i]
            G[a-1].remove((b-1, c))
            G[b-1].remove((a-1, c))
            a1, a2 = 0, 0
            for j in range(N):
                que = deque()
                dis = [-1]*N
                dis[j] = 0
                que.append(j)
                while que:
                    cur = que.popleft()
                    for nn, nd in G[cur]:
                        if dis[nn] == -1:
                            dis[nn] = dis[cur]+nd
                            que.append(nn)
                if dis[0] == -1: 
                    for num in dis:
                        if num != -1: a1 += num
                else: 
                    for num in dis:
                        if num != -1: a2 += num
            ret = min(ret, max(a1, a2))
            G[a-1].append((b-1, c))
            G[b-1].append((a-1, c))
        return ret//2

tccnt = [0] * 10
def write_file(N, K, arr, sub=-1): #파일 입출력

    if sub == -1:
        sub = 0
        if K == 2: sub += 3
        if N <= 400: sub += 1
        elif N <= 2000: sub += 2
        elif N <= 100000: sub += 3
        else: sub += 4

    assert check(sub, N, K, arr)
    tccnt[sub] += 1
    tdx = tccnt[sub]

    fin = open(f"testcase/subtask{sub}-{tdx}.in", "w")
    fout = open(f"testcase/subtask{sub}-{tdx}.out", "w")

    fin.write(f"{N} {K}\n")
    for i in range(N-1):
        fin.write(f"{arr[i][0]} {arr[i][1]} {arr[i][2]}\n")

    t1 = time.perf_counter()
    ans = solve(N, K, arr)
    t2 = time.perf_counter()
    print(sub, tdx, t2-t1)

    if N <= 10:
        ans2 = solve2(N, K, arr)
        assert ans == ans2
    assert ans <= int(1e18)

    fout.write(f"{ans}\n")
    fin.close()
    fout.close()

def permute(arr):
    N = 0
    for a, b, c in arr:
        N = max(a, N)
        N = max(b, N)
    P = [i+1 for i in range(N)]
    random.shuffle(P)
    ret = []
    for a, b, c in arr:
        ret.append((P[a-1], P[b-1], c))
    return ret

def random_tree(N, l=1, r=M):
    ret = []
    for i in range(2, N+1):
        cur = random.randint(1, i-1)
        w   = random.randint(l, r)
        ret.append([cur, i, w])
    return ret

def long_tree(N, l=1, r=M, snipe=False):
    ret = []
    for i in range(2, N//2+1):
        w = random.randint(l, r)
        if snipe == True:
            if i < N//50: w = M
            else: w = 1
        ret.append([i-1, i, w])
    for i in range(N//2+1, N+1):
        w = random.randint(l, r)
        if snipe == True:
            w = 1
        cur = random.randint(N//2, i-1)
        ret.append([cur, i, w])
    return ret

def long_tree2(N, l=1, r=M, snipe=False):
    ret = []
    for i in range(N//10, 9*N//10+1):
        w = random.randint(l, r)
        if snipe == True:
            if i < N//10+N//50: w = M
            else: w = 1
        ret.append([i, i+1, w])
    for i in range(N//10-1, 11, -1):
        w = random.randint(l, r)
        if snipe == True:
            if i < N//10+N//50: w = M
            else: w = 1
        j = random.randint(i+1, N//10+5)
        ret.append([i, j, w])
    for i in range(9*N//10+2, N+1):
        w = random.randint(l, r)
        if snipe == True:
            if i < N//10+N//50: w = M
            else: w = 1
        j = random.randint(9*N//10-5, i-1)
        ret.append([i, j, w])
    for i in range(2, 12):
        j = random.randint(1, N)
        w = random.randint(l, r)
        ret.append([i, j, w])
    w = random.randint(l, r)
    ret.append([1, 2, w])
    return ret

def star_tree(N, l=1, r=M):
    ret = []
    for i in range(2, N//2):
        w = random.randint(l, r)
        ret.append([1, i, w])
    for i in range(N//2, N+1):
        cur = random.randint(1, i-1)
        w = random.randint(l, r)
        ret.append([cur, i, w])
    return ret

def line_tree(N, l=1, r=M):
    ret = []
    for i in range(N-1):
        w = random.randint(l, r)
        ret.append([i+1, i+2, w])
    return ret

def binary_tree(N, l=1, r=M):
    ret = []
    for i in range(2, N+1):
        w = random.randint(l, r)
        ret.append([i, i//2, w])
    return ret

def snipe_sqrt(N, pv, l=1, r=M):
    ret = []
    assert N >= 10000
    for i in range(1, N+1, pv):
        cur = i
        nxt = i+pv
        for j in range(cur+1, nxt):
            w = random.randint(l, r)
            if j <= N: ret.append([cur, j, w])
        w = random.randint(l, r)
        if nxt <= N: ret.append([cur, nxt, w])
    return ret

ex11 = [4, 1, 
       [[2, 1, 1],
        [2, 3, 2],
        [2, 4, 4]]]

ex12 = [1, 1, 
       []]

ex13 = [2, 1, 
       [[1, 2, 1]]]

ex14 = [2, 1, 
       [[1, 2, M]]]

ex15 = [3, 1, 
       [[1, 2, M],
       [2, 3, 1]]]

ex16 = [3, 1, 
       [[1, 2, M],
       [2, 3, M]]]

ex17 = [4, 1, 
       [[1, 2, M],
       [2, 3, M],
       [3, 4, M]]]

ex18 = [4, 1, 
       [[1, 2, 1],
       [2, 3, 1],
       [3, 4, M]]]

ex19 = [4, 1, 
       [[1, 2, 51],
       [2, 3, 50],
       [3, 4, M]]]

ex21 = [5, 2, 
        [[1, 2, 1],
         [1, 3, 2],
         [1, 4, 10],
         [4, 5, 3]]]

ex22 = [2, 2, 
        [[1, 2, 1]]]

ex23 = [2, 2, 
        [[1, 2, M]]]

ex24 = [4, 2,
        [[1, 2, 1],
         [2, 3, 1],
         [3, 4, 1]]]

ex25 = [3, 2, 
       [[1, 2, M],
       [2, 3, 1]]]

ex26 = [3, 2, 
       [[1, 2, M],
       [2, 3, M]]]

ex27 = [4, 2, 
       [[1, 2, M],
       [2, 3, M],
       [3, 4, M]]]

ex28 = [4, 2, 
       [[1, 2, 1],
       [2, 3, 1],
       [3, 4, M]]]

ex29 = [4, 2, 
       [[1, 2, 51],
       [2, 3, 50],
       [3, 4, M]]]

if __name__ == "__main__":

    random.seed(3247)

    write_file(*ex11)
    write_file(*ex12)
    write_file(*ex13)
    write_file(*ex14)
    write_file(*ex15)
    write_file(*ex16)
    write_file(*ex17)
    write_file(*ex18)
    write_file(*ex19)

    write_file(*ex21)
    write_file(*ex22)
    write_file(*ex23)
    write_file(*ex24)
    write_file(*ex25)
    write_file(*ex26)
    write_file(*ex27)
    write_file(*ex28)
    write_file(*ex29)

    tmp = [1, 4, 2, 5, 3, 6]
    kkk = 0
    for n in [400, 2000, 100000]:
        for k in [1, 2]:
            write_file(n-1, k, random_tree(n-1))
            write_file(n, k, random_tree(n))
            write_file(n, k, permute(random_tree(n)))
            write_file(n, k, random_tree(n, 1, 1))
            write_file(n, k, random_tree(n, 1, 2))
            write_file(n, k, random_tree(n, M, M))
            write_file(n, k, long_tree(n))
            write_file(n, k, long_tree(n, snipe=True))
            write_file(n, k, permute(long_tree(n, snipe=True)))
            write_file(n, k, long_tree2(n))
            write_file(n, k, long_tree2(n, snipe=True))
            write_file(n, k, permute(long_tree2(n, snipe=True)))
            write_file(n, k, star_tree(n))
            write_file(n, k, permute(star_tree(n)))
            write_file(n, k, line_tree(n))
            write_file(n, k, permute(line_tree(n)))
            write_file(n, k, permute(line_tree(n, M-1, M)))
            write_file(n, k, permute(line_tree(n, M, M)))
            write_file(n, k, binary_tree(n))
            write_file(n, k, permute(binary_tree(n)))
            if n == 100000:
                write_file(n, k, snipe_sqrt(n, 150))
                write_file(n, k, snipe_sqrt(n, 200))
                write_file(n, k, permute(snipe_sqrt(n, 250)))
                write_file(n, k, snipe_sqrt(n, 300))
                write_file(n, k, permute(snipe_sqrt(n, 333)))
                write_file(n, k, snipe_sqrt(n, 350))
                write_file(n, k, permute(snipe_sqrt(n, 400)))

            print(f"sub {tmp[kkk]} ok")
            kkk += 1


