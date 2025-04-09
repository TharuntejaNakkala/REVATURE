#PASWORD VERIFICATION CODE

import re
password_pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%])[a-zA-Z0-9@#$%]{8,}$"

class passwordex(Exception):    
    pass

def checkpassword(password):
    if re.search(password_pattern,password):
        print("password matched..!")
    else:
        raise passwordex("incorrect password..!")
try:
    password=str(input("enter your password:"))
    checkpassword(password)
except passwordex as e:
    print(e)