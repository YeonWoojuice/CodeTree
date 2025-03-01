A = input()
list1=[]
list2=[]

def palindrome(A):
    list1=list(A)
    list2=list1[::-1]
    
    for i in range(0,len(list1)):
        if (list1[i]!=list2[i]):
            return False
        
if (palindrome(A)==False):
    print("No")
else:
    print("Yes")