word1 = input()
word2 = input()

arr_word1=list(word1)
arr_word2=list(word2)

arr_word1.sort()
arr_word2.sort()

def f(arr_word1,arr_word2):
    if len(arr_word1)!=len(arr_word2):
        return print("No")
    else:
        for i in range(0,len(arr_word1)):
            if arr_word1[i] != arr_word2[i]:
                return print("No")
        print("Yes")

f(arr_word1,arr_word2)

# Please write your code here.
