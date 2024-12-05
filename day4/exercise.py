########This day is a GOOD DAY###############

class day4_1:
    def __init__(self, input:str):
        self.direction_lookup = {'N' : (-1,0), 'NE' : (-1,1), 'E' : (0,1), 'SE' : (1,1), 'S' : (1,0), 'SW' : (1,-1), 'W' : (0,-1), 'NW' : (-1,-1)}

        with open(input, 'r') as file:
            self.input_content = file.readlines()

    def run(self):
        xmas_counter = 0
        for y, line in enumerate(self.input_content):
            for x,c in enumerate(line):
                if c == 'X':
                    matches = self.word_search_matcher(y,x)
                    xmas_counter += matches
        print(xmas_counter)
    
    def word_search_matcher(self, y:int, x:int):
        matches = 0
        for (direction, coord_diff) in self.direction_lookup.items():
            check_coords = (y+coord_diff[0], x+coord_diff[1])

            #Check if corrds are out of bounds
            if  check_coords[0] >= 140 or check_coords[0] < 0 or check_coords[1] >=140 or check_coords[1] < 0:
                continue
            if self.input_content[check_coords[0]][check_coords[1]] == 'M':
                if self.check_direction(direction, check_coords[0], check_coords[1]):
                    matches += 1
        return matches

    def check_direction(self,direction, y, x):
        coord_diff = self.direction_lookup[direction]
        check_coords = (y+coord_diff[0], x+coord_diff[1])
        if check_coords[0] >= 140 or check_coords[0] < 0 or check_coords[1] >=140 or check_coords[1] < 0:
            return False
        
        if self.input_content[check_coords[0]][check_coords[1]] == 'A':
            check_coords = (check_coords[0]+coord_diff[0], check_coords[1]+coord_diff[1])
            if check_coords[0] >= 140 or check_coords[0] < 0 or check_coords[1] >=140 or check_coords[1] < 0:
                return False
            
            if self.input_content[check_coords[0]][check_coords[1]] == 'S':
                return True
        
        return False

class day4_2:
    def __init__(self, input:str):
        self.direction_lookup = {'NE' : (-1,1), 'SE' : (1,1),  'SW' : (1,-1), 'NW' : (-1,-1)}
        self.A_coords = []
        with open(input, 'r') as file:
            self.input_content = file.readlines()

    def run(self):
        xmas_counter = 0
        for y, line in enumerate(self.input_content):
            for x,c in enumerate(line):
                if c == 'M':
                    self.word_search_matcher(y,x)
                
        res = list(set([ele for ele in self.A_coords 
            if self.A_coords.count(ele) > 1]))
        print(len(res)) 
    
    def word_search_matcher(self, y:int, x:int):
        for (direction, coord_diff) in self.direction_lookup.items():
            check_coords = (y+coord_diff[0], x+coord_diff[1])

            #Check if corrds are out of bounds
            if  check_coords[0] >= 140 or check_coords[0] < 0 or check_coords[1] >=140 or check_coords[1] < 0:
                continue
            if self.input_content[check_coords[0]][check_coords[1]] == 'A':
                if self.check_direction(direction, check_coords[0], check_coords[1]):
                    self.A_coords.append(check_coords)

    def check_direction(self,direction, y, x):
        coord_diff = self.direction_lookup[direction]
        check_coords = (y+coord_diff[0], x+coord_diff[1])
        if check_coords[0] >= 140 or check_coords[0] < 0 or check_coords[1] >=140 or check_coords[1] < 0:
            return False
        
        if self.input_content[check_coords[0]][check_coords[1]] == 'S':
            check_coords = (check_coords[0]+coord_diff[0], check_coords[1]+coord_diff[1])
            return True
        
        return False



if __name__ == "__main__":
    input = r"C:\Users\OliverBLauritsen\Documents\fun\adventofcode2024\day4\input\input1.txt"
    checker = day4_2(input)
    checker.run()