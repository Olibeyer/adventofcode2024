import csv
import re

class day3_1:
    def __init__(self, input:str):

        with open(input, 'r') as file:
            self.input_content = file.read()    

    def run(self):
        cmd_list = self.check_for_valid_mul(self.input_content)
        value = 0
        for cmd in cmd_list:
            value += self.call_cmd(cmd)
        print(value)


    def check_for_valid_mul(self, string):
        mul_pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
        try:
            match = re.findall(mul_pattern, string)
            return match
        except AttributeError:
            print('No match')
    
    def call_cmd(self, cmd:str):
        try:
            seperator_index = cmd.find(',')
            number1 = int(cmd[4:seperator_index])
            number2 = int(cmd[seperator_index+1:-1])
        except Exception as e:
            print(cmd)
            raise e

        return number1 * number2
    

    
    def test(self):
        test_string = r"mul(106,680)asdasdmul(106,680)sadmul(106,680)"
        value = 0
        valid_cmds = self.check_for_valid_mul(test_string)
        
        for cmd in valid_cmds:
            value += self.call_cmd(cmd)
            print(value)



class day3_2:
    def __init__(self, input:str):

        with open(input, 'r') as file:
            self.input_content = file.read()    

    def run(self):
        all_enable_matches = self.check_for_valid_enable(self.input_content)
        print(all_enable_matches)
        cmd_list = self.check_for_valid_mul(self.input_content)

        enable = True
        enable_itr = 0
        value = 0
        for cmd in cmd_list:
            cmd_span = cmd.span()
            while enable_itr < len(all_enable_matches) and cmd_span[1] > all_enable_matches[enable_itr].span()[1]:

                if all_enable_matches[enable_itr].group().find(r"don't") != -1:
                    enable = False
                else:
                    enable = True

                enable_itr += 1

            if enable:  
                value += self.call_mul_cmd(cmd)
        print(value)


    def check_for_valid_mul(self, string):
        mul_pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

        try:
            match = re.finditer(mul_pattern, string)
            return match
        except AttributeError:
            print('No match')

    def check_for_valid_enable(self, string):
        do_pattern = re.compile(r"do\(\)")
        dont_pattern = re.compile(r"don't\(\)")

        do_matches = None
        dont_matches = None
        try:
            do_matches = list(re.finditer(do_pattern, string))
        except AttributeError:
            print('No do match')

        try:
            dont_matches = list(re.finditer(dont_pattern, string))
        except AttributeError:
            print('No do match')

        all_matches = dont_matches + do_matches

        # Sort by span (start position)
        sorted_matches = sorted(all_matches, key=lambda m: m.span()[0])
                
        return sorted_matches
    


    def call_mul_cmd(self, cmd):
        try:
            cmd_string = cmd.group()
            seperator_index = cmd_string.find(',')
            number1 = int(cmd_string[4:seperator_index])
            number2 = int(cmd_string[seperator_index+1:-1])
        except Exception as e:
            print(cmd_string)
            raise e

        return number1 * number2


    
    def test(self):
        test_string = r"mul(106,680)asdasdmul(106,680)sadmul(106,680)"
        value = 0
        valid_cmds = self.check_for_valid_mul(test_string)
        
        for cmd in valid_cmds:
            value += self.call_mul_cmd(cmd)
            print(value)



if __name__ == "__main__":
    input = r"C:\Users\OliverBLauritsen\Documents\fun\adventofcode2024\day3\input\input1.txt"
    checker = day3_2(input)
    checker.run()