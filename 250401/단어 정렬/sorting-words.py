n = int(input())
word = [input() for i in range(n)]

def f(word):
    word.sort()
    for i in word:
        print(i)

f(word)