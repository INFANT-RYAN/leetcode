def maxArea(height) -> int:
        lp = 0
        rp = len(height)-1
        area = 0
        while lp < rp:
            area = max(area,(rp-lp)*min(height[lp],height[rp]))
            if height[lp]<height[rp]:
                lp+=1
            else :
                rp-=1
        return area
print(maxArea([1,8,6,2,5,4,8,3,7]))