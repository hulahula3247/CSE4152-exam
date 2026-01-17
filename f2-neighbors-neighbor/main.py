import sys; input = sys.stdin.readline
MIS = lambda: map(int, input().split())
II = lambda: int(input())
IS = lambda: input().strip()
from collections import *
import random
sys.setrecursionlimit(int(2e5))
import time
LIM = int(1e9)

def check(task, N, M, W, edges):

    pa = list(range(N))
    sz = [1]*N

    def root(x):
        while pa[x] != x:
            pa[x] = pa[pa[x]]
            x = pa[x]
        return x

    def merge(a, b):
        a = root(a); b = root(b)
        if a == b: return
        if sz[a] < sz[b]:
            a, b = b, a
        pa[b] = a
        sz[a] += sz[b]

    # ----- basic type checks -----
    if not isinstance(task, int): return False
    if not isinstance(N, int): return False
    if not isinstance(M, int): return False
    if not isinstance(W, list): return False
    if not isinstance(edges, list): return False

    # ----- N, M global constraints -----
    if N < 3: return False
    if M < 1: return False
    if len(W) != N: return False
    if len(edges) != M: return False

    # ----- subtask constraints -----
    if task == 1:
        if not (3 <= N <= 100 and 2 <= M <= 2*N): return False
    elif task == 2:
        if not (3 <= N <= 2000 and 2 <= M <= 2*N): return False
    elif task == 3:
        if not (3 <= N <= 100000 and 2 <= M <= 2*N): return False
    elif task == 4:
        if not (3 <= N <= 100000 and 2 <= M <= 2*N): return False
    else:
        return False

    # ----- weight constraints -----
    for x in W:
        if not isinstance(x, int): return False
        if x < -LIM or x > LIM: return False
        if task == 3 and x < 0: return False

    # ----- edge constraints -----
    # also check simple upper bound for simple undirected graph
    if M > N*(N-1)//2: return False

    deg = [0]*N
    s = set()
    for e in edges:
        if not (isinstance(e, (list, tuple)) and len(e) == 2): return False
        u, v = e
        if not isinstance(u, int): return False
        if not isinstance(v, int): return False
        if not (1 <= u < v <= N): return False  # enforces u<v and bounds

        u -= 1; v -= 1
        if u == v: return False

        if (u, v) in s: return False
        s.add((u, v))

        deg[u] += 1
        deg[v] += 1
        merge(u, v)

    # ----- connectedness -----
    if sz[root(0)] != N: return False

    # ----- existence of at least one valid (a,b) with a common neighbor -----
    # equivalent to: exists a vertex with degree >= 2
    ok_pair = any(d >= 2 for d in deg)
    if not ok_pair: return False

    return True

def solve(N, M, W, graph):
    G = [[] for _ in range(N)]
    for a, b in graph:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = int(2e9)+1

    for c in range(N):
        if len(G[c]) < 2:
            continue
        vals = [W[nbr] for nbr in G[c]]
        vals.sort()
        l, r = 0, len(vals)-1
        while l < r:
            ans = min(ans, abs(vals[l] + vals[r]))
            s = vals[l] + vals[r]
            if s < 0: l += 1
            elif s > 0: r -= 1
            else: return 0
    return ans

def solve2(N, M, W, graph):
    G = [[] for _ in range(N)]
    for a, b in graph:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = int(2e9)+1

    for c in range(N):
        if len(G[c]) < 2:
            continue
        vals = [W[nbr] for nbr in G[c]]
        vals.sort()
        l, r = 0, len(vals)-1
        for l in range(len(vals)):
            for r in range(l+1, len(vals)):
                ans = min(ans, abs(vals[l] + vals[r]))
    return ans

tccnt = [0] * 10
def write_file(N, M, W, graph, sub=-1): #파일 입출력

    if M == -1: M = len(graph)

    if sub == -1:
        if N <= 100: sub = 1
        elif N <= 2000: sub = 2
        elif N <= 100000: sub = 4

    # print(sub, N, M, W, graph)
    assert check(sub, N, M, W, graph)
    tccnt[sub] += 1
    tdx = tccnt[sub]

    fin = open(f"testcase/subtask{sub}-{tdx}.in", "w")
    fout = open(f"testcase/subtask{sub}-{tdx}.out", "w")

    fin.write(f"{N} {M}\n")
    for i in range(N-1):
        fin.write(f"{W[i]} ")
    fin.write(f"{W[-1]}\n")
    for a, b in graph:
        fin.write(f"{a} {b}\n")

    ans = solve(N, N, W, graph)

    if N <= 2000:
        ans2 = solve2(N, N, W, graph)
        assert ans == ans2

    fout.write(f"{ans}\n")
    fin.close()
    fout.close()

def permute(N, M, W, graph):
    neww = [0]*N
    newg = []
    P = [i for i in range(N)]
    random.shuffle(P)
    for i in range(N):
        neww[P[i]] = W[i]
    for i in range(M):
        a, b = graph[i]
        na, nb = P[a], P[b]
        if na > nb: na, nb = nb, na
        newg.append((na, nb))
    return N, M, neww, newg

def random_tree(N):
    ret = []
    for i in range(2, N+1):
        cur = random.randint(1, i-1)
        ret.append([cur, i])
    return ret

