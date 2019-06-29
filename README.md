# Purchase-Analytics

## Table of Contents
1. [How to run the program?](README.md#how-to-run-the-program)
1. [How is test data generated?](README.md#how-is-test-data-generated)

## How to Run the Program?
* This program is written of Python 3.7. Make ensure it's installed in your machine before you run it.
* In a terminal, assuming project home is the current directory, run `cd insight_testsuite && ./run_tests.sh`


## How is Test Data Generated?
There are 3 set of test data. `test_2` and `test_3` are based on the data set of the download link the program provides.

* test_1 is the data set from the original program.
* in test_2, `order_products.csv` is a rename of `order_products__train.csv`. `products.csv` is from the same tar file.
* in test_3, `order_products.csv` is a sample of `order_products__prior.csv`. Please refer to
`src/test_data_generator.py` for the sampling algorithm.
