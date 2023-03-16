import os
import datetime
import toml

__version__ = "1.0.0"
__AUTHOR__ = "Nicholas Toothaker"

class TestCases:

    def __init__(self):
        self.test_cases = self.get_test_cases()
        self.test_string = self.get_test_string()

    def get_test_cases(self):
        tests = self.get_config()
        print(tests)
        temp_keys = list(tests["test_cases"].keys())
        for x in temp_keys:
            temp_key = x
            for x in tests["test_cases"][x]:
                s = x 
                t = tests["test_cases"][temp_key][x]
                print(s,t)
                self.make_test_case(s,t, None)
        return tests
    
    def make_test_case(self, key, value, val_type):
        return (key, value, val_type)


    def get_test_string(self):
        return "NO DATA"  
    
    def get_config(self, config_filepath=None):
        if config_filepath:
            data = toml.load(config_filepath, _dict=dict)
        else:
            data = toml.load("config.toml", _dict=dict)
        return data