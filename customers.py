"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # Add an __init__() method that can be passed a first name, last name, email
    # address, and password, and initializes instance attributes with these values.

    # Add a __repr()__ method like you have for the Melon class so that when you
    # print a customer, you can see some useful information about them. This is very
    # handy for debugging.

    # Add a function to read the customers.txt and populate a dictionary with the
    # format:
    # {email: Customer(...),
    #  email: Customer(...)}

    def __init__(self, first_name, last_name, email, password):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<Customer: {}, {}, {}, {}>".format(self.first_name, self.last_name, self.email, self.password)

def read_customer_information(filepath):

    customer_information = {}

    with open(filepath) as file:
        for line in file:
            (first_name, last_name, email, password) = line.strip().split("|")

            customer_information[email] = Customer(first_name, last_name, email, password)

    return customer_information

def get_by_email(email):

    return customer_information.get(email)


customer_information = read_customer_information("customers.txt")




