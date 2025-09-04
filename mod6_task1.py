marks={'Ayesha':70,'Shahbaaz':80,'Adan':100}
user=input("Enter the student's name: ")
if user in marks:
    print(user, "'s marks:",marks[user])
else:
    print("student not found")