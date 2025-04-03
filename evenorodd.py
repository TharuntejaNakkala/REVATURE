n = int(input("Enter a number"))
if n % 2 == 0:
    print("even")
else:
    print("odd")

#REPLACE EVEN NUMBER TO #
for num in range(1, 101): 
    if num % 2 == 0:  
        print("#", end=" ")  
    else:
        print(num, end=" ") 
