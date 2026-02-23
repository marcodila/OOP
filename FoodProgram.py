import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

DISCOUNT_RATE = 0.2

def main():
    order_total = 0

customers = {
    569: ["Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", "ahimsworthfs@list-manage.com", "254-555-2273", True],
    570: ["Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", False]
}

def main():
    # Pull customer id
    input_id = int(input("Enter customer ID: "))

    # Customer instance
    customer_data = customers[input_id]
    customer = fc.Customer(input_id, *customer_data)

    # Transaction objects
    for data in dict.values():
        trans = fc.Transaction(*data)
        if trans.get_customer_id() == customer.get_customer_id():
            customer.charge_customer(trans)

    customer.report()

main()