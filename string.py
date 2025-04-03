my_str = "Hello, World!"
print("Length:", len(my_str))  
print("Uppercase:", my_str.upper())
print("Lowercase:", my_str.lower())
print("Title Case:", my_str.title()) 
print("Replace 'World' with 'Python':", my_str.replace("World", "Python"))  

words = my_str.split(", ")  
print("Splitted list:", words)  

new_str = "-".join(words)  
print("Joined string:", new_str)  

