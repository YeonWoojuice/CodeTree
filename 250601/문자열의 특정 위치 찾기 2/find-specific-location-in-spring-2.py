str1=input()
cnt=0
list1=["apple","banana","grape","blueberry","orange"]
for i in range(len(list1)):
    if (str1 in list1[i][2:4]):
        print(list1[i])
        cnt+=1
print(cnt)