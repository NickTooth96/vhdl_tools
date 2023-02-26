import os
import sys
import getopt

__version__ = "1.0.2"
__AUTHOR__ = "Nicholas Toothaker"

success = "File Processed"
no_change = "No Block Comments Found"
no_arg = "ERROR: No arguments given:\n\ttry: ./blockcom --Help"
FileTypeERROR = "ERROR: Incorrect File Type (File must be *.vhd file)"
FileNotFoundERROR = "ERROR: File Not Found"
versionMSG = """blockcom """ + str(__version__) + """\nCopywrite (C) 2023 Nicholas Toothaker
This is free software: you are free to change and redistribute
it. There is NO WARRANTY, to the extent permitted by law.
Written by """ + str(__AUTHOR__)

def path_check(filepath):
    path = os.path.join(os.path.dirname(__file__), filepath)
    ext = os.path.splitext(filepath)[-1].lower()
    if ext != ".vhd": 
        print(FileTypeERROR)
        raise SystemExit
    if os.path.exists(path) == False: 
        print(FileNotFoundERROR)
        raise SystemExit
    return path    

def comment(filepath):    
    i = 0
    lines = []
    lines_to_comment = []
    p = path_check(filepath)
    f = open(p, "r+")

    for line in f:
        if line.strip() == "block start":
           start = i
        if line.strip() == "block end":
            block = (start, i)
            lines_to_comment.append(block)
        lines.append(line)
        i += 1
    if len(lines_to_comment) == 0:
        print(no_change)
        raise SystemExit

    for element in lines_to_comment:
        l = element[0]
        m = element[1] + 1
        n = l
        for element in lines[l:m]:
            lines[n] = "-- " + element
            n += 1

    output = open(p,"w")
    output.writelines(lines)  
    print(success) 
    
       
def uncomment(filepath):
    i = 0
    lines = []
    lines_to_comment = []
    p = path_check(filepath)
    f = open(p, "r+")

    for line in f:
        if line.strip() == "-- block start":
           start = i
        if line.strip() == "-- block end":
            block = (start, i)
            lines_to_comment.append(block)
        lines.append(line)
        i += 1
    if len(lines_to_comment) == 0:
        print(no_change)
        raise SystemExit

    for element in lines_to_comment:
        l = element[0]
        m = element[1] + 1
        n = l
        for element in lines[l:m]:
            if (n == l):
                lines[n] = "\n"
            elif (n == m - 1):
                lines[n] = "\n"
            else:
                lines[n] = element[3:]
            n += 1

    output = open(p,"w")
    output.writelines(lines)
    print(success) 

def print_help():
    print("\n\tYou are on your own.")

arglist = sys.argv[1:]
options = "hc:u:v"
long_options = ["Help", "Comment", "Uncomment"]

if len(arglist) < 1:
    print(no_arg)
    raise SystemExit

try: 
    arguments, values = getopt.getopt(arglist, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-c", "--Comment"):
            comment(arglist[1])
        elif currentArgument in ("-u", "--Uncomment"):
            uncomment(arglist[1])
        elif currentArgument in ("-h", "--Help"):
            path = os.path.join(os.path.dirname(__file__), ".help.txt")
            f = open(path,"r")
            for line in f:
                print(line, end="")
        elif currentArgument in ("-v","--version"):
                print(versionMSG)
except getopt.error as err:
    print(str(err))