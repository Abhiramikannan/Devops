import unittest
def add(a,b):
    return a+b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2,3),5," add(2,3) returned some number other than 5")
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2,-3),-5," add(2,3) returned some number other than -5")
    def test_add_positive_numbers(self):
        self.assertEqual(add(-1,2),1," add(2,3) returned some number other than 1")

if __name__ =='__main__':
    unittest.main()