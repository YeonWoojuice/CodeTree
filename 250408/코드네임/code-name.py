MAX_N = 5


codenames = []
scores = []

for i in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

for j in range(MAX_N):
    if scores[j]==min(scores):
        print(codenames[j],end=" ")
        print(scores[j])



