# Write your solution here!
import csv
import os
from data.classes import App
from data.classes import Customers
from data.classes import Inventory

mode = ''

while mode != '6':
    mode = input("\nWelcome to Code Platoon Video!\n---------------\nOptions:\n1. View video inventory \n2. View customer's rented videos \n3. Rent video \n4. Return video \n5. Add new customer\n6. Exit\n---------------\n\nWhat would you like to do?: ")

    if mode == '1':
        Inventory.get_current_inventory()
    elif mode == '2':
        drivers_id = input("Enter driver's license number: ")
        my_path = os.path.abspath(os.path.dirname(__file__))
        customers_path = os.path.join(my_path, "../assessment-2/data/customers.csv")
        with open(customers_path, 'r') as data_file:
                reader = csv.DictReader(data_file)
                for row in reader:
                    if row["id"] == (str(drivers_id)):
                        print(f'Current Video Rentals: {row["current_video_rentals"]}')

    elif mode == '3':
        drivers_id = input("Enter driver's license number: ")
        my_path = os.path.abspath(os.path.dirname(__file__))
        customers_path = os.path.join(my_path, "../assessment-2/data/customers.csv")
        with open(customers_path, 'r') as data_file:
                reader = csv.DictReader(data_file)
                for row in reader:
                    if row["id"] == (str(drivers_id)):
                        print(f'Current Video Rentals: {row["current_video_rentals"]}')
                        string_splitter = str(row["current_video_rentals"]).split('/')
                        if len(string_splitter) >= 3:
                                print("I'm sorry, you already have 3 rentals out. Our policy is 3 rentals per customer at a time.")
                        else:
                            print("What is the name of the video you want to rent?")
        my_path = os.path.abspath(os.path.dirname(__file__))
        inventory_path = os.path.join(my_path, "../assessment-2/data/inventory.csv")
        with open(inventory_path, 'r') as data_file:
                reader = csv.DictReader(data_file)
                for row in reader:
                    copies_counter = str(row["copies_available"])
                    if (copies_counter) > "0":
                        print('Yes, we have video that in stock!')
                    else:
                        print('We do not have that video in stock right now.')
                    # if str(row["title"]) == input
                        
        # my_path = os.path.abspath(os.path.dirname(__file__))
        # inventory_path = os.path.join(my_path, "../assessment-2/data/inventory.csv")
        # with open(inventory_path, 'w') as data_file:
        #         writer = csv.DictWriter(data_file)

                    #decremement the copies_available
                    #add the title to customer csv

    elif mode == "4":
        drivers_id = input("Enter driver's license number: ")
        App.return_video(drivers_id)
    elif mode == "5":
        user_data = {}
        user_data['id'] = input("Enter your driver's license number: ")
        user_data['first_name'] = input("Enter your first name: ")
        user_data['last_name'] = input("Enter your last name: ")
        user_data['current_video_rentals'] = ''
        my_path = os.path.abspath(os.path.dirname(__file__))
        customers_path = os.path.join(my_path, "../assessment-2/data/customers.csv")
        with open(customers_path, 'a') as csvfile:
            fieldnames = ['id', 'first_name', 'last_name', 'current_video_rentals']
            writer = csv.writer(csvfile)
            writer.writerow((user_data['id'],user_data['first_name'], user_data['last_name'], user_data['current_video_rentals']))
            newline=''


    elif mode == '6':
        break
    else:
        pass