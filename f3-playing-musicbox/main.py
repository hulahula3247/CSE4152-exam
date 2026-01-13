import sys; input = sys.stdin.readline
MIS = lambda: map(int, input().split())
II = lambda: int(input())
IS = lambda: input().strip()
from collections import *
import random

# 65 53 35 14 3
# 68 54 44 18 5



def check(task, N, K, s):
    assert isinstance(task, int)
    assert isinstance(N, int)
    assert isinstance(K, int)
    assert isinstance(s, str)

    assert (1 <= N <= 100000)
    assert (1 <= K <= N)
    assert len(s) == N
    assert not any(ch < '0' or ch > '9' for ch in s)

    if task == 1:
        assert (1 <= N <= 100 and K == 1)
    elif task == 2:
        assert (1 <= N <= 100 and K == 2)
    elif task == 3:
        assert (1 <= N <= 100)
    elif task == 4:
        assert (1 <= N <= 2000 and K == 1)
    elif task == 5:
        assert (1 <= N <= 2000 and K == 2)
    elif task == 6:
        assert (1 <= N <= 2000)
    elif task == 7:
        assert (1 <= N <= 100000 and K == 1)
    elif task == 8:
        assert (1 <= N <= 100000 and K == 2)
    elif task == 9:
        assert (1 <= N <= 100000)
    else:
        assert False

    return True
    
def solve(N, K, S):
    def can(X: int) -> bool:
        seg = 1
        l = 0          # start index of current segment in S
        pi = []        # prefix-function for current segment
        L = 0          # length of current segment

        for i in range(N):
            # append S[i] to current segment, update prefix function
            if L == 0:
                pi = [0]
                L = 1
                l = i
            else:
                k = pi[-1]
                while k > 0 and S[l + k] != S[i]:
                    k = pi[k - 1]
                if S[l + k] == S[i]:
                    k += 1
                pi.append(k)
                L += 1

            period = L - pi[-1]
            if period > X:
                seg += 1
                if seg > K:
                    return False
                l = i
                pi = [0]
                L = 1

        return True

    lo, hi = 0, N
    while lo+1 < hi:
        mid = (lo+hi)//2
        if can(mid): hi = mid
        else: lo = mid
    return hi

def solve2(N, K, S):
    def can(X: int) -> bool:
        seg = 1
        l = 0          # start index of current segment in S
        pi = []        # prefix-function for current segment
        L = 0          # length of current segment

        for i in range(N):
            # append S[i] to current segment, update prefix function
            if L == 0:
                pi = [0]
                L = 1
                l = i
            else:
                k = pi[-1]
                while k > 0 and S[l + k] != S[i]:
                    k = pi[k - 1]
                if S[l + k] == S[i]:
                    k += 1
                pi.append(k)
                L += 1

            period = L - pi[-1]
            if period > X:
                seg += 1
                if seg > K:
                    return False
                l = i
                pi = [0]
                L = 1

        return True

    for i in range(1, N+1):
        if can(i): return i


def solve3(N, K, S):
    def ok_prefix(seg_str, X):
        # returns True if seg_str is a prefix of some infinite repetition
        # with pattern length <= X, i.e., seg_str has a period d <= X.
        L = len(seg_str)
        for d in range(1, min(X, L) + 1):
            good = True
            for i in range(d, L):
                if seg_str[i] != seg_str[i - d]:
                    good = False
                    break
            if good:
                return True
        return False

    def can(X):
        seg = 1
        start = 0
        end = 0
        while end < N:
            # try to extend as far as possible
            best = end
            for e in range(end, N):
                if ok_prefix(S[start:e+1], X):
                    best = e + 1
                else:
                    break
            end = best
            if end >= N:
                return True
            seg += 1
            if seg > K:
                return False
            start = end
        return True

    for X in range(1, N + 1):
        if can(X):
            return X
    return N

tccnt = [0] * 10
def write_file(N, K, S, sub=-1): #파일 입출력

    if K > N or K <= 0: return

    if sub == -1:
        if N <= 100: sub = 0
        elif N <= 2000: sub = 3
        else: sub = 6

        if K == 1: sub += 1
        elif K == 2: sub += 2
        else: sub += 3

    assert check(sub, N, K, S)
    tccnt[sub] += 1
    tdx = tccnt[sub]

    fin = open(f"testcase/subtask{sub}-{tdx}.in", "w")
    fout = open(f"testcase/subtask{sub}-{tdx}.out", "w")

    fin.write(f"{N} {K}\n{S}\n")

    ans = solve(N, K, S)
    if sub <= 6: assert ans == solve2(N, K, S)
    if sub <= 2: assert ans == solve3(N, K, S)

    fout.write(f"{ans}\n")

def random_str(N, l=0, r=9):
    ret = ""
    for _ in range(N):
        cur = random.randint(l, r)
        ret += str(cur)
    return ret


