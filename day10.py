import re 
            
class Factory:

    def __init__(self):
        self.bots = {}
        self.outputs = {}
        self.bot_values = []  

        self.match_value = re.compile(r'value ([0-9]+) goes to bot ([0-9]+)')
        self.match_lowhigh = re.compile(r'bot ([0-9]+) gives low to (output|bot) ([0-9]+) and high to (output|bot) ([0-9]+)')
        
        
    def process(self, line):
        """ Parsed one line of input, saves the values and sets the bot's rules.
        """ 
        if line.startswith("value"):
            value, bot = map(int, self.match_value.search(line).groups())
            self.bot_values.append((bot, value))
            
        elif line.startswith("bot"):
            bot, what_low, number_low, what_high, number_high = self.match_lowhigh.search(line).groups()
            bot, number_low, number_high = int(bot), int(number_low), int(number_high) 

            if bot not in self.bots:
                self.bots[bot] = Bot(bot)
            self.bots[bot].set_rule(what_low, number_low, what_high, number_high)

        else:
            raise Exception("parse error", line)

    def parse(self, f):
        for line in f:
            self.process(line)
        
    def run(self):

        for bot, value in self.bot_values:

            if bot not in self.bots:
                self.bots[bot] = Bot(bot)
            self.bots[bot].set_chip(self, value)

        return self.outputs[0] * self.outputs[1] * self.outputs[2]
            
    def set_output(self, number, chip):
        self.outputs[number] = chip 

    def set_bot(self, number, chip):
        if number not in self.bots:
            self.bots[number] = Bot(number)
        self.bots[number].set_chip(self, chip)
        
class Bot:

    def __init__(self, number):
        self.number = number
        self.chip1, self.chip2 = None, None     #chip numbers
        # the rule 
        self.low, self.high = None, None       #where to go low and high
        self.who_low, self.who_high = None, None # low and high output or bot

    def __str__(self):
        return "["+ str(self.chip1) + "," + str(self.chip2) + "]"

    def set_rule(self, who_low, low, who_high, high):
        self.who_low = who_low
        self.low = low
        self.who_high = who_high
        self.high = high
    
    def set_chip(self, factory, number):
        if self.chip1 is not None and self.chip2 is not None:
            raise Exception("third chip")
        
        if self.chip1 is None:
            self.chip1 = number
            return

        if self.chip2 is None:
            self.chip2 = number

            # we have reached two chips, sort them 
            if self.chip1 > self.chip2:
                self.chip1, self.chip2 = self.chip2, self.chip1

            # solution of part1: 
            if self.chip1 == 17 and self.chip2 == 61:
                print("--->", self.number)

            self.proceed(factory)

    def proceed(self, factory):
        """ Proceed chips to outputs or other bots.
        """
        if self.who_low == "output":
            factory.set_output(self.low, self.chip1)
        else:
            factory.set_bot(self.low, self.chip1)
            
        if self.who_high == "output":
            factory.set_output(self.high, self.chip2)
        else:
            factory.set_bot(self.high, self.chip2)
    

if __name__ == "__main__":
    
    factory = Factory()

    with open("input10.txt") as file:
        factory.parse(file)

    print(factory.run())
