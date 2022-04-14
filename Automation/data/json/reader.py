def readfile(filename):
    with open(filename) as f:
        for line in f:
            print(line,end="")