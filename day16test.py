from unittest import TestCase, main 
import day16

class TestStep(TestCase):

    known_examples = [ ("1", "100"),
                       ("0", "001"),
                       ("11111", "11111000000"),
                       ("111100001010", "1111000010100101011110000")]

    def test_step(self):
        for a, res in self.known_examples:
            self.assertEqual(res, day16.step(a))

    def test_dragon_curve(self):
        res = day16.dragon_curve("10000", 20)
        self.assertEqual(res, "10000011110010000111")
    

class TestCheckSum(TestCase):

    known_examples = [ ("110010110100", "100") ]
    
    def test_checksum(self):
        for a, res in self.known_examples:
            self.assertEqual(res, day16.checksum(a))
            
    def test_all(self):
        init = "10000"
        disk = day16.dragon_curve(init, 20)
        self.assertEqual(day16.checksum(disk), "01100")
            
            
if __name__ == "__main__":
    main() 
