import unittest 
import day12

class Example(unittest.TestCase): 

    input = [ "cpy 41 a",
              "inc a",
              "inc a",
              "dec a",
              "jnz a 2",
              "dec a" ] 

    def test(self): 
        comp = day12.Computer() 
        comp.read_input(self.input)
        self.assertEqual(comp.run()['a'], 42)

if __name__ == "__main__":
    unittest.main()
