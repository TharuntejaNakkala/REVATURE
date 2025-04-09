try:
    a=10/0
    print(a)
    b={'name':'Tharun','age':22}
    print(b['nam'])
    c=[1,2,3,4]
    print(c[4])
    print(a)
    file=open("file.txt",'w')
    c=file.read("hello eswar")
    print(c)
except ZeroDivisionError as e:
    print(e)
except KeyError as e:
    print("key value error")
except IndexError as e:
    print(e)  
except NameError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
