import unittest 
import day13

class Example(unittest.TestCase): 

    def test(self): 
        len =  day13.path_len((1, 1), (7, 4))
        self.assertEqual(11, len) 


if __name__ == "__main__":
    unittest.main() 

