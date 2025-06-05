
def reverse( x) :
        if x<0:
            num = str(abs(x))
            revnum = "-"+num[::-1]
            res = int(revnum)
            if res< -2_147_483_648 or res > 2_147_483_647:
                return 0
            else:
                return res
        else:
            num = str(x)
            revnum = num[::-1]
            res = int(revnum)
            if res< -2_147_483_648 or res > 2_147_483_647:
                return 0
            else:
                return res

print(reverse(-987))