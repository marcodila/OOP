class Customer:
    def __init__(self, customer_id: int, name: str, address: str, email: str, phone: str, member_status: bool):
        self.__customer_id = customer_id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = member_status

        self.__items_ordered = []
        self.__subtotal = 0.0
        self.__discount_amount = 0.0

    # Accessors
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_member_status(self):
        return self.__member_status

    # Mutating
    def charge_customer(self, transaction):
        price = float(transaction.get_cost())
        self.__items_ordered.append(transaction)
        self.__subtotal += price

        # 20% discount if member
        if self.__member_status:
            self.__discount_amount += price * 0.20

    def report(self):
        print(f"Customer Name: {self.__name}")
        print(f"Phone: {self.__phone}")

        for trans in self.__items_ordered:
            print(f"Order Item: {trans.get_item_name()} Price: ${trans.get_cost():,.2f}")

        print(f"Total Cost: ${self.__subtotal:,.2f}")

        if self.__member_status:
            print(f"Member Discount: ${self.__discount_amount:,.2f}")
            total_after = self.__subtotal - self.__discount_amount
            print(f"Total Cost after discount: ${total_after:,.2f}")


class Transaction:
    def __init__(self, date: str, item_name: str, cost: float, customer_id: int):
        self.__date = date
        self.__item_name = item_name
        self.__cost = float(cost)
        self.__customer_id = int(customer_id)

    # Accessors
    def get_date(self):
        return self.__date

    def get_item_name(self):
        return self.__item_name

    def get_cost(self):
        return self.__cost

    def get_customer_id(self):
        return self.__customer_id