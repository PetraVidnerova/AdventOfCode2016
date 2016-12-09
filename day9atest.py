from day9a import decompress
import unittest

class Examples(unittest.TestCase):

    known_values = ( ('ADVENT', 6),
                     ('(3x3)XYZ', 9),
                     ('X(8x2)(3x3)ABCY', 20),
                     ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
                     ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445)
                     )

    def test_examples(self):
        for s, length in self.known_values:
            self.assertEqual(decompress(s), length)

    def test_input(self):
        with open("input9.txt") as file:
            compressed_string = file.read().strip()
        self.assertEqual(decompress(compressed_string), 10780403063)


            
if __name__ == "__main__":
    unittest.main()
                     

                     


