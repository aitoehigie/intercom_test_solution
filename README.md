# Intercom Test Solution

This is a little program that will read a JSON file that contains the full list of customers and output
the names and user ids of matching customers (within 100km) of Intercom Dublin offices, sorted by User ID (ascending).
Why? They are good guys and want to invite them for some food and drinks :) .

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed for this script to run:
1. Python 3
2. Click 
3. ujson
4. tabulate
5. pipenv
6. Pytest

### Installing

1. Install pipenv first by running this command:
"pip install pipenv"
2. Create a virtual environment by running this command:
"pipenv --python 3"
3. Install all the dependencies by running this command:
"pipenv install"
4. Now the program is ready to be run. Do this:
"python3 application.py --file-name [json file location containing customer info]"
Example:
"python3 application.py --file-name customers.json
5. The results will be displayed in a tabular form.


## Running the tests

This script uses pytest for testing. 

1. Run this command to automatically run all tests:
"pytest"

### List of tests to be run

1. test_distance_calculator
2. test_distance_calculator_raises_exception_on_non_float_or_integer_arguments
3. test_distance_calculator_raises_exception_on_zero_or_incomplete_arguments
4. test_file_reader_raises_exception__on_no_file_name_argument
5. test_file_reader_raises_exception_on_inability_to_open_file
6. test_app_logic_raises_exception_on_no_file_name_argument

## Built With

* [pipenv] - Official Python packaging tool
* [ujson] - Handling of JSON data
* [tabulate] - Display tabular data 
* [Click] - Creation of CLI programs from Python scripts.
* [python 3] - The Python Interpreter
* [pytest] - Write tests for python programs
## Authors

* **Ehigie Pascal Aito**  - [aitoehigie](https://twitter.com/pystar)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Kenneth Reitz (pipenv)
* Aaron Ronacher (click)
