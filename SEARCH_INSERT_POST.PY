LST=[1,3,5,6]
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(LST)
            


print(searchInsert(LST,5))