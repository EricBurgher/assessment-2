import csv
import os
from data.classes import Customers
from data.classes import Inventory

class App:
    def __init__(self, name):
        self.name = name
        self.users = Customers.customer_objects()
        self.inventory = Inventory.current_inventory()

    # def list_users(self):
    #     print('\n')
    #     for i, user in enumerate(self.users):
    #         print(f'{i + 1}. {user.name} {user.email_address}')

    def view_inventory(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path, 'r') as data_file:
            reader = csv.DictReader(data_file)
            for row in data_file:
                print(data_file)

    def customer_data(self, drivers_num):
        for user in self.users:
            if Customers.dl_number == drivers_num:
                return user
        return "User Not Found"

    def rent_video(self):
        for title in self.title:
            if drivers_id == user.dl.number:
                video_rental = input("What video would you like to rent?: ")
                # Don't append. Take out a specific title. Look that up.
                self.title[f'{title}'].append(video_rental)
        self.save_title()

    def return_video(self):
        pass

    def add_user(self, user_data):
        self.users.append(Customers(user_data['dl_number'],user_data['first_name'], user_data['last_name'], user_data['current_video_rentals']))
        self.posts[user_data['dl_number']] = [user_data['dl_number']]
        self.save()

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.users[user_data['dl_number']])

    # def add_post(self, drivers_id):
    #     for post in self.posts:
    #         if drivers_id == post:
    #             user_post = input("Enter text for you post: ")
    #             self.posts[f'{post}'].append(user_post)
    #     self.save_posts()

    # def save(self):
    #     my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = os.path.join(my_path, "../data/users.csv")

    #     with open(path, 'w') as csvfile:
    #         user_csv = csv.writer(csvfile, delimiter=',')
    #         user_csv.writerow(['name', 'email_address', 'dl_number', 'account_type'])
    #         for user in self.users:
    #             user_csv.writerow([user.name, user.email_address, user.dl_number, user.account_type])

    def save_posts(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/posts.csv")

        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.posts:
                self.posts[row].insert(0,row)
                writer.writerow(post for post in self.posts[row]) 