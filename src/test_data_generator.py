"""
A helper module that generates test data out of order_products__prior/train.csv.
For each 1000 lines in the given input file, it takes one line as a sample.
The samples are written into "order_products_sample.csv"
"""

if __name__ == '__main__':
    input = '../input/order_products__prior.csv'
    sample = '../input/order_products_sample.csv'

    with open(input, "r") as input_file:
        with open(sample, "w") as output_file:
            output_file.writelines(input_file.readline())
            output_file.writelines(input_file.readlines()[2::1000])


