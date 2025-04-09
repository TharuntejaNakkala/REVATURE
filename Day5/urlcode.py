#URL VERIFICATION CODE

import re
url_pattern=r"http://www.[a-zA-Z0-9.]+\.[a-z]{2,}/"
url=str(input("enter url: "))
match=re.search(url_pattern,url)
if match:
    print("success..!")
else:
    print("failed..!")

# import re
# a="ea@gmail.cou"
# p=r"^[a-zA-Z0-9.]+@[a-z]+\.[a-z]{3,}"
# m=re.search(p,a)
# if m:
#     print("success")
# else:
#     print("failed")