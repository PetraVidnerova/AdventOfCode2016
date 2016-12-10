import re 

            
class Factory:

    def __init__(self):
        self.bots = {}
        self.outputs = {}
        self.bot_values = []  
    
    def process(self, line):
        match_value = re.compile(r'value ([0-9]+) goes to bot ([0-9]+)')
        match_lowhigh = re.compile(r'bot ([0-9]+) gives low to (output|bot) ([0-9]+) and high to (output|bot) ([0-9]+)')
        
        if line.startswith("value"):
            value, bot = map(int, match_value.search(line).groups())
            #print("value", value, bot)
            self.bot_values.append((bot, value))
            
        elif line.startswith("bot"):
            bot, what_low, number_low, what_high, number_high = match_lowhigh.search(line).groups()
            bot, number_low, number_high = int(bot), int(number_low), int(number_high) 
            #print(bot, what_low, number_low, what_high, number_high)
            if bot not in self.bots:
                self.bots[bot] = Bot(bot)
            self.bots[bot].set_rule(what_low == "output", number_low,
                                    what_high == "output", number_high)
        else:
            raise Exception("parse error", line)

    def parse(self, f):
        for line in f:
            self.process(line)
        
    def run(self):
        for bot, value in self.bot_values:
            if bot not in self.bots:
                self.bots[bot] = Bot(bot)
            print("set chip", bot, value)
            self.bots[bot].set_chip(self, value)

        print("Outputs", self.outputs)
        print("bots", self.bots)
        for i in self.bots:
            print(i, self.bots[i])
        return self.outputs[0] * self.outputs[1] * self.outputs[2]
            
    def set_output(self, number, chip):
        print("set ouput", number, chip)
        self.outputs[number] = chip 

    def set_bot(self, number, chip):
        print("set_chip", number, chip)
        if number not in self.bots:
            self.bots[number] = Bot(number)
        self.bots[number].set_chip(self, chip)
        
class Bot:

    def __init__(self, number):
        self.number = number
        self.chip1, self.chip2 = None, None     #chip numbers 
        self.low, self.high = None, None       #where to go low and high
        self.low_output, self.high_ouput = False, False # low and high output or bot

    def __str__(self):
        return "["+ str(self.chip1) + "," + str(self.chip2) + "]"

    def set_rule(self, low_output, low, high_output, high):
        self.low_output = low_output
        self.low = low
        self.high_output = high_output
        self.high = high
    
    def set_chip(self, factory, number):
        if self.chip1 is not None and self.chip2 is not None:
            raise Exception("third chip")
        
        if self.chip1 is None:
            self.chip1 = number
            return

        if self.chip2 is None:
            self.chip2 = number
            #proceed
            if self.chip1 > self.chip2:
                self.chip1, self.chip2 = self.chip2, self.chip1

            # solution of part1: 
            #if self.chip1 == 17 and self.chip2 == 61:
            #    print("--->", self.number)
            #    quit()
                
            if self.low_output:
                factory.set_output(self.low, self.chip1)
            else:
                factory.set_bot(self.low, self.chip1)
                
            if self.high_output:
                factory.set_output(self.high, self.chip2)
            else:
                factory.set_bot(self.high, self.chip2)
    

if __name__ == "__main__":
    factory = Factory()
    with open("input10.txt") as file:
        factory.parse(file)
    print(factory.run())
