import os
import subprocess
import sys
import time
import pathlib
import re

# =========================
# Config (문제별로 이 블록만 고정 세팅)
# =========================
TIME_LIMIT = 1.0   # seconds per testcase

scores =     [40, 20, 20, 20] # 각 서브태스크 점수
test_cases = [35, 27, 51, 45] # 각 서브태스크 내 테케 개수

INPUT_DIR  = '.elice/testcase/'
OUTPUT_DIR = '.elice/testcase/'

# 서브태스크 정의 (requires로 의존관계 명시)
SUBTASKS = [
    {"name": "Subtask 1", "count": test_cases[0], "requires": []},
    {"name": "Subtask 2", "count": test_cases[1], "requires": [0]},  # 0-base
    {"name": "Subtask 3", "count": test_cases[2], "requires": [0, 1]},  # 0-base
    {"name": "Subtask 4", "count": test_cases[3], "requires": [0, 1, 2]},  # 0-base
]

SUM_TESTCASE_SCORES = sum(scores)

# =========================
# Elice utils (고정)
# =========================
sys.path.append(os.getcwd())
from grader_elice_utils import EliceUtils  # isort:skip
elice_utils = EliceUtils()
elice_utils.secure_init()

import resource
soft, hard = resource.getrlimit(resource.RLIMIT_STACK)
new_soft = 256 * 1024 * 1024  # 256MB
resource.setrlimit(resource.RLIMIT_STACK, (new_soft, hard))
#스택 메모리 제한 변경

# =========================
# Helpers
# =========================
def run_case(exe_path: str, input_text: str, timeout_sec: float):
    proc = subprocess.Popen(
        [exe_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=True,
    )
    start = time.perf_counter()
    try:
        out, err = proc.communicate(input=input_text, timeout=timeout_sec)
        elapsed = time.perf_counter() - start
        return proc.returncode, out, err, False, elapsed
    except subprocess.TimeoutExpired:
        try:
            proc.kill()
        except Exception:
            pass
        try:
            out, err = proc.communicate(timeout=0.2)
        except Exception:
            out, err = "", ""
        elapsed = timeout_sec
        return None, out, err, True, elapsed

def must_exist(path: pathlib.Path) -> bool:
    try:
        return path.exists()
    except Exception:
        return False

def case_paths(sub_idx: int, case_idx: int):
    in_path  = pathlib.Path(INPUT_DIR)  / f"subtask{sub_idx+1}-{case_idx}.in"
    out_path = pathlib.Path(OUTPUT_DIR) / f"subtask{sub_idx+1}-{case_idx}.out"
    return in_path, out_path

def normalize_text(s: str) -> str:
    s = s.replace('\r\n', '\n').replace('\r', '\n') #개행 처리
    s = re.sub(r'[ \t](?=\n|$)', '', s) #각 줄마다, 마지막 스페이스, 탭만 삭제
    if s.endswith('\n'): s = s[:-1] #마지막 \n에 대해서만, 이것만 삭제: 백준포멧
    return s

# =========================
# Main
# =========================
total_score = 0

try:
    build = subprocess.run(
        ['g++', '-o', 'main', 'main.cpp'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if build.returncode != 0:
        elice_utils.secure_send_grader("💥 Compile Error:\n" + (build.stderr[:800] or build.stdout[:800]))
        raise RuntimeError("Compile failed")

    for s_idx, st in enumerate(SUBTASKS):
        for i in range(1, st["count"] + 1):
            ip, op = case_paths(s_idx, i)
            if not must_exist(ip) or not must_exist(op):
                missing = ip.name if not must_exist(ip) else op.name
                raise RuntimeError(f"Missing testcase: {missing}")

    subtask_pass = [False] * len(SUBTASKS)

    for s_idx, st in enumerate(SUBTASKS):
        name = st["name"]
        ncase = st["count"]
        reqs = st.get("requires", [])

        failed_reqs = [r for r in reqs if not subtask_pass[r]]
        if failed_reqs:
            why = ", ".join(SUBTASKS[r]["name"] for r in failed_reqs)
            elice_utils.secure_send_grader(f"\n {name}: skipped (prerequisite failed: {why})\n")
            continue

        elice_utils.secure_send_grader(f"\n Grading {name} (subtask {s_idx+1}, cases: 1..{ncase})\n")
        all_ok = True
        durations = []

        for i in range(1, ncase + 1):
            ip, op = case_paths(s_idx, i)
            try:
                input_text = ip.read_text(encoding='utf-8', errors='ignore')
                expected_text = op.read_text(encoding='utf-8', errors='ignore')
            except Exception as e:
                msg = f" 💥  [{name} #{i:02d}] File read error: {e} \n"
                all_ok = False
                break

            rc, out, err, is_tle, elapsed = run_case('./main', input_text, TIME_LIMIT)
            tag = f"[{name} #{i:02d}]"

            if is_tle:
                msg = f" ❌  {tag} Time Limit Exceeded at case #{i:02d} \n"
                all_ok = False
                break
            if rc is None or rc != 0:
                snippet = (err[:300] + '...') if err and len(err) > 300 else (err or "")
                msg = f" 💥  {tag} Runtime Error at case #{i:02d} \n{snippet}\n"
                all_ok = False
                break

            got = normalize_text(out)
            exp = normalize_text(expected_text)
            if got == exp:
                durations.append(elapsed)
                continue
            else:
                msg = f" ❌  {tag} Wrong Answer at case #{i:02d} \n"
                all_ok = False
                break

        if all_ok:
            subtask_pass[s_idx] = True
            total_score += scores[s_idx]
            if durations:
                mx = max(durations)
                pct = (mx / TIME_LIMIT) * 100.0
                elice_utils.secure_send_grader(
                    f" ✅  {name}: PASSED (+{scores[s_idx]}) | max time = {mx*1000:.1f} ms\n"
                )
            else:
                elice_utils.secure_send_grader(
                    f" ✅  {name}: PASSED (+{scores[s_idx]})\n"
                )
        else:
            subtask_pass[s_idx] = False
            elice_utils.secure_send_grader(msg)

    total_score = int(total_score)

except Exception as err:
    elice_utils.secure_send_grader(
        f"채점 도중 오류가 발생했습니다. 코드 실행을 확인하세요.\n오류: {str(err)}\n"
    )

finally:
    elice_utils.secure_send_grader(f"\n최종 점수는 : {total_score}/{SUM_TESTCASE_SCORES}점 입니다\n")
    elice_utils.secure_send_score(total_score)
    try:
        time.sleep(0.5)
    except Exception:
        pass
    os._exit(0)
