file=open("simple.txt","r")
read_file=file.read()
print(read_file)
file.close()

try:
    file=open("simple.txt","r")
    read_file=file.read()
    print(read_file)
except FileNotFoundError:
    print("The file simple.txt was not found")
finally:
   file.close()


