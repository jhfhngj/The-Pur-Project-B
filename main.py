import os
def splitter(text: str):
    return text.split("(")
var = {}
libs = []
def read(code):
    for line in code:
        if splitter(line)[0] == "prt":
            if var.get(splitter(line)[1]) == None:
                print(splitter(line)[1])
            else:
                print(var.get(splitter(line)[1]))
        elif splitter(line)[0] == "into":
            do = input()
            var.update({str(splitter(line)[1]): do})
        elif splitter(line)[0] == "get":
            if os.path.exists(splitter(line)[1]):
                libs.append(splitter(line)[1])
        elif splitter(line)[0] == "runlib":
            if libs.count(splitter(line)[1]) > 0:
                with open(splitter(line)[1]) as f:
                    r = f.readlines()
                read(r)
def rfl(file):
    with open(file,"r") as f:
        reads = f.readlines()
    read(reads)
