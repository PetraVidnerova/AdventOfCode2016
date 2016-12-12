CPY = 0
INC = 1
DEC = 2
JNZ = 3
END = 4

class Computer: 

    def __init__(self):
        
        self.register = { 'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0 }
        self.program = [] 

    def parse(self, line):
        """ Parse a line with one instruction, 
            returns a triple. 
        """ 
        vals = line.strip().split()
        if len(vals) < 3:
            vals.append(None)
        if vals[0] == "cpy":
            instr = CPY
        elif vals[0] == "inc":
            instr = INC
        elif vals[0] == "dec":
            instr = DEC
        elif vals[0] == "jnz":
            instr = JNZ
        else:
            raise Exception("parse error", line)

        return((instr, vals[1], vals[2]))


    def read_input(self, input):
        for line in input:
            self.program.append(self.parse(line))
        self.program.append((END, None, None))

    def val(self, s):
        if s in 'abcd':
            return self.register[s]
        else:
            return int(s)

    def run_instr(self, instr):
        """ Perform one instruction, returns False if the program ends,
            True otherwise.
        """
        if instr[0] == CPY:
            self.register[instr[2]] = self.val(instr[1])
            self.index += 1 
  
        elif instr[0] == INC:
            self.register[instr[1]] += 1 
            self.index += 1 

        elif instr[0] == DEC:
            self.register[instr[1]] -= 1
            self.index += 1 
        
        elif instr[0] == JNZ:
            if self.val(instr[1]) != 0:
                self.index += self.val(instr[2])
            else:
                self.index += 1

        elif instr[0] == END:
            return False 

        else:
            raise ValueError("wrong instr", instr[0])

        return True


    def run(self, c=0):

        self.register['c'] = c

        self.index = 0
        while self.run_instr(self.program[self.index]):
            pass
        
        return self.register 



if __name__ == "__main__":
    
    comp = Computer() 

    with open("input12.txt") as file:        
        comp.read_input(file) 

    print(comp.run(1))
        
