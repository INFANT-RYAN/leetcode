def moveZero(lst):
    i = 0
    for j in range(len(lst)):
        if lst[j]!=0:
            print("lst[i],lst[j] ",lst[i],lst[j])
            lst[i],lst[j]=lst[j],lst[i]
            print("lst[i],lst[j] ",lst[i],lst[j])
            i+=1
        else:
            print("zero")
    print(lst)

moveZero([0, 1, 0, 3, 12])