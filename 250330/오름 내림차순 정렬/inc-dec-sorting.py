n = int(input())
nums = list(map(int, input().split()))

def sort(n,nums):
    nums.sort()
    print(*nums)
    nums.sort(reverse=True)
    print(*nums)

sort(n,nums)

