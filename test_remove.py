import unittest
from remove import remove

class RemoveTestCase(unittest.TestCase):
    def test_removes_a_number_from_a_list(self):
        list = [10, 2, 3, 4, 5, 6]
        result = remove.remove([4,5, 6])
        self.assertEqual(10, 2, 3, result)

    def test_only_accepts_a_number(self):
        result = remove.remove(["ten"])
        self.assertEqual("numbers only", result)

    def test_only_accepts_a_list(self):
        self.assertEqual('argument should be of type list', remove(1))
        self.assertEqual('argument should be of type list', remove(True))
        self.assertEqual('argument should be of type list', remove(""))
        self.assertEqual('argument should be of type list', remove({}))
        self.assertNotEqual('argument should be of type list', remove('test'))

if __name__=="__main__":
    unittest.main()