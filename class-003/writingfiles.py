content = "hello this is some text"

lines = ["this is the first line\n", "this is the second line\n"]


with open("sometext2.txt", "w") as outfile:
    outfile.writelines(lines)
