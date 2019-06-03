import unittest
import logging
from pathlib import Path

from balance_weighted_scales import(
    parse_user_input_txt,
    validate_and_parse_values,
    input_txt_to_values,
    check_with_single_weight,
    check_with_two_weights)

logging.disable(logging.CRITICAL)

class TestUserInput(unittest.TestCase):


    def test_user_input_file_can_not_be_found(self):
        file_name = "blurg"
        with self.assertRaises(SystemExit) as ce:
            parse_user_input_txt(file_name)
        self.assertEqual(ce.exception.code, FileNotFoundError)


    def test_user_input_file_can_not_be_opened(self):
        dir_name = "dummy"
        dir_path = Path(__file__).parent / dir_name
        dir_path.mkdir(exist_ok=True)

        with self.assertRaises(SystemExit) as ce:
            parse_user_input_txt(dir_name)
        self.assertEqual(ce.exception.code, IOError)

        dir_path.rmdir()

    def test_scale_values_too_many(self):
        value = ["1", "-1", "0"]
        with self.assertRaises(SystemExit) as ce:
            validate_and_parse_values(value,"scale")
        self.assertEqual(ce.exception.code, ValueError)

    def test_scale_values_too_few(self):
        value = ["1"]
        with self.assertRaises(SystemExit) as ce:
            validate_and_parse_values(value,"scale")
        self.assertEqual(ce.exception.code, ValueError)

    def test_weight_values_too_few(self):
        value = []
        with self.assertRaises(SystemExit) as ce:
            validate_and_parse_values(value,"weight")
        self.assertEqual(ce.exception.code, ValueError)


    def test_list_strings_element_value_is_not_non_negative_integer(self):
        value = ["q"]
        with self.assertRaises(SystemExit) as ce:
            validate_and_parse_values(value,"scale")
        self.assertEqual(ce.exception.code, ValueError)


    def test_parsed_txt_to_int_list(self):
        input = "[1,2]"
        expected = [1,2]
        self.assertEqual(input_txt_to_values(input,"scale"), expected)


    def test_single_weight_answer_true(self):
        left_scale = 3
        right_scale = 4
        weights = [1]
        self.assertEqual(
            check_with_single_weight(left_scale,right_scale,weights),
            "1")

    def test_single_weight_answer_false(self):
        left_scale = 3
        right_scale = 4
        weights = [2]
        self.assertEqual(
            check_with_single_weight(left_scale,right_scale,weights),
            "No possible solution. Please try again.")


    def test_two_weight_answer_true(self):
        left_scale = 13
        right_scale = 4
        weights = [1, 2, 3, 6, 14]
        self.assertEqual(
            check_with_two_weights(left_scale,right_scale,weights),
            "3,6")

    def test_two_weight_answer_true(self):
        left_scale = 13
        right_scale = 4
        weights = [1, 2, 6, 14]
        self.assertEqual(
            check_with_two_weights(left_scale, right_scale,weights),
            "No possible solution. Please try again.")


if __name__ == '__main__':
    unittest.main()