lst = [2, 5, 5, 11]
tar = 10
def tsum():
    for i in range(len(lst)):
        
        for j in range(i+1,len(lst)):
           print(lst[j])
           if lst[i]+lst[j]==tar:
               return [i,j]


print(tsum())