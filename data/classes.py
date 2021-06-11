import csv
import os

class Customers:
    def __init__(self, dl_number, first_name, last_name, currently_rented):
        self.dl_number = dl_number
        self.first_name = first_name
        self.last_name = last_name
        self.currently_rented = currently_rented

    @classmethod
    def customer_objects(cls):
        customer_list = {}
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                customer_list[row[0]] = row[1:]

        return customer_list

class Inventory:
    def __init__(self, id, title, rating, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available

    @classmethod
    def current_inventory(cls):
        inventory_list = {}
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                inventory_list[row[0]] = row[1:]

        return inventory_list