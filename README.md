# Purchase-Analytics

## Table of Contents
1. [How to run the test?](README.md#how-to-run-the-test)
1. [How is test data generated?](README.md#how-is-test-data-generated)
1. [How do I solve the problem?](README.md#how-do-i-solve-the-problem)

## How to Run the Test?
* This program is written in Python. Please make ensure it's installed in your machine before running it.
* In a terminal, assuming project home is the current directory, run `cd insight_testsuite && ./run_tests.sh`

## How is Test Data Generated?
There are 3 set of test data. `test_2` and `test_3` are based on the data set from the download link provided by the 
assignment.

* In test_1, the data set is from the original assignment.
* In test_2, `order_products.csv` is a set of sample data from `order_products__train.csv`. Please refer to 
`src/test_data_generator.py` for the sampling algorithm. `report.csv` is generated via applying `VLOOKUP`
and `COUNTIFS` functions to the sample data in Google Sheets then being exported to a csv file.
* In test_3, the input and output data are generated using the same method as of test_2 except that the source file is 
`order_products__prior.csv`.

## How do I Solve the Problem?
There are two steps to solve the problem.

Step 1 is to convert `products.csv` into a dictionary. The key of the dictionary is product ID, the value of the 
dictionary is department ID. This dictionary is used in Step 2 to lookup department ID by a product ID. 

Step 2 is to traverse the lines of `order_products.csv` to count the number of times a product was requested and the 
number of times a product was first requested for each department. There are 2 counters: time_of_order and 
time_of_first_order. A dictionary is used to save department ID and its corresponding counters。 For each traverse, 
it asks the dictionary generated in Step 1 for department ID and update its counters based on the order information.
A department will be added into the dictionary only if number_of_orders is greater than 0, as required by the assignment.
It can handle `order_products.csv` in big size as the counting only requires one single line of data be read into 
 memory at a time. (In my development, I used `order_products__prior.csv` (500+ MB) for testing, it works well.)

The solution [time complexity](https://en.wikipedia.org/wiki/Time_complexity) is O(n) due to the fact that the total 
number of traversal is the number of line of `products.csv` + the number of line of `order_products.csv`
