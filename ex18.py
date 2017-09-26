def print_these (*argv):
    one,two=argv
    print(f"first:{one},second:{two}")

print_these("1","3")
print_these(1,1+1)
print_these(a+a,2+3)
