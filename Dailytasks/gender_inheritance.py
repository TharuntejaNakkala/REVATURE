#Demonstrate inheritance and method overriding.
class person:
    pass

class male(person):
    def getGender(self):
        print("Male")

class Female(person):
    def getGender(self):
        print("female")

p = male()
p2 = Female()
p.getGender()
p2.getGender()
