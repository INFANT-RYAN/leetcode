x = int(input("enter the num :"))
def pal():
    y=str(x)
    z = y[::-1]
    if z == y:
        return True
    else:
        return False
print(pal())