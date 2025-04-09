product_name, product_code = input().split()
product_code = int(product_code)

class Goods:
    def __init__(self,product_code=50, product_name="codetree"):
        self.product_code=product_code
        self.product_name=product_name

goods1 = Goods()
goods2 = Goods(product_code,product_name)

print(f"product {goods1.product_code} is {goods1.product_name}")
print(f"product {goods2.product_code} is {goods2.product_name}")
