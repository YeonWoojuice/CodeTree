unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class Bomb:
    def __init__(self,unlock_code,wire_color,seconds):
        self.unlock_code=unlock_code
        self.wire_color=wire_color
        self.seconds=seconds
    
bomb1 = Bomb(unlock_code,wire_color,seconds)
print(f"code : {bomb1.unlock_code}")
print(f"color : {bomb1.wire_color}")
print(f"second : {bomb1.seconds}")