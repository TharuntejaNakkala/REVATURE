# Get score from user
score = int(input("Enter your score: "))
if 90 <= score <= 100:
    print("Grade: A")
elif 70 <= score < 90:
    print("Grade: B")
elif 60 <= score < 70:
    print("Grade: C")
else:
    print("Fail")
