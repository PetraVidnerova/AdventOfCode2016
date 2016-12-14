import unittest 
import day14

class TestExample(unittest.TestCase):

    def test_md5(self):
        md5 = day14.produce_md5(18)
        self.assertEqual("cc38887a5" in md5, True)

    def test_triple(self):
        res = day14.find_triple("cc38887a5")
        self.assertEqual(res, '8') 

        res = day14.find_triple("cc388x87a5")
        self.assertEqual(res, None) 

    def test_tuple(self): 
        res = day14.tuple_5('i','x.dkldjiiiiipoas')
        self.assertEqual(res, True)
    
        res = day14.tuple_5('d','x.dkldjiiiiipoas')
        self.assertEqual(res, False)

    def test_is_key(self): 
        self.assertFalse(day14.is_key(18))
        self.assertTrue(day14.is_key(39))

    def test_example(self): 
       index = day14.find_64keys() 
       self.assertEqual(index, 22728)


if __name__ == "__main__":
    unittest.main() 
