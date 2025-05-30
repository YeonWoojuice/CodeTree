class person:
    def __init__(self, name="", address="", region=""):
        self.name=name
        self.address=address
        self.region=region

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people=[person(name,address,region) for name,address,region in arr]

target_idx=0
for i, person in enumerate(people):
    if person.name > people[target_idx].name:
        target_idx = i

print(f"name {people[target_idx].name}")
print(f"addr {people[target_idx].address}")
print(f"city {people[target_idx].region}")