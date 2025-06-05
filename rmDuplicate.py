nums = [1,1,2]
lst = []
lst1=[]

for i in nums:
    if i not in lst:
        lst.append(i)
    else:
        lst1.append(i)
print(lst,lst1)

nums = lst+lst1
print(nums)