def long_tree(N):
    ret = []
    for i in range(2, N//2+1):
        ret.append([i-1, i])
    for i in range(N//2+1, N+1):
        cur = random.randint(N//2, i-1)
        ret.append([cur, i])
    return ret

def star_tree(N):
    ret = []
    for i in range(2, N//2):
        ret.append([1, i])
    for i in range(N//2, N+1):
        cur = random.randint(1, i-1)
        ret.append([cur, i])
    return ret

def star_tree2(N):
    ret = []
    for i in range(2, N-10):
        ret.append([1, i])
    for i in range(N-10, N+1):
        cur = random.randint(1, i-1)
        ret.append([cur, i])
    return ret

def random_graph(N, func=random_tree):
    ret = func(N)
    st = set()
    for a, b in ret:
        if a > b: a, b = b, a
        st.add((a, b))
    while len(ret) != 2*N:
        a, b = random.randint(1, N), random.randint(1, N)
        if a == b: continue
        if a > b: a, b = b, a
        if not (a, b) in st:
            st.add((a, b))
            ret.append((a, b))
    return ret

def snipe_sqrt(N, func=random_tree, P=300):
    ret = func(N)
    st = set()
    for a, b in ret:
        if a > b: a, b = b, a
        st.add((a, b))
    cnt = 0; org = random.randint(1, N)
    assert N >= 90000
    while len(ret) != 2*N:
        b = random.randint(1, N)
        a = org
        if a == b: continue
        if a > b: a, b = b, a
        if not (a, b) in st:
            st.add((a, b))
            ret.append((a, b))
        cnt += 1
        if cnt == P:
            cnt = 0
            org = random.randint(1, N)
    return ret

def rw(N, l=-LIM, r=LIM):
    return [random.randint(l, r) for _ in range(N)]

def rw2(N):
    ret = []
    for i in range(N):
        cur = random.randint(int(6e8), int(1e9))
        if random.randint(0, 1) == 0: cur *= -1
        ret.append(cur)
    return ret

def plusarr(arr):
    ret = [abs(x) for x in arr]
    return ret

ex1 = [3, 2, [4, 3, 5],
       [[1, 3],
        [2, 3]]]

ex2 = [3, 3, [-4, -3, 5],
       [[1, 2],
        [1, 3],
        [2, 3]]]

ex3 = [4, 4, [-3, 2, -4, 7],
       [[1, 2],
       [2, 3],
       [3, 4],
       [1, 4]]]

ex4 = [4, 4, [-LIM, LIM, -LIM, LIM],
       [[1, 2],
       [2, 3],
       [3, 4],
       [1, 4]]]

if __name__ == "__main__":

    write_file(*ex1)
    write_file(*ex2)
    write_file(*ex3)
    write_file(*ex4)

    for N in [100, 2000, 100000]:
        write_file(N-1, -1, rw(N-1), random_tree(N-1))
        write_file(N, -1, rw(N), random_tree(N))
        write_file(N, -1, rw(N), long_tree(N))
        write_file(N, -1, rw(N), star_tree(N))
        write_file(N, -1, rw2(N), star_tree(N))

        write_file(N-1, -1, rw(N-1), random_graph(N-1))
        write_file(N, -1, rw(N), random_graph(N))

        write_file(N, -1, rw(N), random_graph(N))
        write_file(N, -1, rw2(N), long_tree(N))
        write_file(N, -1, rw2(N), random_graph(N))

        write_file(N, -1, rw(N), random_graph(N, func=long_tree))
        write_file(N, -1, rw2(N), random_graph(N, func=long_tree))
        write_file(N, -1, rw(N), random_graph(N, func=star_tree))
        write_file(N, -1, rw2(N), random_graph(N, func=star_tree))

        if N == 100000:
            write_file(N, -1, rw(N), snipe_sqrt(N, P=20))
            write_file(N, -1, rw2(N), snipe_sqrt(N, P=300))
            write_file(N, -1, rw(N), snipe_sqrt(N, P=5000))
            write_file(N, -1, rw2(N), snipe_sqrt(N, P=20000))
            write_file(N, -1, rw2(N), snipe_sqrt(N, func=long_tree, P=1000))
            write_file(N, -1, rw2(N), snipe_sqrt(N, func=star_tree, P=700))

    N = 100000
    write_file(N, -1, plusarr(rw(N)), random_graph(N), sub=3)
    write_file(N, -1, plusarr(rw(N)), random_tree(N), sub=3)
    write_file(N, -1, plusarr(rw(N)), long_tree(N), sub=3)
    write_file(N, -1, plusarr(rw(N)), star_tree(N), sub=3)
    write_file(N, -1, plusarr(rw(N)), random_graph(N, func=long_tree), sub=3)
    write_file(N, -1, plusarr(rw(N)), random_graph(N, func=star_tree), sub=3)
    write_file(N, -1, plusarr(rw(N)), snipe_sqrt(N, func=star_tree, P=20000), sub=3)
    write_file(N, -1, plusarr(rw(N)), snipe_sqrt(N, func=star_tree, P=20), sub=3)
    write_file(N, -1, plusarr(rw(N)), star_tree2(N), sub=3)
