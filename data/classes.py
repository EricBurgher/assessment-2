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
    # Do harder Googling on why this won't work.
    def current_inventory(cls):
        inventory_list = {}
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                inventory_list[row[0]] = row[1:]

        return inventory_list

class App:
    def __init__(self, name, users):
        self.name = name
        self.users = Customers.customer_objects()
        self.inventory = Inventory.current_inventory()

    # def list_users(self):
    #     print('\n')
    #     for i, user in enumerate(self.users):
    #         print(f'{i + 1}. {user.name} {user.email_address}')

    def current_inventory(self):
    # Do harder Googling on why this won't work.
        current_inventory = {}
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path, 'r') as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                print(row)

    def customer_data(drivers_num):
    # Write logic on current list of video rentals by title only.
        for user in self.users:
            if drivers_num == Customers.dl_number:
                return user
        return "User Not Found"

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/inventory.csv")
    with open(path, 'r') as data_file:
        reader = csv.DictReader(data_file)
        for row in reader:
            print(row)
        

    def rent_video(self, drivers_id):
        for id in self.id:
            if drivers_id == Customers.dl.number:
                video_rental = input("What video would you like to rent?: ")
    # Not append. Decremement copies_available in CSV file. Look it up.
                self.title[f'{title}'].append(video_rental)
    # Add logic to remove 1 from copies_available in inventory.csv
    # Add logic so that you can't rent less than 0 copies.
    # If copies are at 0, display "Ope! There are no copies available right now."
    # Add logic so that customer can't rent more than 3 copies at a time.
    # If trying to rent 4 or more videos, display "I'm sorry, you already have 3 rentals out."
    
        self.save_title()

    def return_video(self):
        for id in self.id:
            if drivers_id == Customers.dl.number:
                video_return = input("What video are you returning today?: ")
                self.title[f'{title}'].append(video_return)
         # write logic to remove title from current_video_rentals for that customer
         # write logic to add title back to inventory CSV
         # once successful, populate string "Thank you for returning {title}. Come again soon."
        self.save_title()

    def add_user(self, user_data):
        self.users.append(Customers(user_data['dl_number'],user_data['first_name'], user_data['last_name'], user_data['current_video_rentals']))
        self.save()

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.users[user_data['dl_number']])