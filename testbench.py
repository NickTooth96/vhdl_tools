import os
import datetime
import toml

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
    types = {}
    name = ""
    creator = ""
    description = ""
    date = datetime.datetime.now().strftime("%x")
    entity = []
    ports = {}
    signals = {}
    port_map = []
    test_cases = {}
    lines = []
    filepath = ""
    ports_string = ""
    signals_string = ""
    pmap_string = ""
    test_string = ""
    template_lines = []
    libraries = ""
    generics = ""
    config_filepath = "./config.toml"
    clock = ""

    def __init__(self, filepath, data=None):

        self.filepath = filepath
        self.data = data
        
        p = self.path_check()
        f = open(p, "r+")

        i = 0
        for line in f:
            self.lines.append(line)
            i += 1

        self.types = self.get_types()
        self.libraries = self.get_libraries()
        self.generics = self.get_generics()
        self.name = self.get_name()
        self.creator = self.get_creator()
        self.description = self.get_description()
        self.date = datetime.datetime.now().strftime("%x")
        self.entity = self.get_entity()
        self.ports = self.get_ports()
        self.signals = self.get_signals()
        self.port_map = self.get_port_map()
        self.test_cases = self.get_test_cases()
        self.ports_string = self.get_ports_string()
        self.signals_string = self.get_signals_string()
        self.pmap_string = self.get_pmap_string()
        self.test_string = self.get_test_string()
        self.bit_width = self.get_bit_width()
        self.clock = self.get_clock()

        p = self.path_check("./tb_template.vhd")
        self.output_file = open(p, "r+")
     
    ### getter functions

    def get_types(self):
        self.types["NAME"] = str(type(self.name))
        self.types["CREATOR"] = str(type(self.creator))
        self.types["DESCRIPTION"] = str(type(self.description))
        self.types["DATE"] = str(type(self.date))
        self.types["ENTITY"] = str(type(self.entity))
        self.types["PORTS"] = str(type(self.ports))
        self.types["SIGNALS"] = str(type(self.signals))
        self.types["PORT MAP"] = str(type(self.port_map))
        self.types["TESTS"] = str(type(self.test_cases))
        return self.types
    
    def get_clock(self):
        s = "cCLK_PER"
        return s

    def get_bit_width(self):
        for x in self.lines:
            if " N " in x:
                self.bit_width = x.split(":=")[1]
            else:
                self.bit_width = 32
        return self.bit_width
    
    def get_libraries(self):
        s = ""
        start = 0
        end = 0
        for x in self.lines:
            if "library" in x:
                start = self.lines.index(x)
            if "entity" in x:
                end = self.lines.index(x)
        for x in self.lines[start:end]:
            s += x
        return s.strip()
    
    def get_generics(self):
        s = ""
        start = 0
        end = 0
        for x in self.lines:
            if "generic" in x:
                start = self.lines.index(x)
            if "end" in x:
                end = self.lines.index(x)
        if start == 0:
            s = "generic(gCLK_HPER   : time := 10 ns);"
        else:
            for x in self.lines[start:end]:
                s += x
        return s.strip()

    def get_name(self):
        s = ""
        for x in self.lines:
            if "entity" in x:
                s = x[7:-3]
        return s.strip()
    
    def get_creator(self):
        return self.lines[1][3:].strip()

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
        return s[3:].strip()

    def get_entity(self):
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
            self.entity.append(x)
        return self.entity

    def get_ports(self):
        s = ""
        t = {}
        for x in self.entity:
            if " : " in x:
                if "in" in x:
                    t = ["in", x.split(":")[1].split(" ")[2][:-1]]
                else: 
                    t = ["out", x.split(":")[1].split(" ")[2][:-1]]
                if ")" in t[1]:
                    t[1] = t[1][:-2]
                else:
                    t[1] = t[1][:-1]
                s = x.strip()
                if "port(" in s:
                    s = s.split("(")[1]
                    s = s.split(":")[0].strip()
                else:
                    s = s.split(":")[0].strip()
                self.ports[s] = t
        return self.ports

    def get_signals(self):
        for x in self.ports:
            s = ""
            s_init = ""
            if self.ports[x][0] == "in":
                s += "si_"
                if "_" in x:
                    s += x.split("_")[1]
                else:
                    s += x
            else:
                s += "so_"
                if "_" in x:
                    s += x.split("_")[1]
                else:
                    s += x
            s_init = "signal " + s + " : " + str(self.ports[x][1]) + ";"
            self.signals[s] = s_init
        return self.signals

    def get_port_map(self):
        self.port_map.append("test_" + self.name + " : " + self.name)
        self.port_map.append("port map (")
        temp_p = list(self.ports.keys())
        temp_s = list(self.signals.keys())
        for x in self.ports:
            i = temp_p.index(x)
            s = "\t\t" + x + "\t=> " + temp_s[i] + ","
            self.port_map.append(s)
        self.port_map[len(self.port_map)-1] = self.port_map[len(self.port_map)-1][:-1]
        self.port_map.append(");")
        return self.port_map
   
    def get_ports_string(self):
        s = ""
        for x in self.entity:
            if "entity" in x:
                s += ""
            elif "(" in x:
                s += x.split("(")[0] + "(\t" + x.split("(")[1]
            elif "end" in x:
                s += "" 
            else:
                s += "\t\t" + x.strip() + "\n"
        return s.strip()
    
    def get_signals_string(self):
        s = ""
        for x in self.signals:
            s += "\t" + self.signals[x] + "\n"
        return s
    
    def get_pmap_string(self):
        s = ""
        for x in self.port_map:
            buffer = x.split(" ")[0]
            if buffer in self.ports.keys():
                s += "\t" + x + "\n"
            elif ")" in buffer:
                s += "\t" + x
            else:
                s += x + "\n"
        return s

    ### Test Cases

    def get_test_cases(self):
        tests = self.get_config()
        temp_keys = list(tests["test_cases"].keys())
        for x in temp_keys:
            temp_key = x
            cases = []
            for x in tests["test_cases"][x]:
                key = x 
                val = tests["test_cases"][temp_key][x]
                val_type = self.ports[key][1]
                if val_type == "std_logic":
                    val = self.get_binary(val)
                elif val_type == "std_logic_vector":
                    val = self.get_hex(val,self.bit_width)
                temp_p = list(self.ports.keys())
                temp_s = list(self.signals.keys())
                i = temp_p.index(key)
                key = temp_s[i]
                tc = (key,val,val_type)
                cases.append(tc)
                self.test_cases[temp_key] = cases
        return self.test_cases
    
    def get_test_string(self):
        s = ""
        for x in self.test_cases:
            temp_key = x
            s += "\n-- Test Case " + str(temp_key) +"\n"            
            for x in self.test_cases[temp_key]:
                s += "\t"
                s += x[0] + "\t<= " + x[1] + ";\n"
            s += "\twait for cCLK_PER" + self.clock + ";\n"
        return s 
    
    def get_config(self, config_filepath=None):
        if config_filepath:
            data = toml.load(config_filepath, _dict=dict)
        else:
            data = toml.load("config.toml", _dict=dict)
        return data
    
    def get_binary(self, num):
        buffer = bin(int(num)).split("b")[1]
        return "'" + buffer + "'"        
    
    def get_hex(self, num):
        buffer = hex(num).split("x")[1]
        while len(buffer) < 8:
            buffer = "0" + buffer
        out = 'x"' + buffer + '"'
        return out
    
    ### end of getter functions

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