def rep(p, N):
    """pattern p를 무한반복해서 길이 N prefix"""
    return (p * (N // len(p) + 1))[:N]

def mutate_one(s, pos, digits="0123456789"):
    """s[pos]를 다른 숫자로 1개 바꿈"""
    c = s[pos]
    cand = [d for d in digits if d != c]
    return s[:pos] + random.choice(cand) + s[pos+1:]

def two_phase(N, d1, d2, cut):
    """앞 cut은 주기 d1, 뒤는 주기 d2"""
    p1 = rep("".join(str((i*7+3)%10) for i in range(d1)), cut)
    p2 = rep("".join(str((i*5+1)%10) for i in range(d2)), N-cut)
    return p1 + p2

def periodic_then_spike(N, d, spike_pos=None):
    """주기 d로 길게 가다가 한 글자만 깨트림 (K에 따라 최적 분할 민감)"""
    if spike_pos is None:
        spike_pos = N - 1
    p = "".join(str((i*7+2)%10) for i in range(d))
    s = rep(p, N)
    s = mutate_one(s, spike_pos)
    return s

def border_heavy(N, a='1', b='2'):
    """
    border(접두=접미)가 엄청 큰 문자열:
    aaaaa...a b aaaaa...a 형태 -> pi가 길게 튐
    """
    k = N//2
    s = a * k + b + a * (N - k - 1)
    return s

def ladder_prefix(N, base="1234567890"):
    """
    prefix 사다리: base의 접두를 길이 1,2,3,... 식으로 이어붙임
    border/실패함수 구조 꼬이기 좋음
    """
    out = []
    i = 1
    while len(out) < N:
        out.append(base[:(i % len(base)) + 1])
        i += 1
    s = "".join(out)[:N]
    return s

def almost_constant_runs(N):
    """
    거의 상수인데 중간중간 다른 숫자 끼워넣음
    - 답이 1로 잘못 떨어지는 오답 잡기
    """
    s = ['0'] * N
    # 1% 지점에 스파이크 여러개
    for pos in [N//7, N//5, N//3, N//2, (2*N)//3, N-2]:
        if 0 <= pos < N:
            s[pos] = '1'
    return "".join(s)

ex1 = [5, 1, "12121"]
ex2 = [10, 2, "1231232132"]
ex3 = [20, 3, "12121200700700121212"]
ex4 = [1, 1, "0"]
ex5 = [2, 2, "00"]
ex6 = [3, 3, "000"]

if __name__ == "__main__":

    random.seed(3247)
    write_file(*ex1)
    write_file(*ex2)
    write_file(*ex3)
    write_file(*ex4)
    write_file(*ex5)
    write_file(*ex6)

    for N in [100, 2000, 100000]:

        write_file(N, 1, random_str(N, 0, 0))
        write_file(N, N, random_str(N, 0, 9))

        for k in [1, 2, 5, N//300, N//30, N//10]:

            write_file(N, k, random_str(N, 0, 9))
            write_file(N, k, random_str(N, 0, 2))
            write_file(N, k, random_str(N, 0, 1))

        for k in [1, 2, 5, N//300, N//30]:

            write_file(N, k, rep("0123456789", N))
            write_file(N, k, rep("012345678901234567890123456789012345678901234560123456789", N))
            write_file(N, k, rep("01020304050607009120001000000002000100102030405060700912000100003000200010", N))
            write_file(N, k, rep("01020304050607009120001000000002000100102030405060700912000100003000200010010203040506070091200010000000020001001020304050607009120001000030002000100000", N))
            write_file(N, k, periodic_then_spike(N, d=20, spike_pos=N-10))
            if N >= 2000: write_file(N, k, periodic_then_spike(N, d=200, spike_pos=N-100))
            if N >= 2000: write_file(N, k, periodic_then_spike(N, d=20000, spike_pos=N-1000))
            write_file(N, k, border_heavy(N, a='1', b='2'))

            write_file(N, k, ladder_prefix(N, base="12121234567890"))
            write_file(N, k, ladder_prefix(N, base="12121212121212345678901212121212121234567"))
            write_file(N, k, ladder_prefix(N, base="121212121212123456789012121212121212345671212121212121234567890121212121212123456"))
            write_file(N, k, ladder_prefix(N, base="12121212121212345678901212121212121234567121212121212123456789012121212121212345612121212121212345678901212121212121234567121212121212123456789012121212121212345612121212121212345678901212121212121234567121212121212123456789012121212121212345612121212121212345678901212121212121234567121212121212123456789012121212121212345677"))
            write_file(N, k, almost_constant_runs(N))

            if N == 2000:

                write_file(N, k, two_phase(N, d1=852, d2=97, cut=N//2))
                write_file(N, k, two_phase(N, d1=852, d2=997, cut=N//2))

            if N == 100000:

                write_file(N, k, two_phase(N, d1=22, d2=3247, cut=N//2))
                write_file(N, k, two_phase(N, d1=222, d2=3247, cut=N//2))
                write_file(N, k, two_phase(N, d1=2222, d2=3247, cut=N//2))
                write_file(N, k, two_phase(N, d1=22222, d2=3247, cut=N//2))



    #Author: Geunsoo Song (hulahula3247)
    #hulahula3247@gmail.com
   