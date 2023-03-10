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

        self.name = self.get_name()
        self.description = self.get_description()
        self.date = datetime.datetime.now().strftime("%x")
        self.entity = self.get_entity()
        self.ports = self.get_ports()
        self.signals = self.get_signals()
        self.port_map = self.get_port_map()
        self.test_cases = self.get_test_cases()

        p = self.path_check("./tb_template.vhd")
        self.output_file = open(p, "r+")

        # print("ENTITY: \n", entity)
        # print("NAME: ", name)
        # print("SIGNALS: \n", signals)
        # print("PORTS: \n", ports)
      

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
        component = ""
        start = 0
        end = 0
        for x in self.lines:
            if "component " in x:
                start = self.lines.index(x)
            if "end component" in x:
                end = self.lines.index(x)
                break
        end += 1
        for x in self.lines[start:end]:
            component += x
        return component

    def get_signals(self):
        signals = ""
        for x in self.lines:
            if "signal" in x:
                signals += x
            if "begin " in x:
                break
        return signals

    def get_port_map(self):
        pass

    def get_test_cases(self):
        pass

    def path_check(self, fpath=None):
        if fpath == None:
            path = os.path.join(os.path.dirname(__file__), self.filepath)
        else:
            path = os.path.join(os.path.dirname(__file__), fpath)
        ext = os.path.splitext(self.filepath)[-1].lower()
        if ext != ".vhd": 
            print(FileTypeERROR)
            raise SystemExit
        if os.path.exists(path) == False: 
            print(FileNotFoundERROR)
            raise SystemExit
        return path 
    
    def output_to_file(self):
        for line in self.output_file:
            if "<name>" in line:
                search = "{name}"
                s = line
                print(s)
                s.replace("<name>", self.name)
                print(s)
    
    def replace_line(self, line):
        pass

    def to_string(self):
        print("NAME: \n",self.name)
        print("DESCRIPTION: \n",self.description)
        print("DATE: \n",self.date)
        print("ENTITY: \n",self.entity)
        print("PORTS: \n",self.ports)
        print("SIGNALS: \n",self.signals)
        print("PORT MAP: \n",self.port_map)
        print("TESTS: \n",self.test_cases)

tb = TestBench("./mux2t1.vhd")
# tb.to_string()
tb.output_to_file()


     