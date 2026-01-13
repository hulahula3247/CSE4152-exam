import sys; input = sys.stdin.readline
MIS = lambda: map(int, input().split())
II = lambda: int(input())
IS = lambda: input().strip()
from collections import *
import random
M = int(1e6)

def check(task, N, arr): #데이터 형태 체크
    if not isinstance(N, int): return False
    if not len(arr) == N: return False
    if task == 1:
        if not 1 <= N <= 10: return False
    if task == 2:
        if not 1 <= N <= 2000: return False
    if task == 3:
        if not 1 <= N <= 80: return False
    if task == 4:
        if not 1 <= N <= 400: return False
    if task == 5:
        if not 1 <= N <= 2000: return False
    for i in range(N):
        if not len(arr) == N: return False
        for j in range(N):
            if not isinstance(arr[i][j], int): return False
            if task == 1 or task == 2:
                if not 0 <= arr[i][j] <= 1: return False
            else:
                if not -M <= arr[i][j] <= M: return False
    return True

def solve(N, arr): #정해

    def histo(N, flatt):
        st = []
        mmax = 0
        flatt = [0] + flatt
        for i in range(1, len(flatt)):
            while st and flatt[st[-1]] > flatt[i]:
                height = flatt[st.pop()]
                if not st: width = i - 1
                else: width = i - st[-1] - 1
                mmax = max(mmax, height*width)
            st.append(i)
        while st:
            height = flatt[st.pop()]
            if not st:
                width = len(flatt)-1
            else:
                width = len(flatt)-1 - st[-1]
            mmax = max(mmax, height*width)
        return mmax
    
    ans = 0
    last = [int(2e9)]*N
    flat = [0]*N
    for i in range(N):
        query = []
        for j in range(N):
            if arr[i][j] == last[j]: flat[j] += 1
            else: flat[j] = 1
            if j != 0 and arr[i][j-1] != arr[i][j]:
                ans = max(ans, histo(N, query))
                query = []
            query.append(flat[j])
            last[j] = arr[i][j]
        ans = max(ans, histo(N, query))
    return ans

def solve2(N, arr): #검증용 naive
    ans = 0
    for x in range(N):
        for xx in range(x, N):
            for y in range(N):
                for yy in range(y, N):
                    fg = True
                    tg = arr[x][y]
                    for i in range(x, xx+1):
                        for j in range(y, yy+1):
                            if arr[i][j] != tg:
                                fg = False
                    if fg: ans = max(ans, (xx-x+1)*(yy-y+1))
    return ans

tccnt = [0] * 10
def write_file(sub, arr): #파일 입출력
    N = len(arr)

    assert check(sub, N, arr)
    tccnt[sub] += 1
    tdx = tccnt[sub]

    fin = open(f"testcase/subtask{sub}-{tdx}.in", "w")
    fout = open(f"testcase/subtask{sub}-{tdx}.out", "w")

    fin.write(f"{N}\n")
    for i in range(N):
        for j in range(N-1):
            fin.write(f"{arr[i][j]} ")
        fin.write(f"{arr[i][-1]}\n")

    ans = solve(N, arr)
    if N <= 10:
        ans2 = solve2(N, arr)
        assert ans == ans2

    fout.write(f"{ans}\n")

    fin.close()
    fout.close()

def make_random(N, L, R):
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = random.randint(L, R)
    return arr

def make_ratio(N, L, R, v, ratio):
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = random.randint(L, R)
            if random.random() < ratio:
                arr[i][j] = v
    return arr

def make_fixarea(N, y1, y2, x1, x2, v, L, R):
    arr = [[0]*N for _ in range(N)]
    assert y1 <= y2 and x1 <= x2 and 0 <= y1 < N and 0 <= y2 < N and 0 <= x1 < N and 0 <= x2 < N
    for i in range(N):
        for j in range(N):
            if y1 <= i <= y2 and x1 <= j <= x2: arr[i][j] = v
            else: arr[i][j] = random.randint(L, R)
    return arr

def make_stair(N, L, R):
    arr = [[0]*N for _ in range(N)]        
    for i in range(N):
        for j in range(N):
            if i >= j: arr[i][j] = L
            else: arr[i][j] = R
    return arr

def make_zigzag(N, a, b, L, R, bk=False):
    arr = [[L]*N for _ in range(N)]
    M = a//b
    for j in range(N):
        cur = N-1
        for i in range((a if j%2 else b)):
            if bk and j%M == 0: continue
            arr[cur][j] = R
            cur -= 1
    return arr

