dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
num = input("roman no: ")
pval = 0
rnum = num[::-1]
sum = 0
for i in rnum:
    val = dict[i]
    if pval<=val:
        sum +=val
    else:
        sum -=val
    pval = val
print(sum)