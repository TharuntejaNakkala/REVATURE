def get_user_details():
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    city = str(input("Enter your city: "))

    return {
        "name": name,
        "age": age,
        "city": city
    }

def display_user_details(user_details):
    print("User Details:")
    print("Name:", user_details["name"])
    print("Age:", user_details["age"])
    print("City:", user_details["city"])

get_user_details = get_user_details()
display_user_details(get_user_details)