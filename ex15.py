from sys import argv
script,filename=argv
txt=open(filename)
# If you provide the correct arguments, the script will read and display the contents of the specified file and
# prompt you to input another filename to read again.
print(f"Here's your file{filename}:")
print(txt.read())
print("Type the filename again:")
file_again=input(">")
txt_again=open(file_again)
print(txt_again.read())