def k_color(N, k, ad=0):
    P = [i for i in range(N*N)]
    random.shuffle(P)
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            key = i*N+j
            color = key%k+ad
            pos = P[key]
            ii = pos//N; jj = pos%N
            arr[ii][jj] = color
    return arr

ex1 = [[1, 0, 0, 0],
       [1, 0, 1, 0],
       [1, 1, 0, 0],
       [0, 1, 1, 0]]

ex2 =   [[0, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [0, 1, 1, 1, 0],
         [1, 1, 0, 0, 1]]

ex3 =   [[0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]

ex4 =   [[0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]

ex5 =   [[0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 0, 1, 1],
         [1, 1, 1, 1, 0]]

ex6 =  [[0]]
ex7 =  [[1]]

eex1 = [[1, 2, 2, 2],
        [1, 2, 2, 2],
        [1, 2, 2, 2],
        [3, 3, 0, -1]]

eex2 = [[1, 1, 2, 2, 2, 4],
        [1, 1, 1, 2, 2, 4],
        [3, 1, 1, 2, 2, 2],
        [3, 3, 3, 3, 3, 2],
        [4, 4, 4, 4, 4, 5],
        [5, 5, 5, 5, 1, 1]]

eex3 = [[-1]]
eex4 = [[-M]]
eex5 = [[M]]

eex6 = [[0, -1, 0, -1, 0],
        [0, -1, -1, -1, 0],
        [-1, -1, -1, -1, -1],
        [0, -1, -1, -1, 0],
        [-1, -1, 0, 0, -1]]

eex7 = [[2, 3, 5, 3, -M],
        [0, 3, 1, 3, -M],
        [4, 3, 3, 3, M],
        [5, 3, 3, 3, 3],
        [3, 3, 3, 3, 3]]

eex8 = [[M-1, M, 0, M, -M],
        [M-1, M, 1, M, -M],
        [-M, M, M, M, M-1],
        [M, M, M, M, M],
        [M, M, M, M, M]]

eex9 = [[0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, -1, 1, 1],
        [1, 1, 1, 1, 0]]

if __name__ == "__main__":

    write_file(1, ex1)
    write_file(1, ex2)
    write_file(1, ex3)
    write_file(1, ex4)
    write_file(1, ex5)
    write_file(1, ex6)
    write_file(1, ex7)

    write_file(1, make_random(10, 0, 1))
    write_file(1, make_fixarea(10, 0, 9, 0, 9, 0, 0, 1))
    write_file(1, make_fixarea(10, 3, 7, 2, 7, 1, 0, 1))
    write_file(1, make_fixarea(10, 6, 7, 1, 9, 1, 0, 1))
    write_file(1, make_fixarea(10, 0, 7, 7, 7, 0, 0, 1))

    write_file(1, make_stair(10, 0, 1))
    write_file(1, make_zigzag(10, 9, 2, 0, 1))
    write_file(1, make_zigzag(10, 9, 2, 1, 0, True))
    print("sub1 ok")
    ## sub1

    write_file(2, make_random(1999, 0, 1))
    write_file(2, make_ratio(2000, 0, 1, 0, 0.9))
    write_file(2, make_ratio(2000, 0, 1, 0, 0.999))
    write_file(2, make_ratio(2000, 0, 1, 0, 0.99999))

    write_file(2, make_fixarea(2000, 0, 1999, 0, 1999, 0, 0, 1))
    write_file(2, make_zigzag(2000, 1999, 2, 1, 0, True))
    print("sub2 ok")

    ## sub2
   
    N = 80
    write_file(3, eex1)
    write_file(3, eex2)
    write_file(3, eex3)
    write_file(3, eex4)
    write_file(3, eex5)
    write_file(3, eex6)
    write_file(3, eex7)
    write_file(3, eex8)
    write_file(3, eex9)

    write_file(3, make_random(N, -N, N))
    write_file(3, make_random(N, -M, M))
    write_file(3, make_ratio(N, -N, N, 3247, 0.99))
    write_file(3, make_ratio(N, -M, M, 3247, 0.999))
    
    write_file(3, make_fixarea(N, 0, N-1, 0, N-1, M-3247, -N, N))
    write_file(3, make_fixarea(N, 5, N-15, 25, N-35, random.randint(-M, M), -M, M))
    write_file(3, make_fixarea(N, N//2, N//2, 0, N-1, random.randint(-M, M), -M, M))
    write_file(3, make_fixarea(N, N//2, N//2+2, N//4, 3*N//4, random.randint(-M, M), -M, M))

    write_file(3, make_fixarea(N, N//4, N//4+5, N//6, N//6+5, M-3247, -M//2, M//2))
    write_file(3, make_fixarea(N, N//4, N//4+15, N//6, N//6+25, M-3247, -M//4, M//4))
    write_file(3, make_fixarea(N, N//4, N//4+N//50, N//6, N//6+N//50, M-3247, -M//8, M//8))
    write_file(3, make_fixarea(N, N//4, N//2, N//6, N//3, M-3247, -M//2, M//2))
    write_file(3, make_fixarea(N, N//4, N//4*3, N//6, N//6*5, M-3247, -M//4, M//4))

    write_file(3, make_stair(N, -M+3247, M-3247))
    write_file(3, make_zigzag(N, N-1, 2, -77, 77))
    write_file(3, make_zigzag(N, N-1, 2, 77, -77, True))

    write_file(3, k_color(N, 3))
    write_file(3, k_color(N, 4))
    write_file(3, k_color(N, 5))
    write_file(3, k_color(N, 10))
    write_file(3, k_color(N, 100))
    write_file(3, k_color(N, 1000))
    print("sub3 ok")

    #sub3

    N = 400

    write_file(4, make_random(N, -N, N))
    write_file(4, make_random(N, -M, M))
    write_file(4, make_ratio(N, -N, N, 3247, 0.99))
    write_file(4, make_ratio(N, -N, N, 3247, 0.999))
    write_file(4, make_ratio(N, -N, N, 3247, 0.9999))
    write_file(4, make_ratio(N, -M, M, 3247, 0.99999))
    
    write_file(4, make_fixarea(N, 0, N-1, 0, N-1, M-3247, -N, N))
    write_file(4, make_fixarea(N, 5, N-15, 25, N-35, random.randint(-M, M), -M, M))
    write_file(4, make_fixarea(N, 5, N-15, N//2, N//2+1, random.randint(-M, M), -M, M))
    write_file(4, make_fixarea(N, N//2, N//2, 0, N-1, random.randint(-M, M), -M, M))
    write_file(4, make_fixarea(N, N//2, N//2+2, N//4, 3*N//4, random.randint(-M, M), -M, M))

    write_file(4, make_fixarea(N, N//4, N//4+5, N//6, N//6+5, M-3247, -M//2, M//2))
    write_file(4, make_fixarea(N, N//4, N//4+15, N//6, N//6+25, M-3247, -M//4, M//4))
    write_file(4, make_fixarea(N, N//4, N//4+N//50, N//6, N//6+N//50, M-3247, -M//8, M//8))
    write_file(4, make_fixarea(N, N//4, N//2, N//6, N//3, M-3247, -M//2, M//2))
    write_file(4, make_fixarea(N, N//4, N//4*3, N//6, N//6*5, M-3247, -M//4, M//4))

    write_file(4, make_stair(N, -M+3247, M-3247))
    write_file(4, make_zigzag(N, N-1, 2, -77, 77))
    write_file(4, make_zigzag(N, N-1, 2, 77, -77, True))

    write_file(4, k_color(N, 3))
    write_file(4, k_color(N, 5))
    write_file(4, k_color(N, 10))
    write_file(4, k_color(N, 100))
    write_file(4, k_color(N, 400))
    write_file(4, k_color(N, 2000))
    write_file(4, k_color(N, 5000))

    print("sub4 ok")
    #sub4

    N = 2000

    write_file(5, make_random(N, -M, M))
    write_file(5, make_ratio(N, -N, N, random.randint(-M, M), 0.999))
    write_file(5, make_ratio(N, -M, M, random.randint(-M, M), 0.99999))
    write_file(5, make_ratio(N, -M, M, random.randint(-M, M), 0.999995))
    
    write_file(5, make_fixarea(N, 0, N-1, 0, N-1, M-3247, -N, N))
    write_file(5, make_fixarea(N, N//4, N//2, N//6, N//3, M-3247, -M//2, M//2))

    write_file(5, k_color(N, 5))
    write_file(5, k_color(N, 400))
    write_file(5, k_color(N, 5000))

    tmp = k_color(N, 5000)
    for i in range(N//2, N//2+N//3):
        for j in range(N//6, N//6+N//7):
            tmp[i][j] = 3247
    write_file(5, tmp)

    print("sub5 ok")
    #sub5

    #Author: Geunsoo Song (hulahula3247)
    #hulahula3247@gmail.com