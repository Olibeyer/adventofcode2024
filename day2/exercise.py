import csv
import numpy as np

class day2_1:
    def __init__(self, input:str):
        self.reports = []
        with open(input, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=' ')
            for row in csv_reader:
                self.reports.append([int(i) for i in row])
            print(self.reports)

    def run(self):
        safe_reports = 0
        for report in self.reports:
            if self.check_report(report):
                safe_reports += 1
        print(safe_reports)
    
    def check_report(self, report):
        last_digit = report[0]
        acending = None
        for i in range(1, len(report)):
            next_digit = report[i]
            
            ##cant be the same
            if next_digit == last_digit:
                return False
            
            if acending is None:
                if next_digit > last_digit:
                    acending = True
                else:
                    acending = False
            
            #needs to only acend or decent
            if next_digit > last_digit and not acending:
                return False
            if next_digit < last_digit and acending:
                return False
            
            #cannot change with more than 3
            if abs(next_digit - last_digit) > 3:
                return False
            last_digit = next_digit
        
        return True
    
    def test_report_check(self):
        test = [7, 6 ,4, 2, 1]
        print(self.check_report(test))

################################# EEEUUUUUUGHHH###########
class day2_2:
    def __init__(self, input:str):
        self.reports = []
        with open(input, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=' ')
            for row in csv_reader:
                self.reports.append([int(i) for i in row])

    def run(self):
        safe_reports = 0
        for report in self.reports:
            if self.check_report(report):
                safe_reports += 1
        print(safe_reports)
    
    def check_report(self, report):
        last_digit = report[0]
        acending = None
        
        can_remove_issue = True

        acending = self.check_report_ascending(report=report)

        test_report = report[1:]
        last_digit = test_report[0]
        for i in range(1, len(test_report)):
            
            next_digit = test_report[i]
            
            ##cant be the same
            if next_digit == last_digit:
                break
            
            #needs to only acend or decent
            if next_digit > last_digit and not acending:
                break
            
            if next_digit < last_digit and acending:
                break
            
            #cannot change with more than 3
            if abs(next_digit - last_digit) > 3:
                break
                
            last_digit = next_digit

            if i == len(test_report)-1:
                return True

        last_digit = report[0]
        for i in range(1, len(report)):
            
            next_digit = report[i]
            
            ##cant be the same
            if next_digit == last_digit:
                if can_remove_issue:
                    can_remove_issue = False
                    continue
                    
                else:
                    return False
            
            #needs to only acend or decent
            if next_digit > last_digit and not acending:
                if can_remove_issue:
                    can_remove_issue = False
                    continue
                else:
                    return False
            
            if next_digit < last_digit and acending:
                if can_remove_issue:
                    can_remove_issue = False
                    continue
                else:
                    return False
            
            #cannot change with more than 3
            if abs(next_digit - last_digit) > 3:
                if can_remove_issue:
                    can_remove_issue = False
                    continue
                else:
                    return False
                
            last_digit = next_digit    
        return True
    
    def check_report_ascending(self, report):
        acending_counter = 0
        last_lvl = None
        for lvl in report:
            if last_lvl is None:
                last_lvl = lvl
                continue
            if lvl > last_lvl:
                acending_counter += 1
            last_lvl = lvl
        
        if acending_counter >= len(report)/2:
            return True
        return False
            
    def test_report_check(self):
        test = [2, 1 ,2,3, 4]
        print(self.check_report(test))

if __name__ == "__main__":
    input = r"C:\Users\OliverBLauritsen\Documents\fun\adventofcode2024\day2\input\input1.txt"
    checker = day2_2(input)
    checker.run()