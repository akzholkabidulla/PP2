def spy_game(nums):
    result = False
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == '0' and nums[i+2]=='7':
            result = True
            break
    print(result)

nums = input().split()
spy_game(nums)