import sys
n = int(sys.stdin.readline())

def f_cycle(n):
    if n == 1: return 2
    if n == 2: return 4

    # f(1)=2, f(2)=4로 시작
    seq = [0, 2, 4]          # 1-indexed 편의
    seen = {}                # (prev, curr) -> index
    prev, curr = 2, 4
    seen[(prev, curr)] = 2

    start_cycle = None
    while True:
        nxt = (prev * curr) % 100
        seq.append(nxt)
        prev, curr = curr, nxt
        key = (prev, curr)
        if key in seen:
            start_cycle = seen[key]   # 사이클 시작 인덱스
            break
        seen[key] = len(seq) - 1

    # 사이클 구간: [start_cycle+1 ... len(seq)-1] (1-indexed 기준 주의)
    # n이 사이클 전이면 그대로 반환, 아니면 주기 길이로 위치 점프
    if n < len(seq):
        return seq[n]

    cycle_head = start_cycle        # 사이클 직전 인덱스
    cycle_len  = (len(seq) - 1) - cycle_head
    idx_in_cycle = (n - cycle_head) % cycle_len
    if idx_in_cycle == 0:
        idx_in_cycle = cycle_len
    return seq[cycle_head + idx_in_cycle]

print(f_cycle(n))
