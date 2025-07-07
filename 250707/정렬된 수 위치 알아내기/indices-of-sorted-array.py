class Seq:
    def __init__(self, arr, idx):
        self.arr, self.idx = arr, idx

n = int(input())
seq = list(map(int, input().split()))
# 뭔가 이전 인덱스 정보를 저장해 놓아야 함

seq2 = [(v, i) for i, v in enumerate(seq)]

seq2.sort(key = lambda x:x[0])

pos=[0]*n

for sorted_idx, (val, original_idx) in enumerate (seq2):
    pos[original_idx] = sorted_idx +1

print(*pos)