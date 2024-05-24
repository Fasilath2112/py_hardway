# Copies the content of one file to another, providing information about the file sizes and user confirmation prompts. 
from sys import argv
from os.path import exists
script, from_file, to_file=argv
print(f"Copying from{from_file} to {to_file}")
in_file=open(from_file)
indata=in_file.read()
print(f"The input file is {len(indata)} bytes long")
print("ready, hit RETURN to continue, CTRL-C to abort")
input()
out_file=open(to_file,'w')
out_file.write(indata)
print("alright all done")
out_file.close()
in_file.close()
