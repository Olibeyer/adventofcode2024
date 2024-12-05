######Another good day
class day5_1:
    def __init__(self, input1:str, input2:str):

        with open(input1, 'r') as file:
            self.rules = file.readlines()
        self.rules = list(
            tuple(map(int, line.strip().split('|')))  # Convert each string to a tuple of floats
            for line in self.rules
        )

        self.followers = [i[1] for i in self.rules]
        self.dependencies = [i[0] for i in self.rules]

        self.all_rules_for_follower = {}

        for i in range(0,len(self.followers)):
            if self.followers[i] in self.all_rules_for_follower.keys():
                self.all_rules_for_follower[self.followers[i]].append(self.dependencies[i])
            else:
                self.all_rules_for_follower[self.followers[i]] = [self.dependencies[i]]

        print(self.all_rules_for_follower)
        
        
        with open(input2, 'r') as file:
            self.updates = file.readlines()

        self.updates = list(
            list(map(int, line.strip().split(',')))
            for line in self.updates
        )
        
    def run(self):
        value = 0
        for update in self.updates:
            if self.check_update_pages(update):
                mid = len(update) // 2
                value += (update[mid] + update[~mid]) / 2
        print(value)



    def check_update_pages(self, update):
        confirmed_values = []

        for i in update:
            #check if i is a follower
            if i in self.all_rules_for_follower.keys():
                #check if dependencies are in update:
                for dep in self.all_rules_for_follower[i]:
                    if dep in update:
                        #dep is in update, then atleast one is required to already be in confimred values
                        if dep not in confirmed_values:
                            return False
            confirmed_values.append(i)
        return True    


class day5_2:
    def __init__(self, input1:str, input2:str):

        with open(input1, 'r') as file:
            self.rules = file.readlines()
        self.rules = list(
            tuple(map(int, line.strip().split('|')))  # Convert each string to a tuple of floats
            for line in self.rules
        )

        self.followers = [i[1] for i in self.rules]
        self.dependencies = [i[0] for i in self.rules]

        self.all_rules_for_follower = {}

        for i in range(0,len(self.followers)):
            if self.followers[i] in self.all_rules_for_follower.keys():
                self.all_rules_for_follower[self.followers[i]].append(self.dependencies[i])
            else:
                self.all_rules_for_follower[self.followers[i]] = [self.dependencies[i]]
        
        
        with open(input2, 'r') as file:
            self.updates = file.readlines()

        self.updates = list(
            list(map(int, line.strip().split(',')))
            for line in self.updates
        )

        print(self.all_rules_for_follower[45])
        print(self.all_rules_for_follower[52])
        
    def run(self):
        value = 0
        bad_updates = []
        good_updates = []
        for update in self.updates:
            if not self.check_update_pages(update):
                bad_updates.append(update)
        for bad_update in bad_updates:
            done_switching = False
            switched_update  =bad_update
            while not done_switching:
                switched_update, done_switching = self.switcharoo(switched_update)
                print(switched_update)

            
            good_updates.append(switched_update)
        
        for update in good_updates:
            value += self.middleNumber(update)
        print(value)
    
    def switcharoo(self, update):
        confirmed_values = []

        for i, follower in enumerate(update):
            #check if i is a follower
            if follower in self.all_rules_for_follower.keys():
                #check if dependencies are in update:
                for dep in self.all_rules_for_follower[follower]:
                    if dep in update:
                        #dep is in update, then atleast one is required to already be in confimred values
                        if dep not in confirmed_values:
                            #get indicies of dep in update
                            dep_indicies = [di for di in range(0, len(update)) if update[di] == dep]
                            buffer_val = update[dep_indicies[0]]
                            update[dep_indicies[0]] = update[i]
                            update[i] = buffer_val
                            return update, False
            confirmed_values.append(follower)
        return confirmed_values, True    


    
    def middleNumber(self, update):
        mid = len(update) // 2
        return (update[mid] + update[~mid]) / 2

    def check_update_pages(self, update):
        confirmed_values = []

        for i in update:
            #check if i is a follower
            if i in self.all_rules_for_follower.keys():
                #check if dependencies are in update:
                for dep in self.all_rules_for_follower[i]:
                    if dep in update:
                        #dep is in update, then atleast one is required to already be in confimred values
                        if dep not in confirmed_values:
                            return False
            confirmed_values.append(i)
        return True    

            

    

if __name__ == '__main__':
    input1 = r"C:\Users\OliverBLauritsen\Documents\fun\adventofcode2024\day5\input\input1.txt"
    input2 = r"C:\Users\OliverBLauritsen\Documents\fun\adventofcode2024\day5\input\input2.txt"
    checker = day5_2(input1, input2)
    checker.run()