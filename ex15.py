from sys import argv
script, filename = argv
prompt = ' -->'
print("here is the file u reqested")
txt=open(filename)
print(txt.read())
txt.close()

newfile=input("hello how are you? what file name would you like to open ")
txt=open(newfile)
print(txt.read())
txt.close()
