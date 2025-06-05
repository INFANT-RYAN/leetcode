import re

def isPalindrome(s: str) -> bool:
        string1 = s.replace(" ","")
        string2 = string1.lower()
        val = s.replace(" ","")
        final = re.sub(r'[^a-zA-Z0-9]',"",val.lower())
        res = re.sub(r'[^a-zA-Z0-9]',"",string2[::-1])
        if final==" ":
              return True
        elif final == res:
              print(final)
              print(res)
              return True
        else:
              print(final)
              print(res)
              return False
print(isPalindrome("A man, a plan, a canal: Panama"))
        