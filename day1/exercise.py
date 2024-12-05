import csv

class day1_1:
    def __init__(self, input:str):
        self.list1 = []
        self.list2 = []
        with open(input, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=' ')
            for row in csv_reader:
                # Access the two columns using indices
                column1, column2 = row[0], row[3]
                self.list1.append(int(column1))
                self.list2.append(int(column2))
        self.run()
    
    def run(self):
        self.list1.sort()
        self.list2.sort()
        total_dist = 0
        for i in range(0,len(self.list1)):
            total_dist += abs(self.list1[i] - self.list2[i])
        print(total_dist)

class day1_2:
    def __init__(self, input:str):
        self.list1 = []
        self.list2 = []
        with open(input, mode='r') as file:
            csv_reader = csv.reader(file, delimiter=' ')
            for row in csv_reader:
                # Access the two columns using indices
                column1, column2 = row[0], row[3]
                self.list1.append(int(column1))
                self.list2.append(int(column2))
        self.run()
    
    def run(self):
        self.list1.sort()
        self.list2.sort()
        similarity = 0
        for i in range(0,len(self.list1)):
            similarity += self.list1[i]*self.list2.count(self.list1[i])

        print(similarity)



if __name__ == "__main__":
    input = r"C:\Users\OliverBLauritsen\Documents\fun\adventofcode2024\day1\input\input1.txt"
    day1_2(input)