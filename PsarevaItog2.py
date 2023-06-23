import unittest
from PsarevaItog import division

class Test_Main(unittest.TestCase):
    def test_A(self):
        self.assertEqual(division(5), 25)
    def test_B(self):
        self.assertNotEqual(division('уттуту'), TypeError)
    def test_C(self):
        self.assertEqual(division(1.2), 1.44)
    def test_D(self):
        self.assertEqual(division(1), 1)
    def test_F(self):
        self.assertNotEqual(division(-5), TypeError)
        
if __name__ == '__main__':
    unittest.main()