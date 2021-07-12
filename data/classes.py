import csv
import os


class Customers:
    def __init__(self, id, first_name, last_name, current_video_rentals):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals

    @classmethod
    def objects(cls):
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        customers_path = os.path.join(my_path, "../customers.csv")
        with open(customers_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(Customers(**dict(row)))
        return customers

    def get_customer_rentals(drivers_id, id):
        rentals_list = {}
        my_path = os.path.abspath(os.path.dirname(__file__))
        customers_path = os.path.join(my_path, "../customers.csv")
        with open(customers_path, 'r') as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                target = Customers(**dict(row))
                if target.drivers_id == id:
                    rentals_list.append(id)
        for rentals in rentals_list:
                print(f'Customer ID: {row["id"],{row["first_name"]}} Video Title: {row["current_video_rentals"]}')

    def add_user(self, user_data):
        #this naming convention follows exactly the OOP review by Kate and I DONT UNDERSTAND why I'm getting an error here. Google says it should work too.
        new_user = Customers(**user_data)
        self.customers.append(new_user)
        self.save_new_user()

    def save_new_user(self, user_data):
        my_path = os.path.abspath(os.path.dirname(__file__))
        customers_path = os.path.join(my_path, "../customers.csv")
        with open(customers_path, 'w') as csvfile:
            fields = ['id','first_name','last_name','current_video_rentals']
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            for user in self.customers:
                csvwriter.writerow(user_data.id, user_data.first_name, user_data.last_name, user_data.current_video_rentals)

class Inventory:
    def __init__(self, id, title, rating, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available

# This is option 1 in the interface.
    def get_current_inventory():
        inventory_list = {}
        my_path = os.path.abspath(os.path.dirname(__file__))
        inventory_path = os.path.join(my_path, "../data/inventory.csv")
        with open(inventory_path, 'r') as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                print(f'Video ID: {row["id"]} Video Title: {row["title"]} Rating: {row["rating"]} Copies Available: {row["copies_available"]}')
        return inventory_list

class App:
    def __init__(self, users):
        self.users = Customers()
        self.inventory = Inventory.get_current_inventory()


    def rent_video(self, drivers_id):
        for i, user in enumerate(self.user):
                if drivers_id == Customers.id:
                    self.users.append(i - 1)
                    print(f"Thank you for renting {Inventory.title}. It's due back in 5 days.")   
        self.save_title()

    def return_video(self):
        video = input("\nEnter the movie you'd like to return: ")
        id = input("\nEnter Divers License Number: ")
        if id == Customers(id):
                self.users.append(id + 1)
                print(f"Thank you for returning {Inventory.title}.")
                # write logic to increment the inventory count
                self.title[f'{Inventory.title}'].append(video)
         # write logic to remove title from current_video_rentals for that customer
         # write logic to add title back to inventory CSV
                my_path = os.path.abspath(os.path.dirname(__file__))
                inventory_path = os.path.join(my_path, "../inventory.csv")
                with open(inventory_path, 'w') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(self.users[id['copies_available']])
         # once successful, populate string "Thank you for returning {title}. Come again soon."
                self.save_title()
    
    def save_title(self):
        