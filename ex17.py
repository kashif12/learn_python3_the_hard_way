from sys import argv
script, in_file, out_file =argv
print(f"input file is {in_file} and is {len(in_file)} bytes long")
print(f"Output file exists? {exists(out_file)}")

handle= open(in_file,'r');
of=open(out_file,'w');
open.write(handle);
print("All done")
of.close()
handle.close();
