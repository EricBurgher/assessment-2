# Write your solution here!
import csv
from data.classes import App
from data.classes import Customers
from data.classes import Inventory

mode = ''

while mode != '6':
    mode = input("\nWelcome to Code Platoon Video!\nOptions:\n1. View video inventory \n2. View customer's rented videos \n3. Rent video \n4. Return video \n5. Add new customer\n6. Exit\n\nWhat would you like to do?: ")
    # I don't understand why this isn't working. Moving on...
    if mode == '1':
        Inventory.current_inventory()
    elif mode == '2':
        drivers_id = input("Enter driver's license number: ")
        App.customer_data()
    elif mode == '3':
        drivers_id = input("Enter driver's license number: ")
        App.rent_video(drivers_id)
    elif mode == "4":
        drivers_id = input("Enter driver's license number: ")
        App.return_video(drivers_id)
    elif mode == "5":
        user_data = {}
        user_data['dl_number'] = input("Enter your driver's license number: ")
        user_data['first_name'] = input("Enter your first name: ")
        user_data['last_name'] = input("Enter your last name: ")
        user_data['current_video_rentals'] = input("What video would you like to rent today? ")
        App.add_user(user_data)

    elif mode == '6':
        break
    else:
        pass