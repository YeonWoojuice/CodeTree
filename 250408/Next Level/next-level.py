user2_id, user2_level = input().split()
user2_level = int(user2_level)

class User:
    def __init__(self,user2_id,user2_level):
        self.user2_id=user2_id
        self.user2_level=user2_level
    
user1 = User("codetree",10)
user2 = User(user2_id,user2_level)

print(f"user {user1.user2_id}",end=" ")
print(f"lv {user1.user2_level}")
print(f"user {user2.user2_id}",end=" ")
print(f"lv {user2.user2_level}")