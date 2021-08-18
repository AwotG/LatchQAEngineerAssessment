# QA Engineer Take Home Assessment

Assignment to assess canidates. Detailed instructions found here:
[Instructions](test_instructions.pdf)

## Getting Started

Clone this repository onto your machine with `git clone git@github.com:AwotG/LatchQAEngineerAssessment.git`

### Prerequisites

1. Python 3.6+

### Installing

If you have python version 3.6+, no need to download any additional python packages

### Usage
From the root directory, run

`python3 balance_weighted_scales.py`  

Script uses values found in `user_input.txt`. The restrictions are:

1. ALL values must be non-negative integers i.e. `0, 1, 12934` etc 
2. Scale values must be a total of 2 since the scale has two platforms to hold one weight
3. Weight values must be _at least_ 1 value. 
4. Scale values and weight values are a string representation of a list i.e. `"[1,2,3,4]"`
5. First element of the list is Scale values, Second Element of the list are Weight Values

**Example of valid input** 

`["[5, 9]", "[1, 2, 6, 7]"]`

**Example of invalid input (non-integer)**

`["[5, QSA]", "[1, 2, 6, 7]"]`

**(too few scale values)**

`["[5]", "[1, 2, 6, 7]"]`


## Running the tests

Uses python's built in `unittest`. To run all tests, navigate to root directory of repository and run

` python -m unittest -v`

If you would like to output test results to a log file, you can run 

` python -m unittest -v 2>&1 | tee "test-results-$(date +%Y-%H:%M).log"`

This will output the test results on the termainl and also output to the current directory as a log file, with 
the name as the current date and time.  

### Notes on Script and Approach

To preserve input format, I opted to use a `.txt` file it.  

This is very error prone when humans are entering values, hence some extra validation. If this were coming from a log,
it would not be as big of an issue.

If this were to be used by developers then a better option would be a class or running the script with command line prompts.
If this were for non-developers a very simple GUI would be easiest for any one to use.  

If this were an actual consumer product and needed to be tested:
1. What metric system are we using?
2. What language?
3. Is this for non-developers and will be using GUI? Would need to test the interface
4. Will this be updated frequently? A round of manual tests should be built first and then if this becomes bigger than a 
a Continous Integration system should be created (That way less strain on developers).
5. Will this be for just one platform (Mac vs PC), will this be on mobile or transition into a webapp? Deployment and testing 
differs for each method and would need to be tested
