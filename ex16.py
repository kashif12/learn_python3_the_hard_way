from sys import argv
script , file_name = argv

print(f"Now we are going to truncate file{file_name}");
print(f"if you don't want that press ctrl+c (control c)\n otherwise press enter")
input()
handle= open(file_name,'a');
#handle.truncate();

print("now we are going to write some data into the file/n , we are going to ask you to enter three lines")
print("enter line 1")
line1= input("Line 1:")
line2= input("Line 2:")
line3= input("line 3:")

handle.write( line1+ '\n'+line2 + '\n' +line3 + '\n');

# handle.write(line1);
# handle.write('\n')
# handle.write(line2);
# handle.write('\n')
# handle.write(line3);
# handle.write('\n')
handle.close()

