string = "abcerfabcabcedfkabcabcabcasdasdfsf"
x = "abc"
counter = 0
for _ in string:
    if (x + x + x) in string:
        counter += 1
print(counter)
