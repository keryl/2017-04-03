import unittest
from add import add

class AddTestCase(unittest.TestCase):
    def test_adds_a_number_to_a_list(self):
        list = [10, 2, 3]
        result = add.add([4,5,6])
        self.assertEqual(10, 2, 3, 4, 5, 6, result)

    def test_only_accepts_a_number(self):
        result = add.add(["ten"])
        self.assertEqual("numbers only", result)

    def test_only_accepts_a_list(self):
        self.assertEqual('argument should be of type list', append(1))
        self.assertEqual('argument should be of type list', append(True))
        self.assertEqual('argument should be of type list', append(""))
        self.assertEqual('argument should be of type list', append({}))
        self.assertNotEqual('argument should be of type list', add('test'))

if __name__=="__main__":
    unittest.main()