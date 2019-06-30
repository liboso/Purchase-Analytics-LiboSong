# Purchase-Analytics

## Table of Contents
1. [How to run the program?](README.md#how-to-run-the-program)
1. [How is test data generated?](README.md#how-is-test-data-generated)
1. [How do I solve the problem?](README.md#how-do-i-solve-the-problem)

## How to Run the Program?
* This program is written of Python 3.7. Make ensure it's installed in your machine before you run it.
* In a terminal, assuming project home is the current directory, run `cd insight_testsuite && ./run_tests.sh`

## How is Test Data Generated?
There are 3 set of test data. `test_2` and `test_3` are based on the data set from the download link in the provided 
program.

* In test_1, the data set is from the original assignment.
* In test_2, `order_products.csv` is a set of sample data from `order_products__train.csv`. Please refer to 
`src/test_data_generator.py` for the sampling algorithm. `report.csv` is generated via applying `VLOOKUP`
and `COUNTIFS` functions to the sample data in Google Sheets then being exported to csv.
* In test_3, the input and output data are generated using the same method as of test_2 except that the source file is 
`order_products__prior.csv`.

## How do I Solve the Problem?
There are two steps to solve the problem.

Step 1 is to convert `products.csv` into a dictionary. The key of the dictionary is product ID, the value of the 
dictionary is department ID. This dictionary is used in Step 2 to lookup department ID by a product ID. It assumes the
number of product is finite (i.e. not ever-growing) and limited therefore it can be stored in memory.

Step 2 is to traverse the lines of `order_products.csv` to count the number of times a product was requested, number of 
times a product was requested for the first time. For each department, there are 2 counters: time_of_order and 
time_of_first_order. A dictionary is used to save department ID and its corresponding counters。 For each traverse, 
it consults the dictionary generated in Step 1 for department ID and update its counters based on the order information.
 It can handle `order_products.csv` in big size as the counting only requires one single line of data be read into 
 memory at a time. (In my development, I used `order_products__prior.csv` (500+ MB) for testing, it works well)

The solution [time complexity](https://en.wikipedia.org/wiki/Time_complexity) is O(n) due to the fact that the total 
number of traversal is the number of line of products.csv` + the number of line of `order_products.csv`
