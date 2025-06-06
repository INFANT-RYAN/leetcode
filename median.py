import math

def findMedianSortedArrays(nums1, nums2) :
        temp = nums1+nums2
        
        for i in range(len(temp)):
                for j in range(i+1,len(temp)):
                        if temp[i]>temp[j]:
                                swap = temp[i]
                                temp[i] = temp[j]
                                temp[j] = swap
        print(temp)
        if len(temp) % 2 != 0 :
                print(math.floor(len(temp)/2))
                print(temp[math.floor(len(temp)/2)])
        else:
                print(len(temp)/2)
                res = temp[int(len(temp)/2)]+temp[int((len(temp)/2)-1)]
                print(res/2)
findMedianSortedArrays([1,3],[2,5,6])