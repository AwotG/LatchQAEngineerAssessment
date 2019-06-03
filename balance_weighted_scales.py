import sys
import re
import logging
from itertools import combinations
from pathlib import Path

########################################################################################################################
# Basic Logging (nothing fancy)
########################################################################################################################
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s")


########################################################################################################################
# Constants
########################################################################################################################
SCALE = "scale"
WEIGHT = "weight"
SCRIPT_PATH = Path(__file__).parent


########################################################################################################################
# Gather Input Validation
########################################################################################################################
def parse_user_input_txt(user_input="user_input.txt"):
    user_input_txt_path = SCRIPT_PATH / user_input

    try:
        file = open(user_input_txt_path, "r")
    except FileNotFoundError:
        logging.error(f"\nCan't find the file': '{user_input}'\nFull Path: '{user_input_txt_path}'\nExiting.")
        sys.exit(FileNotFoundError)
    except IOError:
        logging.error(f"\nDoesn't look like you can open the file: '{user_input}'\nFull Path: '{user_input_txt_path}'\nExiting.")
        sys.exit(IOError)
    else:
        line = file.readline()
        scale, weights = re.findall(r'"(.*?)"', line)
        file.close()
        return scale, weights


def validate_and_parse_values(list_of_strings, type):
    """Scale must have only 2 elements, Weights must have at least 1 element """
    length = len(list_of_strings)

    if type.lower() == "scale" and length != 2:
        logging.error(f"\nScale values have too many elements\nExpected 2 but got {length}\n{list_of_strings}")
        sys.exit(ValueError)
    elif type.lower() == "weight" and length < 1:
        logging.error(f"\nWeight values have too many elements\nExpected 1 but got {length}\n{list_of_strings}")
        sys.exit(ValueError)

    result_list = strings_to_ints(list_of_strings, type)

    return result_list


def input_txt_to_values(raw_value, type):
    if type.lower() == SCALE:
        raw_scale_values = list(raw_value.strip("[]").split(","))
        result_values = validate_and_parse_values(raw_scale_values, SCALE)
    elif type.lower() == WEIGHT:
        raw_weight_values = list(raw_value.strip("[]").split(","))
        result_values = validate_and_parse_values(raw_weight_values, WEIGHT)
    else:
        return False
    return result_values


def strings_to_ints(list_of_strings, type):
    """Values must be non-negative integers, scale elements must be 2, weight elements must be at least 1"""
    result = []

    for value in list_of_strings:
        try:
            to_int = int(value)
            if to_int < 0: raise ValueError
        except ValueError:
            logging.error(
                f"Unable to convert {type} value {value} to non-negative integer.\nFull {type} values were {list_of_strings}")
            sys.exit(ValueError)
        else:
            result.append(int(value))
    return sorted(result)


########################################################################################################################
# Balancing scale algorithm
########################################################################################################################
def check_values(scale_list, weight_list):
    LEFT_SCALE = scale_list[0]
    RIGHT_SCALE = scale_list[1]

    if len(weight_list) == 1:
        return check_with_single_weight(LEFT_SCALE, RIGHT_SCALE, weight_list)
    elif len(weight_list) > 1:
        return check_with_two_weights(LEFT_SCALE, RIGHT_SCALE, weight_list)


def check_with_single_weight(left_scale, right_scale, weight_list):
    scale_diff = abs(right_scale-left_scale)
    if scale_diff == weight_list[0]:
        return f"{weight_list[0]}"
    else:
        return "No possible solution. Please try again."


def check_with_two_weights(left_scale, right_scale, weight_list):
    for pair in combinations(weight_list, 2):
        if pair[0] + left_scale == pair[1] + right_scale \
                or pair[0] + right_scale == pair[1] + left_scale\
                or pair[0] + pair[1] + left_scale == right_scale \
                or pair[0] + pair[1] + right_scale == left_scale:
            l, i = min(pair), max(pair)
            return ','.join([str(l), str(i)])
    return "No possible solution. Please try again."


if __name__ == '__main__':
    raw_scale, raw_weights = parse_user_input_txt()
    processed_scale = input_txt_to_values(raw_scale, SCALE)
    processed_weight = input_txt_to_values(raw_weights, WEIGHT)
    output = check_values(processed_scale, processed_weight)
    print(output)