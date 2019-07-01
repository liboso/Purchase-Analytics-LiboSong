import sys
import csv


def parse_department_id_int(val):
    """
    parses the string department_id to an integer;
    If the entered value is invalid then return -1; so all records under department_id = -1 might need to be cleaned up.
    :return: department_id as an integer;
    """
    try:
        return int(val)
    except ValueError:
        return -1


def product_dept_map(products):
    """
    Read products.csv into a dictionary (key = product_id, value = department_id)
    :return: a dictionary
    """
    result = {}

    # To run this program in Windows, encoding='utf-8' is required to avoid 'UnicodeDecodeError'
    with open(products, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # covert each row into a dictionary entry (key = product_id, value = department_id)
        # department_id will be converted to int for easy to sort which is required for report generation.
        for row in reader:
            result.update({row['product_id'].strip(): parse_department_id_int(row['department_id'])})
    return result


def main(args):
    """
    Expected args are csv paths in the order of: order, products and report
    :param args:
    :return:
    """
    # A simple error handling solution to ensure expected arguments are provided.
    assert len(args) >= 4, "Mismatched arguments. Please ensure orders, products and report path are provided."

    orders = args[1]
    products = args[2]
    report = args[3]

    # print(f'orders: {orders}, products: {products}, report: {report}')
    print("orders: {0}, products: {1}, report: {2}".format(orders, products, report))

    prod_dept_map = product_dept_map(products)
    result = {}

    print("Start to traverse order.")

    # To run this program in Windows, encoding='utf-8' is required to avoid 'UnicodeDecodeError'
    with open(orders, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_id = row['product_id'].strip()

            # If a department_id cannot be found the set department = -1;
            # so all records "department_id = -1" might need to be cleaned up.
            department_id = prod_dept_map.get(product_id, -1)

            # First time order is 1 only if `reordered` is 0.
            first_time_order = int(row['reordered'].strip() == "0")

            # default value is a tuple with value of (number of order, number of order of first time)
            result.setdefault(department_id, (0, 0))
            counters = result[department_id]
            result.update({department_id: (counters[0] + 1, counters[1] + first_time_order)})

    print("Traversing order finished.")

    with open(report, 'w') as report_csv:
        fieldnames = ['department_id', 'number_of_orders', 'number_of_first_orders', "percentage"]
        writer = csv.DictWriter(report_csv, delimiter=',', lineterminator='\n', fieldnames=fieldnames)

        writer.writeheader()
        for department_id in sorted(result):
            writer.writerow({
                "department_id": department_id,
                "number_of_orders": result[department_id][0],
                "number_of_first_orders": result[department_id][1],
                # to ensure 2 fixed decimal places as required by the test data.
                "percentage": "{0:.2f}".format(round(result[department_id][1] / result[department_id][0], 2))
            })

    print("Report generated.")


def entry_point():
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()
