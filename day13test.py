import unittest 
import day13

class Example(unittest.TestCase): 

    def test(self): 
        """ The lenght of shortest path from [1, 1]
        to [7, 4] is 11. 
        """
        len =  day13.path_len((1, 1), (7, 4))
        self.assertEqual(11, len) 


if __name__ == "__main__":
    unittest.main() 

