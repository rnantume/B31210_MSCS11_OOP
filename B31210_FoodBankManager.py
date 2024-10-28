import datetime
from B31210_FoodBank import Person, Refugee, Donor, Unit, Food, Supply, Donation, Distribution, Inventory

class FoodManager:
    def __init__(self):
        # Initialize the inventory system
        self.inventory = Inventory()

        # Creating units and respective quantity per family head
        self.unit_rice = Unit("Rice", 6)
        self.unit_beans = Unit("Beans", 2)
        self.unit_oil = Unit("Oil", 1) 
        self.unit_matooke = Unit("Matooke", 1)

        # Create food items with their respective units
        self.food_rice = Food("Rice", self.unit_rice)
        self.food_beans = Food("Beans", self.unit_beans)
        self.food_oil = Food("Oil", self.unit_oil)
        self.food_matooke = Food("Matooke", self.unit_matooke)

        # Create donors
        self.donor1 = Donor("Kijjo Joe", "23232323", "Kampala", _is_organisation=False)
        self.donor2 = Donor("Samuel Co. Ltd", "11414169", "Wakiso", _is_organisation=True)

        # Create refugees
        self.refugees = [
            Refugee("Soma Family", "444444444", "Nakivale Camp", 5, "Congo"),
            Refugee("Tamu Family", "333333333", "Nakivale Camp", 3, "Congo"),
            Refugee("Goma Family", "222222222", "Nakivale Camp", 5, "Burundi"),
            Refugee("Kenge Family", "111111111", "Nakivale Camp", 3, "Somalia"),
            Refugee("Deug Sutan", "0789562010", "Nakivale Camp", 3, "South Sudan")
        ]

        # Create supplies objects
        self.supplies = [
            Supply(self.food_rice, 100, datetime.datetime(2025, 1, 1)),
            Supply(self.food_beans, 50, datetime.datetime(2025, 6, 1)),
            Supply(self.food_oil, 20, datetime.datetime(2025, 6, 1)),
            Supply(self.food_rice, 50, datetime.datetime(2025, 2, 1)),
            Supply(self.food_beans, 50, datetime.datetime(2025, 7, 1)),
            Supply(self.food_matooke, 10, datetime.datetime(2024, 10, 5))
        ]

        # Create donations objects
        self.donation1 = Donation(self.donor1, datetime.datetime.now())
        self.donation2 = Donation(self.donor2, datetime.datetime.now())
        
    def show_menu(self):
        print("System Menu ---------------------------------------------------")
        print("     1: Show Available Unit Types")
        print("     2: Show Available Food Types")
        print("     3: Add Donors")
        print("     4: Add Refugees")
        print("     5: Add Supplies to Donations")
        print("     6: Record Donations")
        print("     7: View Supplies List")
        print("     8: Check Stock Levels")
        print("     9: Low-Stock Alerts")
        print("     10: Notify Expired Food Supplies") 
        print("     11: View All Refugees")
        print("     12: Add Refugees to inventory")
        print("     13: Distribute Food")
        print("     14: View all food distributions")
        print("     15: View all Donations")
        print("     0: Exit")

    def show_units(self):
        print("Units set ---------------------------------------------------")
        print(self.unit_rice)
        print(self.unit_beans)
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

    def add_refugees(self):
        print("Refugee set ---------------------------------------------------")
        for refugee in self.refugees:
            self.inventory.add_refugee(refugee)
        #print(f"Total Refugee families: {len(self.inventory.refugees_list)} with {self.inventory.get_total_refugees()} members")

    def add_supplies_to_donations(self):
        print("Adding supplies to donations-----------------------------------")
        self.donation1.add_supply(self.supplies[0])
        self.donation1.add_supply(self.supplies[1])
        self.donation1.add_supply(self.supplies[2])
        print(f"{self.donation1.get_donation()}")
        self.donation2.add_supply(self.supplies[3])
        self.donation2.add_supply(self.supplies[4])
        self.donation2.add_supply(self.supplies[5])
        print(f"{self.donation2.get_donation()}")

    def record_donations(self):
        print("Donations Recorded-------------------------------------------")
        self.inventory.record_donation(self.donation1)
        self.inventory.record_donation(self.donation2)

    def view_supplies(self):
        print("Available Supplies List:")
        for supply in self.inventory.get_supplies():
            food_name = supply.food_item.get_food_name()
            quantity = supply.quantity
            expiry = supply.expiration_date.strftime('%Y-%m-%d')
            print(f"{food_name}: {quantity} (Expires on: {expiry})")

    def check_stock_levels(self):
        print("Current Stock Levels:")
        print(f"{self.inventory.get_stock_count()}")

    def low_stock_alerts(self):
        print(f"{self.inventory.notify_stock_levels()}")

    def notify_expired_supplies(self):
        print(f"{self.inventory.notify_expired_supplies()}")

    def get_all_refugees(self):
        print(f"{self.inventory.get_all_refugees()}")

    def distribute_food(self):
        food_items = []
        print("Enter food items to distribute (comma-separated): ")
        user_input = input().split(',')
        for item in user_input:
            food_item = item.strip()
            if food_item == "Rice":
                food_items.append(self.food_rice)
            elif food_item == "Beans":
                food_items.append(self.food_beans)
            elif food_item == "Oil":
                food_items.append(self.food_oil)
            elif food_item == "Matooke":
                food_items.append(self.food_matooke)

        distribution = Distribution(datetime.datetime.now(), self.inventory, food_items)
        try:
            distribution.distribute()
            self.inventory.record_distribution(distribution)
            print(f"Distribution {distribution.id} completed successfully.")
        except ValueError as e:
            print(f"Distribution failed: {e}")

    def get_distributions(self):
        print(f"{self.inventory.get_distributions()}")

    def add_refugee_to_distribution(self):
        refugee_id = input("Enter Refugee ID to add to distribution: ")
        refugee = self.inventory.get_refugee_by_id(refugee_id)
        if refugee:
            distribution_id = input("Enter Distribution ID to add this refugee: ")
            distribution = self.inventory.get_distribution_by_id(distribution_id)
            if distribution:
                distribution.add_refugee(refugee)
                print(f"Added {refugee.name} to distribution {distribution.id}.")
            else:
                print("Distribution not found.")
        else:
            print("Refugee not found in inventory.")

    def view_donations_by_donor(self):
        donor_item = input("Enter Donor object to view donations: ")
        donations = self.inventory.get_donations_by_donor(donor_item)
        if donations:
            for donation in donations:
                print(donation)
        else:
            print("No donations found for this donor.")

    def get_all_donations(self):
        print(f"{self.inventory.get_all_donations()}")

# Running the application
if __name__ == "__main__":
    user_food_manager = FoodManager()
    user_food_manager.show_menu()
    while True:
        user_menu = input("Select an option: ")
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
            user_food_manager.view_supplies()
        elif user_menu.strip() == "8":
            user_food_manager.check_stock_levels()
        elif user_menu.strip() == "9":
            user_food_manager.low_stock_alerts()
        elif user_menu.strip() == "10":
            user_food_manager.notify_expired_supplies()
        elif user_menu.strip() == "11":
            user_food_manager.get_all_refugees()
        elif user_menu.strip() == "12":
            user_food_manager.add_refugees()
        elif user_menu.strip() == "13":
            user_food_manager.distribute_food()
        elif user_menu.strip() == "14":
            user_food_manager.get_distributions()
        elif user_menu.strip() == "#15":
            user_food_manager.add_refugee_to_distribution()
        elif user_menu.strip() == "15":
            user_food_manager.get_all_donations()
        elif user_menu.strip() == "0":
            print("Exiting the Food Manager application.")
            break
        else:
            print("Invalid option. Please try again.")
