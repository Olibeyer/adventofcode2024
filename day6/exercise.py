import numpy as np
import time

class day6_1:
    def __init__(self, input:str):
        
        self.directions = {"v" : "up", "^" : "down", "<" : "left", ">" : "right"}
        self.list_directions = ["up", "right", "down", "left"]
        self.direction_index = 0

        with open(input, 'r') as file:
            self.map = file.readlines()
        #self.map = [line.strip() for line in self.map]
        self.find_start_position()
        self.direction_index = self.list_directions.index(self.current_directon)
        
    def run(self):
        total_steps = 1
        while self.current_position[1] < len(self.map) and self.current_position[0] < len(self.map[0]) and self.current_position[0] > 0 and self.current_position[1] > 0:
            if self.take_step():
                total_steps += 1
        print(total_steps)


    def find_start_position(self):
        for y, line in enumerate(self.map):
            for x, c in enumerate(line):
                if c in self.directions.keys():
                    self.current_directon = self.directions[c]
                    self.current_position = (x,y)  


    def take_step(self):

        match self.current_directon:
            case "up":
                next_postion = (self.current_position[0],self.current_position[1]+1) 
            case "down":
                next_postion = (self.current_position[0],self.current_position[1]-1)

            case "left":
                next_postion = (self.current_position[0]+1,self.current_position[1]) 
                
            case "right":
                next_postion = (self.current_position[0]-1,self.current_position[1]) 

        if next_postion[1] > len(self.map)-1 or next_postion[0] > len(self.map[0])-1 or next_postion[1] < 0 or next_postion[0] < 0:
            self.current_position = next_postion
            return False
        try:
            if self.map[next_postion[1]][next_postion[0]] == '#': 
                if self.direction_index < len(self.list_directions)-1:
                    self.direction_index += 1
                else:
                    self.direction_index = 0
                self.current_directon = self.list_directions[self.direction_index]
                return False
        except Exception as e:
            print(next_postion)
            print(len(self.map))
            print(len(self.map[0]))

        self.current_position = next_postion
        if  self.map[next_postion[1]][next_postion[0]] == 'X' or self.map[next_postion[1]][next_postion[0]] in self.directions.keys():
            return False
        self.map[self.current_position[1]]= self.map[self.current_position[1]][:self.current_position[0]] +"X" + self.map[self.current_position[1]][self.current_position[0]+1:]
        with open(r"C:\Users\olive\Documents\adventofcode2024\day6\input\debug.txt", 'w') as file:
           file.writelines(self.map)
           file.close()

        return True  


if __name__ == '__main__':
    checker = day6_1(input=rf"C:\Users\olive\Documents\adventofcode2024\day6\input\input1.txt")
    checker.run()
    #print(checker.map)