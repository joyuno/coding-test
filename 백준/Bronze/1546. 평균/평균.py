N = int(input())
fix_nums=[]

nums = list(map(int,input().split()))
if N ==len(nums):
    for i in range(len(nums)):
        fix_nums.append(nums[i]/max(nums)*100)
print(sum(fix_nums)/len(fix_nums))