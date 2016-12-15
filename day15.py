import re 

class Disc:
    
    def __init__(self, positions, start):
        self.positions = positions
        self.start = start 
        self.state = start 

    def tick(self, steps=1):
        self.state += steps
        self.state %= self.positions 

    def slot(self):
        return self.state == 0
        
    def __str__(self):
        return "[{0}]".format(state)
        
class Statue:
 
    discs = []        
    ball = 0 


    def print(self): 
        print("ball", self.ball)
        for i, x in enumerate(self.discs): 
            print("Disc #{0} is in position {1}.".format(i+1, x.state)) 

    def read_input(self, input):
        for line in input:
            line.strip()
            number, positions, start = map(int, re.search('Disc #([0-9]+) has ([0-9]+) positions; at time=0, it is at position ([0-9]+).',
                                                 line).groups())
            assert(number-1 == len(self.discs))
            self.discs.append(Disc(positions, start)) 

            
    def tick(self, steps=1):
        for disc in self.discs:
            disc.tick(steps) 
            
    def balltick(self):
        if self.discs[self.ball].slot():
            self.ball += 1
            return True 
        return False 


    def simulate(self, starttime):
        self.ball = 0
        for d in self.discs:
            d.state = d.start 

        self.tick(starttime+1)

        time = starttime+1
        while True:     
            time += 1
            if not self.balltick():
                return False 
            if self.ball >= len(self.discs):
                print("happy end")
                return True 
            self.tick() 
            


if __name__ == "__main__":
    
    statue = Statue() 

    with open("input15.txt") as file:
        statue.read_input(file)

    # for second part:
    statue.discs.append(Disc(11, 0))
    
    start = 0
    while not statue.simulate(start):
        start += 1
    print(start)
        
