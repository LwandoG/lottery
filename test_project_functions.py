import unittest
import project_functions


class TestProjectFunctions(unittest.TestCase):
    # In this class we deal with the unittest for most function defined in project_functions
    # there is nothing much to comment on.
    def test_age_test(self):
        self.assertTrue(project_functions.age_test(20), "Should be True")
        self.assertFalse(project_functions.age_test(9), "Should be False")

    def test_selection_sort(self):
        my_list = [1, 5, 14, 18, 24, 36]
        sec_list = project_functions.selection_sort(my_list)
        self.assertTrue(all(sec_list[i] <= sec_list[i+1] for i in range(len(sec_list) - 1)), "Should be True")
        self.assertFalse(all(sec_list[i] > sec_list[i+1] for i in range(len(sec_list) - 1)), "Should be False")

    def test_swap(self):
        self.assertEqual(project_functions.swap([1, 5, 3, 2], 1, 3), [1, 2, 3, 5], "Should swap")

    def test_count_matches(self):
        self.assertEqual(project_functions.count_matches([4, 15, 26, 38, 41, 47], [2, 4, 9, 15, 23, 47]), 3, "Should be 3")