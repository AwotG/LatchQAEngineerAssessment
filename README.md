# Latch QA Engineer Take Home Assessment

Latch assignment to assess canidates. Detailed instructions found here:
[Instructions](test_instructions.pdf)

## Getting Started

Clone this repository onto your machine with `git clone {url_link}`

### Prerequisites

1. Python 3.6+

### Installing

If you have python version 3.6+, no need to download any additional python packages

### Usage

To run, enter values in `user_input.txt`. The restrictions are:

1. ALL values must be non-negative integers i.e. 0, 1, 12934 etc 
2. Scale values must be a total of 2 since the scale has two handles
3. Weight values must be _at least_ 1 value. 
4. Scale values and weight values are a string representation of a list i.e. `"[1,2,3,4]"`
5. First element of the list is Scale values, Second Element of the list are Weight Values

**Example of valid input** 

`["[5, 9]", "[1, 2, 6, 7]"]`

**Example of invalid input (non-integer)**

`["[5, QSA]", "[1, 2, 6, 7]"]`

**(too many scale values)**

`["[5]", "[1, 2, 6, 7]"]`


## Running the tests

Uses python's built in `unittest`. To run all tests, navigate to root directory of repository and run

` python -m unittest -v`

###Notes on Script and Approach

To preserve input format, I opted to use a `.txt` file it.  

This is very error prone when humans are entering values, hence some extra validation. If this were coming from a log,
it would not be as big of an issue.

If this were to be used by developers then a better option would be a class or running the script with command line prompts.
If this were for non-developers a very simple GUI would be easiest for any one to use.  

If this were an actual consumer product and needed to be tested:
1. What metric system are we using?
2. What language?



