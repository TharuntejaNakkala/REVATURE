# Creating a dictionary
my_dict = {
    "name": "Tharun",
    "age": 22,
    "city": "Chennai"
}


print("Name:", my_dict["name"])  


print("Age using get():", my_dict.get("age"))  

my_dict["job"] = "Engineer"  
print("After adding job:", my_dict)  


my_dict["age"] = 23  
print("After updating age:", my_dict)  

my_dict.pop("city")  
print("After removing city:", my_dict)  

print("Keys:", list(my_dict.keys()))  

print("Values:", list(my_dict.values()))  


