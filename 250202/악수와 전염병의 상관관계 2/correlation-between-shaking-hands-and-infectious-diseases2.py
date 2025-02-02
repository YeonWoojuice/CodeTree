N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for i in range(T)]

handshakes.sort(key=lambda x: x[0])
# lambda 매개변수: 함수 안에 들어갈 내용  

A = [0]*(N+1)

arr = [P] 

for a,b,c in handshakes:
    if b in arr and c in arr:
        A[b]+=1
        A[c]+=1
    elif b in arr and A[b]<K:
        A[b]+=1
        arr.append(c)
    elif c in arr and A[c]<K:
        A[c]+=1
        arr.append(b)

for i in range(1,N+1):
    if i in arr:
        print(1, end="")
    else: 
        print(0, end="")



'''
for a, p1, p2 in handshakes:
    if p1 in arr:
        if p2 not in arr:
            arr.append(p2)
    elif p2 in arr:
        if p2 not in arr:
            arr.append(p1)
    A[p1] += 1
    A[p2] += 1

'''    



# 전염 개발자 저장 배열 만들기
# 개발자 고유 번호를 인덱스로 한다.
# 1번 -> 인덱스가 1번에다가 횟수 업데이트 
# 조건문을 통과 하면서 업데이트
# t-> 시간 얘를 기준으로 오름차순 정렬 
# 시간에 따라 순서대로 악수를 할 수 있음

