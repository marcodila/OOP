class Customer:
    def __init__(self, customer_id, name, address, email, phone, member_status):
        self._customer_id = customer_id
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone
        self._member_status = member_status

    #Accessor Methods

    def get_customer_id(self):
        return self._customer_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def get_member_status(self):
        return self._member_status


class Transaction:
    def __init__(self, date, item_name, cost, customer_id):
        self._date = date
        self._item_name = item_name
        self._cost = cost
        self._customer_id = customer_id

    def get_date(self):
        return self._date

    def get_item_name(self):
        return self._item_name

    def get_cost(self):
        return self._cost

    def get_customer_id(self):
        return self._customer_id
