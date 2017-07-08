"""
Given an array of Customer objects with an array of Purchase objects,
return the name of customers that purchased the most last week
"""

import uuid
from datetime import datetime
from datetime import timedelta

def parse_date(date):
    return datetime.strptime(date, '%Y-%m-%d')

class Customer(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = uuid.uuid4()

    def show(self):
        return "{} {}".format(self.first_name, self.last_name)

class CustomerList(object):
    def __init__(self, *args):
        self.items = [ arg for arg in args ]

    def get_all(self):
        return [ item for item in self.items ]


class Purchase(object):
    def __init__(self, customer_id, date, cost, description):
        self.customer_id = customer_id
        self.date = parse_date(date)
        self.cost = cost
        self.description = description
        self.id = uuid.uuid4()


class PurchaseList(object):
    def __init__(self, *args):
        self.items = [ arg for arg in args ]

    def get_all(self):
        return [ item for item in self.items ]

    def filter_by_date(self, target_date):
        return [ item for item in self.items if item.date > parse_date(target_date) ]

    def last_week_only(self):
        last_week = datetime.today() - timedelta(7)
        return [ item for item in self.items if item.date > last_week ]


def create_purchase_list():
    a = Customer('John', 'Doe')
    b = Customer('Jane', 'Snow')
    customers = CustomerList(a, b)
    assert([customer.first_name for customer in customers.get_all()]) == ['John', 'Jane']

    apple = Purchase(a.id, '2017-06-01', 2, 'apple')
    assert(apple.cost) == 2

    banana = Purchase(a.id, '2017-07-02', 5, 'banana')
    orange = Purchase(b.id, '2017-07-03', 10, 'orange')

    purchases = PurchaseList(apple, banana, orange)

    print([purchase.date for purchase in purchases.get_all()])

    assert([purchase.description for purchase in purchases.filter_by_date('2017-01-01')]) == ['apple', 'banana', 'orange']
    assert([purchase.description for purchase in purchases.last_week_only()]) == ['banana', 'orange']

    return customers, purchases


def main():
    customers, purchases = create_purchase_list()
    active_customers = []
    for purchase in purchases.last_week_only():
        for customer in customers.get_all():
            if customer.id == purchase.customer_id:
                name = customer.show()
                active_customers.append({ name: purchase.cost })

    print(active_customers)


main()
