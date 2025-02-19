import unittest

def same_list(list1,list2):

    return list1 == list2

class TestSortedAscending(unittest.TestCase):
   
    def test_list_equal(self):
        lst1 = [1, 2, 3, 4, 5, 6, 7]
        lst2 = [1, 2, 3, 4, 5, 6, 7]
        print("lists: \n", lst1,"\n",lst2)
        self.assertTrue(same_list(lst1,lst2), "Equal")

    def test_unsorted_list(self):
        lst1 = [1, 2, 3, 4, 5, 6, 7]
        lst2 = [1, 9, 3, 4, 5, 8, 7]
        print("lists: \n", lst1,"\n",lst2)
        self.assertFalse(same_list(lst1,lst2), "Not Equal")


if __name__ == '__main__':
    unittest.main()