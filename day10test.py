import day10a 
import unittest


class FactoryTest(unittest.TestCase):
    
    input_file = [ "value 5 goes to bot 2",
                   "bot 2 gives low to bot 1 and high to bot 0",
                   "value 3 goes to bot 1",
                   "bot 1 gives low to output 1 and high to bot 0",
                   "bot 0 gives low to output 2 and high to output 0",
                   "value 2 goes to bot 2" ]

    def test_parse(self):
        factory = day10a.Factory()
        factory.parse(self.input_file)
    
    def test_example(self):

        factory = day10a.Factory()
        factory.parse(self.input_file)
        output = factory.run()
        self.assertEqual(output, 30)

if __name__ == "__main__":
    unittest.main()
