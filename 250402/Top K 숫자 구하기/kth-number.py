n, k = map(int, input().split())
nums = list(map(int, input().split()))

def f(k,nums):
    nums.sort()
    print(nums[k-1])

f(k,nums)

