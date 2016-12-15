from unittest import TestCase, main
import day15 


class TestExample(TestCase):

    def test_simulation(self):
        statue = day15.Statue() 
        
        input = ["Disc #1 has 5 positions; at time=0, it is at position 4.",
                 "Disc #2 has 2 positions; at time=0, it is at position 1."] 

        statue.read_input(input) 

        self.assertFalse(statue.simulate(0)) 
        self.assertTrue(statue.simulate(5))



if __name__ == "__main__": 
 
    main() 
