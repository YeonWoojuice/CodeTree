class Person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

n = 5

people=[]

for _ in range(n):
    name, height, weight = input().split()
    people.append(Person(name,int(height),float(weight)))

people.sort(key = lambda x : x.name)

print("name")
for person in people:
    print(person.name, person.height, person.weight)

people.sort(key = lambda x : -x.height)
print()

print("height")
for person in people:
    print(person.name, person.height, person.weight)


# Please write your code here.