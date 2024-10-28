import unittest
import datetime
import uuid
from B31210_FoodBank import Person, Refugee, Donor, Unit, Food, Supply, Donation, Distribution, Inventory

class FoodManager:
    """"""
    dict_unit_list = {}
    dict_food_list = {}
    dict_donor_list = {}
    dict_refugee_list = {}
    dict_supply_list = {}
    dict_donation_list = {}
    dict_distribution_list = {}
    store_inventory = Inventory()

    # Creating units
    dict_unit_list["Kilograms"] = Unit("Kilograms")
    dict_unit_list["Litres"] = Unit("Litres")
    dict_unit_list["Banches"] = Unit("Banches")
    
    # Create food items with their respective units
    food_rice = Food("Rice", dict_unit_list["Kilograms"], 2)
    food_beans = Food("Beans", dict_unit_list["Kilograms"], 2)
    food_oil = Food("Oil", dict_unit_list["Litres"], 1)
    food_matooke = Food("Matooke", dict_unit_list["Banches"], 1)
    dict_food_list[food_rice.id] = food_rice
    dict_food_list[food_beans.id] = food_beans
    dict_food_list[food_oil.id] = food_oil
    dict_food_list[food_matooke.id] = food_matooke

    # Create donors
    donor1 = Donor("Kijjo Joe", "23232323", "kampala", _is_organisation=False)
    donor2 = Donor("Samuel Co. Ltd", "11414169", "wakiso", _is_organisation=True)
    donor3 = Donor("Kato Vincent", "07014596300", "Nairobi Kenya", _is_organisation=False)
    dict_donor_list[donor1.id] = donor1
    dict_donor_list[donor2.id] = donor2
    dict_donor_list[donor3.id] = donor3

    # Create refugees
    refugee1 = Refugee("Soma Family", "444444444", "Nakivale Camp", 5, "Congo")
    refugee2 = Refugee("Tamu Family", "333333333", "Nakivale Camp", 3, "Congo")
    refugee3 = Refugee("Goma family", "222222222", "Nakivale Camp", 5, "Burundi")
    refugee4 = Refugee("Kenge family", "111111111", "Nakivale Camp", 3, "Somalia")
    refugee5 = Refugee("Deug Sutan", "0789562010", "Nakivale Camp", 3, "South Sudan")
    dict_refugee_list[refugee1.id] = refugee1
    dict_refugee_list[refugee2.id] = refugee2
    dict_refugee_list[refugee3.id] = refugee3
    dict_refugee_list[refugee4.id] = refugee4
    dict_refugee_list[refugee5.id] = refugee5

    def show_menu(self, _menuItem = "" ):
        if _menuItem == "":
            print("System Menu ---------------------------------------------------")
            print("  1: Show Available Unit Types")
            print("  2: Show Available Food Types")
            print("  3: Show Available Donors")
            print("  4: Show Available Refugees")
            print("  5: Donations")
            print("  6: Distributions")
            print("  7: Inventory")
            print("  0: Back")
        elif _menuItem == "1":
            self.show_units()
        elif _menuItem == "2":
            self.show_fooditems()
        elif _menuItem == "3":
            self.show_donors()
        elif _menuItem == "4":
            self.show_refugees()
        elif _menuItem == "5":
            print("5: Donations Menu ---------------------------------------------------")
            print("  51: Available Donations")
            print("  52: Create Donation")
            print("  53: Add Donor")
            print("  54: Add Supply")
            print("  55: Show Donation Details")
        elif _menuItem == "6":
            print("6: Distributions Menu ---------------------------------------------------")
            print("  61: Available Distributions")
            print("  62: Create Distributions")
            print("  63: Add Refugee")
            print("  64: Add Food Item")
        elif _menuItem == "7":
            print("7: Inventory Menu ---------------------------------------------------")
            print("  71: Available Stock")
            print("  72: Add Donation")
            print("  73: Release Distribution")
            print("  74: View History")

    def show_units(self):
        print("Units available ---------------------------------------------------")
        for _unit in self.dict_unit_list:
            print(self.dict_unit_list[_unit].get_details())
        print("")

    def show_fooditems(self):
        print("Foods available ---------------------------------------------------")
        for _food in self.dict_food_list:
            print(self.dict_food_list[_food].get_details())

    def show_donors(self):
        print("Donor available ---------------------------------------------------")
        for _donor in self.dict_donor_list:
            print(self.dict_donor_list[_donor].get_details())

    def show_refugees(self):
        print("Refugee available ---------------------------------------------------")
        for _refugee in self.dict_refugee_list:
            print(self.dict_refugee_list[_refugee].get_details())

    def manage_donations(self, _menuItem):
        try:
            if _menuItem == "51": # Available Donations
                print("Donations available ---------------------------------------------------")
                for _donation in self.dict_donation_list:
                    print(self.dict_donation_list[_donation].get_donation())

            elif _menuItem == "52": # Create Donation
                self.show_menu("3") # Show Available Donors
                print("Input the donor id from the above list for this donation !")
                user_input = input()
                if len(user_input.strip()) != 36:
                    print("Donor id be 36 character long, donation not created !")
                    return
                else:
                    try:
                        new_donation =Donation(self.dict_donor_list[user_input.strip()], datetime.datetime.now())
                        self.dict_donation_list[new_donation.id] = new_donation
                        print(f"Donation with ID '{new_donation.id}' created successfully !")
                    except KeyError:
                        print("Donor with id '' not found. Donations not created, please try again !")

            elif _menuItem == "53": # Add Donor
                self.show_menu("3") # Show Available Donors
                self.show_menu("51") # Available Donations
                print("Input format [donation id, donor id] to add / update donor on a donation !")
                user_input = input()
                user_input_list = user_input.strip().split(",")
                try:
                    new_supply =Supply(self.dict_food_list[user_input_list[1]], int(user_input_list[2]), expire_date)
                    donation: Donation = self.dict_donation_list[user_input_list[0]]
                    donation.add_donor(self.dict_donor_list[user_input_list[1]])
                    print("Donor add / updated successfully !")
                except KeyError:
                    print(f"Donation id '{user_input_list[0]}' or donor id '{user_input_list[1]}' not found. Add / Update no done, please try again !")

            elif _menuItem == "54": # Add Supply
                if len(self.dict_donation_list) > 0:
                    self.show_menu("2") # Show Available Food Types
                    self.show_menu("51") #  Available Donations
                    print("Input Supply details in this format  [donation id, food id, quantity, number of days to expire] !")
                    user_input = input()
                    user_input_list = user_input.strip().split(",")
                    
                    if len(user_input_list) != 4:
                        print("Input supply details are not correct to create a supply !")
                    else:
                        if not user_input_list[2].isdigit():
                            print("Input supply quantity is not a digit !")
                        elif not user_input_list[3].isdigit():
                            print("Input supply 'number of days' is not a digit !")
                        try:
                            expire_date = datetime.datetime.now()
                            expire_date = expire_date + datetime.timedelta(days= int(user_input_list[3]))
                            new_supply =Supply(self.dict_food_list[user_input_list[1]], int(user_input_list[2]), expire_date)
                            donation: Donation = self.dict_donation_list[user_input_list[0]]
                            donation.add_supply(new_supply)
                            print("Donations created successfully !")
                        except KeyError:
                            print(f"Donation id '{user_input_list[0]}' or food id '{user_input_list[1]}' not found. Supply not added, please try again !")
                
                else:
                    print("First create a donation to add supplies !")

            elif _menuItem == "55": # Show Donation Details
                self.show_menu("51") # Available Donations
                print("Input [donation id] !")
                user_input = input()
                try:
                    donation: Donation = self.dict_donation_list[user_input.split()]
                    print(donation.get_donation())
                except KeyError:
                    print(f"Donation id '{user_input.split()}' not found. Please try again !")
        except Exception as error:
            print("An exception happened with donations, please try again ", error)
        finally:
            self.show_menu("5") # Donations Menu
    
    def manage_distributions(self, _menuItem):
        try:
            if _menuItem == "61": # Available Distributions
                print("Distributions available ---------------------------------------------------")
                for _distribution in self.dict_distribution_list:
                    print(self.dict_distribution_list[_distribution].get_distribution())
            elif _menuItem == "62": # Create Distributions
                    new_distribution = Distribution(datetime.datetime.now())
                    self.dict_distribution_list[new_distribution.id] = new_distribution
                    print(f"Distribution with ID '{new_distribution.id}' created successfully !")
            elif _menuItem == "63": # Add Refugee
                if len(self.dict_distribution_list) > 0:
                    self.show_menu("4") # Show Available Refugees
                    self.show_menu("61") # Available Distributions
                    print("Input format [distribution id, refugee id] to add / update refugee on a distribution !")
                    user_input = input()
                    user_input_list = user_input.strip().split(",")
                    try:
                        distribution: Distribution = self.dict_distribution_list[user_input_list[0]]
                        distribution.add_refugee(self.dict_refugee_list[user_input_list[1]])
                        print("Refugees add / updated successfully to distribution !")
                    except KeyError:
                        print(f"Distribution id '{user_input_list[0]}' or refugee id '{user_input_list[1]}' not found. Add / Update no done, please try again !")
                else:
                    print("First create a distribution to add refugees !")

            elif _menuItem == "64": # Add Food Item
                if len(self.dict_distribution_list) > 0:
                    self.show_menu("2") # Show Available Food Types
                    self.show_menu("61") # Available Distributions
                    print("Input format [distribution id, food id] to add / update food on a distribution !")
                    user_input = input()
                    user_input_list = user_input.strip().split(",")
                    try:
                        distribution: Distribution = self.dict_distribution_list[user_input_list[0]]
                        distribution.add_food(self.dict_food_list[user_input_list[1]])
                        print("Food add / updated successfully to distribution !")
                    except KeyError:
                        print(f"Distribution id '{user_input_list[0]}' or food id '{user_input_list[1]}' not found. Add / Update no done, please try again !")
                else:
                    print("First create a distribution to add food items !")

        except:
            print("An exception happened with distributions, please try again -------------")
        finally:
            self.show_menu("6")

    def manage_inventory(self, _menuItem):
        try:
            if _menuItem == "71": # Available Stock 
                print("Available stock in inventory ---------------------------------------------------")
                registered_food_id_list = list(self.dict_food_list)
                for _food_id in registered_food_id_list:
                    try:
                        print(f"Food {self.dict_food_list[_food_id].name}: {self.store_inventory.dict_stock_count_list[_food_id]}")
                    except KeyError:
                        print(f"Food {self.dict_food_list[_food_id].name}: 0")  

            elif _menuItem == "72": # Add Donation
                self.show_menu("51") # Available Donations
                print("Input donation id from the above list to add to inventory !")
                user_input = input()
                try:
                    if user_input.strip() in self.dict_donation_list:
                        _donation: Donation = self.dict_donation_list[user_input.strip()]
                        if len(_donation.supply_list) > 0:
                            for _supply in _donation.supply_list:
                                if _supply in self.dict_supplies_list:
                                    self.store_inventory.dict_donation_list 
                            print(f"Donation with ID '{_donation.id}' added to inventory successfully !")
                        else:
                            print("Supply list is zero. Donations not added to inventory, please try again !")
                    else:
                        print(f"Donation id '{user_input.strip()}' not found. Donations not added to inventory, please try again !")
                except KeyError:
                    print("Item id not found. Donations not added to inventory, please try again !")

        except Exception as error:
            print("An exception happened with inventory, please try again", error)
        finally:
            self.show_menu("7")

try:
   user_food_manager = FoodManager()
   user_food_manager.show_menu("")
   while True:
       user_input = input()
       if user_input.strip() == "1" or user_input.strip() == "2" or user_input.strip() == "3" \
            or user_input.strip() == "4" or user_input.strip() == "5" or user_input.strip() == "6" \
            or user_input.strip() == "7":
           user_food_manager.show_menu(user_input.strip())
       elif user_input.strip()[:1] == "5":
           user_food_manager.manage_donations(user_input.strip())
       elif user_input.strip()[:1] == "6":
           user_food_manager.manage_distributions(user_input.strip())
       elif user_input.strip()[:1] == "7":
           user_food_manager.manage_inventory(user_input.strip())
       elif user_input.strip() == "0":
           user_food_manager.show_menu("")
       else:
           print("No Menu Item Selected")
           break
       
except:
    print("Exception happened, please try again --------------------------------")
finally:
    print("End: Food manager closed ---------------------------------------------")