import unittest
import datetime
import uuid
from B31210_FoodBank import Person, Refugee, Donor, Unit, Food, Supply, Donation, Distribution, Inventory

class FoodManager:
    """"""

    # Creating units
    unit_kgs = Unit("Kilograms")
    unit_litres = Unit("Litres")
    unit_banches = Unit("Banches")
    
    # Create food items with their respective units
    food_rice = Food("Rice", unit_kgs, 2)
    food_beans = Food("Beans", unit_kgs, 2)
    food_oil = Food("Oil", unit_litres, 1)
    food_matooke = Food("Matooke", unit_banches, 1)

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

    def show_menu(self, _menuItem = "" ):
        if _menuItem == "":
            print("System Menu ---------------------------------------------------")
            print("     1: Show Available Unit Types")
            print("     2: Show Available Food Types")
            print("     3: Show Available Donors")
            print("     4: Show Available Refugees")
            print("     5: Donations")
            print("     6: Distributions")
            print("     7: Inventory")
            print("     0: Back")

    def show_units(self):
        print("Units set ---------------------------------------------------")
        print(self.unit_kgs.get_details())
        print(self.unit_litres.get_details())
        print(self.unit_banches.get_details())
        print("")

    def show_fooditems(self):
        print("Foods set ---------------------------------------------------")
        print(self.food_rice.get_details())
        print(self.food_beans.get_details())
        print(self.food_oil.get_details())
        print(self.food_matooke.get_details())

    def show_donors(self):
        print("Donor set ---------------------------------------------------")
        print(self.donor1.get_details())
        print(self.donor2.get_details())
        print(self.donor3.get_details())

    def show_refugees(self):
        print("Refugee set ---------------------------------------------------")
        print(self.refugee1.get_details())
        print(self.refugee2.get_details())
        print(self.refugee3.get_details())
        print(self.refugee4.get_details())
        print(self.refugee5.get_details())

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
           user_food_manager.show_donors()
       elif user_menu.strip() == "4":
           user_food_manager.show_refugees()
       elif user_menu.strip() == "5":
           user_food_manager.show_menu("")

       elif user_menu.strip() == "6":
           user_food_manager.show_menu("")
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