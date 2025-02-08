n = int(input())
segments = [tuple(map(int, input().split())) for i in range(n)]
# 튜플 들의 리스트가 만들어 진다.

#배열에다가 하나씩 표시를 해준다. 해당 인덱스에 하나씩 추가를 해준다!
#그 전에 -가 있을때 OFFset을 설정 해줘야 한다.

arr = [0]*(200)
for x1,x2 in segments:
    for i in range(x1,x2+1):
        arr[i]+=1


print(max(arr))
