import sys
upper_list=[]
for i in range(5):
    words = map(str, sys.stdin.readline().split())

    for word in words:
        upper_list.append(word.upper())
    print(' '.join(upper_list))
    upper_list=[]