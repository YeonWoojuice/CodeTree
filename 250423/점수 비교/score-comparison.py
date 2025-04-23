A_math,B_math= map(int, input().split(" "))
A_eng,B_eng = map(int, input().split(" "))

if (A_math > B_math and A_eng > B_eng):
    print(1)
else:
    print(0)