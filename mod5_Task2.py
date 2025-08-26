user=input("Enter text to write to the file: ")

with open("output.txt","w") as file:
    file.write(user+"\n")
    print('Data successfully written to output.txt')

user_1=input("Enter additional text to append: ")

with  open("output.txt", "a") as file:
        file.write(user_1 + "\n")
        print('Data successfully appended to output.txt')




