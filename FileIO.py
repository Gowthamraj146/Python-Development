with open("D:\\KT\\MyTextFile.txt","w") as d:
    d.write("This is the first line\n")
    d.write("This is the second line\n")
    d.write("Final line of the Text File\n")

with open("D:\\KT\\MyTextFile.txt","r") as f:
    print(f.read())
    for line in f:
        print(line,end='')
    f.seek(0)

