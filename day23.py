CPY = 0
INC = 1
DEC = 2
JNZ = 3
END = 4
TGL = 5

class Computer: 

    def __init__(self):
        
        #self.register = { 'a' : 12, 'b' : 0, 'c' : 0, 'd' : 0 }
        self.register = [ 12, 0, 0, 0 ]
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
        elif vals[0] == "tgl":
            instr = TGL
        else:
            raise Exception("parse error", line)

        return([instr, vals[1], vals[2]])


    def read_input(self, input):
        for line in input:
            self.program.append(self.parse(line))
        self.program.append([END, None, None])

    def val(self, s):
        if s in 'abcd':
            return self.register[ord(s)-ord('a')]
        else:
            return int(s)

    def get_idx(self, s):
        if s is None:
            return None
        if s  in 'abcd':
            return ord(s)-ord('a')
        return None
    
    def run_instr(self, instr):
        """ Perform one instruction, returns False if the program ends,
            True otherwise.
        """
        if instr[0] == CPY:
            idx = self.get_idx(instr[2])
            if idx is not None:
                self.register[idx] = self.val(instr[1])
            self.index += 1 
  
        elif instr[0] == INC:
            idx = self.get_idx(instr[1])
            if idx is not None:
                self.register[idx] += 1 
            self.index += 1 

        elif instr[0] == DEC:
            idx = self.get_idx(instr[1])
            if idx is not None:
                self.register[idx] -= 1
            self.index += 1 
        
        elif instr[0] == JNZ:
            if self.val(instr[1]) != 0:
                self.index += self.val(instr[2])
            else:
                self.index += 1

        elif instr[0] == TGL:
            idx = self.index + self.val(instr[1])
            if idx > len(self.program) - 1:
                self.index += 1
                return True
            if self.program[idx][0] == INC:
                self.program[idx][0] = DEC
            elif self.program[idx][2] is None:
                self.program[idx][0] = INC
            elif self.program[idx][0] == JNZ:
                self.program[idx][0] = CPY
            else:
                self.program[idx][0] = JNZ
            self.index += 1
            
        elif instr[0] == END:
            return False 

        else:
            raise ValueError("wrong instr", instr[0])

        return True


    def run(self):

        self.index = 0
        i = 0
        while self.run_instr(self.program[self.index]):
            if self.index >= len(self.program):
                break
            if i % 1000000 == 0:
                print(i // 1000000, self.register)
            i += 1
        
        return self.register 



if __name__ == "__main__":
    
    comp = Computer()

    with open("input23.txt") as file:        
        comp.read_input(file) 

    print(comp.run())
        
