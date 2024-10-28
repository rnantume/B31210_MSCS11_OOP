import unittest
import datetime
import uuid
from B31210_FoodBank import Person, Refugee, Donor, Unit, Food, Supply, Donation, Distribution, Inventory

class FoodManager:
    """"""
    # Create an inventory system
    inventory = Inventory()

    # Creating units and respective quantity per family head
    unit_rice = Unit("Rice", 6)
    unit_beans = Unit("Beans", 2)
    unit_oil = Unit("Oil", 1) 
    unit_matooke = Unit("Matooke", 1)
    
    # Create food items with their respective units
    food_rice = Food("Rice", unit_rice)
    food_beans = Food("Beans", unit_beans)
    food_oil = Food("Oil", unit_oil)
    food_matooke = Food("Matooke", unit_matooke)

    # Create donors
    donor1 = Donor("Kijjo Joe", "23232323", "kampala", _is_organisation=False)
    donor2 = Donor("Samuel Co. Ltd", "11414169", "wakiso", _is_organisation=True)
    donor3 = Donor("Kato Vincent", "07014596300", "Nairobi Kenya", _is_organisation=False)

    # Create refugees
    refugee1 = Refugee("Soma Family", "444444444", "Nakivale Camp", 5, "Congo")
    refugee2 = Refugee("Tamu Family", "333333333", "Nakivale Camp", 3, "Congo")
    refugee3 = Refugee("Goma family", "222222222", "Nakivale Camp", 5, "Burundi")
    refugee4 = Refugee("Kenge family", "111111111", "Nakivale Camp", 3, "Somalia")
    refugee5 = Refugee("Deug Sutan", "0789562010", "Nakivale Camp", 3, "South Sudan")

    # Create supplies objects
    supply_rice1 = Supply(food_rice, 100, datetime.datetime(2025, 1, 1))  
    supply_beans1 = Supply(food_beans, 50, datetime.datetime(2025, 6, 1))  
    supply_oil1 = Supply(food_oil, 20, datetime.datetime(2025, 6, 1))

    supply_rice2 = Supply(food_rice, 50, datetime.datetime(2025, 2, 1))  
    supply_beans2 = Supply(food_beans, 50, datetime.datetime(2025, 7, 1))  
    supply_matooke2= Supply(food_matooke, 10, datetime.datetime(2024, 12, 5))

    # Create donations objects
    donation1 = Donation(donor1, datetime.datetime.now())
    donation2 = Donation(donor2, datetime.datetime.now())

    # Add supplies to inventory
    inventory.supplies_list.append(supply_rice1)
    inventory.supplies_list.append(supply_beans1)
    inventory.supplies_list.append(supply_oil1)
    inventory.supplies_list.append(supply_beans2)
    inventory.supplies_list.append(supply_rice2)
    inventory.supplies_list.append(supply_matooke2)

    # Add the donation to the inventory
    inventory.donation_list.append(donation1)
    inventory.donation_list.append(donation2)

    # Create a distribution event
    distribution1 = Distribution(datetime.datetime.now(), inventory, [food_rice, food_beans, food_oil])
    distribution2 = Distribution(datetime.datetime.now(), inventory, [food_rice, food_beans, food_oil])
    distribution3 = Distribution(datetime.datetime.now(), inventory, [food_rice, food_beans, food_oil])
    distribution4 = Distribution(datetime.datetime.now(), inventory, [food_rice, food_beans, food_oil])

     # Add the donation to the inventory
    inventory.donation_list.append(donation1)
    inventory.donation_list.append(donation2)

    # Create a distribution event
    distribution1 = Distribution(datetime.datetime.now(), inventory, [food_rice, food_beans, food_oil])
    distribution2 = Distribution(datetime.datetime.now(), inventory, [food_rice, food_beans, food_oil])
    distribution3 = Distribution(datetime.datetime.now(), inventory, [food_rice, food_beans, food_oil])
    distribution4 = Distribution(datetime.datetime.now(), inventory, [food_rice, food_beans, food_oil])

    # Create a list of all distribution events
    distributions = [distribution1, distribution2, distribution3, distribution4]

    # Loop through each distribution event and distribute food
    for distribution in distributions:
        try:
            distribution.distribute()
            print(f"Distribution {distribution.id} for refugees completed successfully.")
        except ValueError as e:
            print(f"Distribution failed for {distribution.id}: {e}")

    # Record each distribution event in the inventory
    for distribution in distributions:
        inventory.record_distribution(distribution)

    # Check the remaining stock after all distributions
    print("Stock after distributions:", inventory.get_stock_count())

    # Print the donation details
    donation_details = donation1.get_donation()
    print(f"Donation details: {donation_details}")

    # Print the distribution history
    for dist in inventory.distribution_list:
        print(f"Distribution ID: {dist.id}, Date: {dist.release_date}")
        for refugee in dist.refugees_list:
            food_info = refugee.get_food_received()
            print(f"  Refugee: {refugee.name}, Food Received: {food_info}")

    #getting available stock for rice
    print(f"Quantity of {food_oil.name} left is: {inventory.get_stock_count(food_oil)}")

    # Retrieve all donations
    all_donations = inventory.get_all_donations()
    for donation in all_donations:
        print(donation)

    donor_donations = inventory.get_donations_by_donor(donor1)
    for donation in donor_donations:
        print(donation)

    def show_menu(self, _menuItem = "" ):
        if _menuItem == "":
            print("System Menu ---------------------------------------------------")
            print("     1: Show Available Unit Types")
            print("     2: Show Available Food Types")
            print("     3: Add Donors")
            print("     4: Add Refugees")
            print("     5: Add Supplies to donations")
            print("     6: Record Donations")
            #print("     5: Donations")
            #print("     6: Distributions")
            #print("     7: Inventory")
            #print("     0: Back")
    # check inventory for stock counts,  distributions list, donations list
    # create supply items
    # add supplies and donors to donation/s: expiration dates of supplies are checked
    # record donations, new donor is added to donors list, and donation objects added in the inventory
    # add food items and refugees to a distributions
    # distribute food according to refugee family size; new refugee can be added to the distribution list
    # check stock levels again for reduction of food items
    # notification for low stock levels is issued
    #lists for donations and distributions printed
    def show_units(self):
        print("Units set ---------------------------------------------------")
        print(self.unit_beans)
        print(self.unit_rice)
        print(self.unit_oil)
        print(self.unit_matooke)
        print("")

    def show_fooditems(self):
        print("Foods set ---------------------------------------------------")
        print(self.food_rice)
        print(self.food_beans)
        print(self.food_oil)
        print(self.food_matooke)

    def add_donors(self):
        print("Donor set ---------------------------------------------------")
        self.inventory.add_donor(self.donor1)
        self.inventory.add_donor(self.donor2)
        self.inventory.add_donor(self.donor2)
        self.inventory.add_donor(self.donor1)

    def add_refugees(self):
        print("Refugee set ---------------------------------------------------")
        self.inventory.add_refugee(self.refugee1)
        self.inventory.add_refugee(self.refugee2)
        self.inventory.add_refugee(self.refugee3)
        self.inventory.add_refugee(self.refugee2)
        print(f"------------------------")
        print(f"Total Refugee families: {len(self.inventory.refugees_list)} with {self.inventory.get_total_refugees()} members")
        
    def add_supplies_to_donations(self):
        print("Donations and their supplies--------------------------------------")
        self.donation1.add_supply(self.supply_rice1)
        self.donation1.add_supply(self.supply_beans1)
        self.donation1.add_supply(self.supply_oil1)
        print(f"{self.donation1.get_donation()}")
        self.donation2.add_supply(self.supply_rice2)
        self.donation2.add_supply(self.supply_beans2)
        self.donation2.add_supply(self.supply_matooke2)
        print(f"{self.donation2.get_donation()}")
        
    def record_donations(self):
        print("Donations Recorded-------------------------------------------")
        self.inventory.record_donation(self.donation1)
        self.inventory.record_donation(self.donation2)
        self.inventory.record_donation(self.donation2)
        print(f"View All Supplies: {self.inventory.supplies_list}")

try:
   user_food_manager = FoodManager()
   user_food_manager.show_menu("")
   while True:
       user_menu = input()
       if user_menu.strip() == "1":
           user_food_manager.show_units()
       elif user_menu.strip() == "2":
           user_food_manager.show_fooditems() 
       elif user_menu.strip() == "3":
           user_food_manager.add_donors()
       elif user_menu.strip() == "4":
           user_food_manager.add_refugees()
       elif user_menu.strip() == "5":
           user_food_manager.add_supplies_to_donations()
       elif user_menu.strip() == "6":
           user_food_manager.record_donations()
       elif user_menu.strip() == "7":
           user_food_manager.show_menu("")
       elif user_menu.strip() == "0":
           user_food_manager.show_menu("")
       else:
           print("No Menu Item Selected")
           break
       
except:
    print("Exception happened, please try again --------------------------------")
finally:
    print("End: Food manager closed ---------------------------------------------")