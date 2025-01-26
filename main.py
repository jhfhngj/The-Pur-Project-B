#!/usr/bin/python
import os
import sys
def splitter(text: str):
    return text.split("(")
var = {}
libs = []
out = ""
def read(code):
    out = ""
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
        elif splitter(line)[0] == "if=":
            if var.get(splitter(line)[1]) == None:
                v1 = "str"
            else:
                v1 = "var"
            if var.get(splitter(line)[2]) == None:
                v2 = "str"
            else:
                v2 = "var"
            if v1 == "str" and v2 == "str":
                if splitter(line)[1] == splitter(line)[2]:
                    out = "True"
                else:
                    out = "False"
            if v1 == "var" and v2 == "var":
                if var.get(splitter(line)[1]) == var.get(splitter(line)[2]):
                    out = "True"
                else:
                    out = "False"
            if v1 == "str" and v2 == "var":
                if splitter(line)[1] == var.get(splitter(line)[1]):
                    out = "True"
                else:
                    out = "False"
            if v1 == "var" and v2 == "str":
                if var.get(splitter(line)[1]) == splitter(line)[2]:
                    out = "True"
                else:
                    out = "False"
            var.update({splitter(line)[3]: out})
           
def rfl(file):
    with open(file,"r") as f:
        reads = f.readlines()
    read(reads)
if len(sys.argv) > 1:
    rfl(sys.argv[1])
    input("Press Enter to continue . . . ")
