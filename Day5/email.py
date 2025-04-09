import re
a="ea@gmail.cou"
p=r"^[a-zA-Z0-9.]+@[a-z]+\.[a-z]{3,}"
m=re.search(p,a)
if m:
    print("success")
else:
    print("failed")