### File Output 

    def generate_tbVHD(self):
        replacements = {"CREATOR": self.creator,"NAME": self.name,"DESCRIPTION": self.description,
                "DATE": self.date,"PORTS": self.ports_string,"SIGNALS": self.signals_string,
                "PORTMAP": self.pmap_string,"TESTCASES": self.test_string, "LIBRARIES": self.libraries, 
                "GENERICS": self.generics}
        filename = "tb_" + self.name.strip() + ".vhd"
        template_p = "./tb_template.vhd"
        self.template_lines = []
        f = open(template_p, "r")
        for line in f:
            self.template_lines.append(line)
        for line in self.template_lines:
            i = self.template_lines.index(line)            
            for x in replacements.keys():
                if x in line:
                    self.find_and_replace(x, replacements[x], i)                    
        out = open(filename, "w")
        for line in self.template_lines:
            out.write(line)
        print("File '" + filename + "' Successfully Created")
    
    def find_and_replace(self, search_key, replace, index):
        self.template_lines[index] = self.template_lines[index].replace(search_key, replace)
        return self.template_lines

    def generate_textfile(self):
        time = {0:"h",1:"m",2:"s"}
        input = str(datetime.datetime.now())
        i = 0
        text_output_filename = ""
        for element in input:
            if element != " ":
                if element != ":":
                    if element != ".":
                        text_output_filename += element
                    else: 
                        text_output_filename += str(time[i])
                        break
                else:
                    text_output_filename += str(time[i])
                    i += 1 
            else:   
                text_output_filename += "_" 
        path = "output/Testbench_" + text_output_filename + ".txt"
        f = open(path, "x")
        f.write("TYPES: \n")
        for x in self.types:
            f.write("\t")
            f.write(x)
            f.write("\t")
            f.write(self.types[x])
            f.write("\n")
        f.write("NAME: \n")
        f.write(self.name)
        f.write("\t")
        f.write("\nCREATOR: \n")
        f.write(self.creator)
        f.write("\nDESCRIPTION: \n")
        f.write(self.description)
        f.write("\nDATE: \n")
        f.write(self.date)
        f.write("\nENTITY: \n")
        for x in self.entity:
            f.write(x)
        f.write("\nPORTS: \n")
        for x in self.ports:
            f.write("\t")
            f.write(x)
            f.write("\t")
            f.write(self.ports[x][0])
            f.write("\t")
            f.write(self.ports[x][1])
            f.write("\n")
        f.write("\nSIGNALS: \n")
        for x in self.signals:
            f.write("\t")
            f.write(x)
            f.write("\t")
            f.write(self.signals[x])
            f.write("\n")
        f.write("\nPORT MAP: \n")
        for x in self.port_map:
            f.write("\t")
            f.write(x)
            f.write("\n")
        f.write("\nTESTS: \n")
        for x in self.test_cases:
            f.write("\t")
            f.write(x)
            f.write("\n")

### MAIN 

# tb = TestBench("./mux2t1.vhd")

# msg = tb.ports
# msg = tb.signals
# msg = tb.port_map
# msg = tb.types
# msg = tb.entity_string
# msg = tb.pmap_string
# msg = tb.bit_width
# msg = tb.test_string
# print(msg)

# print(tb.get_hex(10))
# print(tb.get_binary(5))

      
# tb.to_string()
# tb.generate_tbVHD()
# tb.generate_textfile()



     