import os
import sys
import getopt
import datetime

__version__ = "1.0.0"
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

class TestBench:
    i = 0
    name = ""
    description = ""
    date = datetime.datetime.now().strftime("%x")
    entity = []
    ports = []
    signals = []
    port_map = []
    test_cases = []
    lines = []
    filepath = ""

    def __init__(self, filepath, data=None):

        self.filepath = filepath
        self.data = data
        
        p = self.path_check()
        f = open(p, "r+")

        i = 0
        for line in f:
            self.lines.append(line)
            i += 1

        name = self.get_name()
        description = self.get_description()
        date = datetime.datetime.now().strftime("%x")
        entity = self.get_entity()
        ports = self.get_ports()
        signals = self.get_signals()
        port_map = self.get_port_map()
        test_cases = self.get_test_cases()

        print("ENTITY: \n", entity)
        print("NAME: ",name)
      

    def get_name(self):
        s = ""
        for x in self.lines:
            if "entity" in x:
                s = x[7:-3]
        return s

    def get_description(self):
        s = ""
        start = 0
        end = 0
        for x in self.lines:
            if "DESCRIPTION" in x:
                start = self.lines.index(x)
            if "NOTES" in x:
                end = self.lines.index(x)
        for x in self.lines[start:end]:
            s += x
        return s

    def get_entity(self):
        entity = ""
        start = 0
        end = 0
        for x in self.lines:
            if "entity" in x:
                start = self.lines.index(x)
            if "end " in x:
                end = self.lines.index(x)
                break
        end += 1
        for x in self.lines[start:end]:
            entity += x
        return entity

    def get_ports(self):
        pass

    def get_signals(self):
        pass

    def get_port_map(self):
        pass

    def get_test_cases(self):
        pass

    def path_check(self):
        path = os.path.join(os.path.dirname(__file__), self.filepath)
        ext = os.path.splitext(self.filepath)[-1].lower()
        if ext != ".vhd": 
            print(FileTypeERROR)
            raise SystemExit
        if os.path.exists(path) == False: 
            print(FileNotFoundERROR)
            raise SystemExit
        return path 
    
    def to_string(self):
        print(self.name)
        print(self.description)
        print(self.date)
        print(self.entity)
        print(self.ports)
        print(self.signals)
        print(self.port_map)
        print(self.test_cases)
     