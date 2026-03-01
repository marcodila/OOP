import FoodClass as fc

# This dictionary represents transactions
# The key is the transaction identifier
# Each value is a list: ['Date', 'Name of item', 'Cost', 'customerid']
dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

#Customer class
customer_one = fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710', 'ahimsworthfs@list-manage.com', '254-555-2273', True)
customer_two = fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712', 'dsellyarft@gmpg.org', '254-555-9362', False)

#Built a switch for the customer we want to run
active_customer = customer_one
#active_customer = customer_two
#Can comment out either line above for the switch

#Customer Header
print(f"Customer Name: {active_customer.get_name()}")
print(f"Phone: {active_customer.get_phone()}")

#Transaction object
order_total = 0
for entry in dict.values():
    transaction = fc.Transaction(entry[0], entry[1], entry[2], entry[3])
    
    if transaction.get_customerid() == active_customer.get_customer_id():
        print(f"Order Item: {transaction.get_item_name()}  Price: ${transaction.get_cost():.2f}")
        order_total += transaction.get_cost()

#Total + Discount if member
print(f"Total Cost: ${order_total:.2f}")

if active_customer.get_member_status() == True:
    discount = order_total * 0.20
    print(f"Member Discount: ${discount:.2f}")
    print(f"Total Cost after discount: ${order_total - discount:.2f}")