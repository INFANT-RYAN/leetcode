inp = "{[]}"
st=[]
def isvalid():
    d = {'{':'}','[':']','(':')'}
    for i in inp:
        if i in d:
            st.append(i)
        else:
            if st == []:
                return("False")
            else:
                if d[st[-1]] == i:
                    st.pop()
                else:
                    return("False")
    if st ==[]:
        return("true")
    else: 
        return("False")


print(isvalid())