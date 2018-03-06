import unittest

import my_functions

class TestMyFunc(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_increment_one_1(self): 
        self.assertEqual( my_functions.cps6282(4), 16)
  

if __name__ == '__main__':
    unittest.main()

