import uuid
import datetime

class Person:
    """
    Represents a person that could be either a donor or refugee with the attributes below:
    id(str): uniquely identified,
    name(str),
    contact(str),
    address(str)
    """
    def __init__(self, _name, _contact, _address) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.contact = _contact
        self.address = _address
    
    def get_details(self):
        """returns details abour a person"""
        #return f"ID: {self.id}, Name: {self.name}, Contact No: {self.contact}, Address: {self.address}"
        return f"Name: {self.name}, Contact No: {self.contact}, Address: {self.address}"
    
    def get_name(self):
        """Returns the name of the person"""
        return self.name
    
class Donor(Person):
    """
    Represents a donor, who inherits from Person
    Donor has additional attributes: is_organisation(boolean)
    """
    def __init__(self, _name, _contact, _address, _is_organisation) -> None:
        super().__init__(_name, _contact, _address)
        self.is_organisation = _is_organisation

    def get_details(self):
        _details = "Donor " + super().get_details()
        _details += f", Is Organisation: {str(self.is_organisation)}, ID: {self.id}"
        return _details

class Refugee(Person):
    """
    Represents a refugee, who inherits from Person
    Refugee has additional attributes: 
    family_size(int) &
    origin_country(str)
    """
    def __init__(self, _name, _contact, _address, _family_size, _origin_country) -> None:
        super().__init__(_name, _contact, _address)
        self.family_size = _family_size
        self.origin_country = _origin_country

    def get_details(self):
        _details = "Refugee " + super().get_details()
        _details += f", Family size: {self.family_size}, Origin Country: {self.origin_country}, ID: {self.id}"
        return _details

class Unit:
    """
    Represents the unit of measurement for food
    Attributes:
    id (str): Unique identifier for the unit.
    name(str): Name of the food.
    Methods:
    get_details(): returns unit details.
    """
    def __init__(self, _name) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
    
    def get_details(self):
        return f"Unit ID: {self.id},  Name: {self.name}"

class Food:
    """
    Represents a food item in the foodbank with attributes below:
    - id: Unique identifier od food item
    - name: Name of the food item (e.g., Rice, Beans)
    - unit: Unit of release for this food item, which must be an instance of Unit class)
    - quantity_per_family_member(int): Quantity of food allocated per family member.
    """
    def __init__(self, _name, _unit, _quantity_per_family_member) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.unit = _unit   #_unit is an instance of Unit class
        self.quantity_per_family_member = _quantity_per_family_member
        if not isinstance(_unit, Unit):
            raise TypeError("variable '_unit' must be of type 'Unit'")
    
    """This part demonstrate encapsulation"""    
    @property
    def unit(self):
        """Gets the value for unit."""
        return self._unit
    
    @unit.setter
    def unit(self, _unit):
        """SSets the value of unit, with validation."""
        if not isinstance(_unit, Unit):
            raise TypeError("Argument '_unit' must be of type 'Unit'")
        self._unit = _unit

    def get_unit_cap(self):
        return self.quantity_per_family_member

    def get_details(self):
        """Returns food details."""
        return f"Food ID: {self.id}, Name: {self.name}, Unit of release: {self.get_unit_cap()}"
    
    def quantity_needed_for_distribution(self, num_refugees):
        """Calculates the total quantity needed of a particulat food based on the number of refugees."""
        return self.unit.get_unit_cap() * num_refugees
         
class Supply:
    id = ""
    quantity = 0
    quantity_available = 0
    expiration_date = datetime.datetime.now

    def __init__(self, _food_item, _quantity, _expiration_date) -> None:
        if not isinstance(_food_item, Food):
            raise TypeError("variable '_food_item' must be of type 'Food'")
        if not isinstance(_quantity, int):
            raise TypeError("variable '_quantity' must be of type 'int'")
        if _quantity <= 0:
            raise ValueError("variable '_quantity' must be greater than zero")
        if not isinstance(_expiration_date, datetime.datetime):
            raise TypeError("variable '_expiration_date' must be of type 'datetime.datetime'")
        
        self.id = str(uuid.uuid1())
        self.food_item = _food_item
        self.quantity = _quantity
        self.quantity_available = _quantity  # Initialize available quantity to the total quantity
        self.expiration_date = _expiration_date

    def add_expire_date(self, _new_expire_date):
        self.expiration_date = _new_expire_date

    def is_expired(self):
        return self.expiration_date < datetime.datetime.now()  # Check if the expiration date has passed
    
    def update_quantity(self, _quantity_used):
        try:
            if self.quantity_available > 0:
                if (self.quantity_available - _quantity_used) >= 0:
                    self.quantity_available -= _quantity_used
            return self.quantity_available
        except:
            print("Update quantity failed ")

    def get_quantity_available(self):
        return self.quantity_available
    
    def get_details(self):
        return f"Supply ID: {self.id},  Quantity: {self.quantity}, Quantity available {self.quantity_available}, Expiry {self.expiration_date}. ({self.food_item.get_details()})"

class Donation:
    """
    Represents a donation made to the food bank.
    Attributes:
    id (str): Unique identifier od a donation.
    donor(Donor): The donor who made the donation.
    supply_list (list): List of supplies in the donation.
    donation_date(datetime): Date the donation was made.
    """
    def __init__(self, _donor, _donation_date, _supply_list=None):
        self.id = str(uuid.uuid1())
        self.donor = _donor
        self.donation_date = _donation_date
        self.supply_list = _supply_list if _supply_list is not None else []
        
    def add_donor(self, _donor):
        """adds new donor"""
        if not isinstance(_donor, Donor):
            raise TypeError("variable '_donor' must be of type 'Donor'")
        self.donor = _donor

    def add_supply(self, _supply):
        """adds a supply to a supply list of a donation"""
        if not isinstance(_supply, Supply):
            raise TypeError("variable '_supply' must be of type 'Supply'")
        self.supply_list.append(_supply)

    def get_donation(self):
        """
        Retrieves details of the donation, including donor, date, and supplies.
        """
        return {
            "id": self.id,
            "donor": self.donor.get_details(),
            "donation_date": self.donation_date,
            "supplies": [supply.get_details() for supply in self.supply_list] if self.supply_list is not None else []
        }

class Distribution:
    """
    Represents a distribution event for food supplies to refugees.

    Attributes:
        id (int): Unique identifier for the distribution event.
        refugee (Refugee): The refugee receiving the distribution.
        supply_list (list): A list of Supply objects representing the supplies distributed.
        distribution_date (datetime): The date the distribution was made.
 
    """
    def __init__(self, release_date, refugees_list=None, food_list=None):
        self.id = str(uuid.uuid1())
        self.release_date = release_date
        self.refugees_list = refugees_list if refugees_list is not None else {}
        self.food_list = food_list if food_list is not None else {}

    def add_refugee(self, refugee: Refugee):
        """Adds refugee to the list of those receiving food."""
        try: 
            if refugee not in self.refugees_list:
                self.refugees_list[refugee.id] = refugee
        except:
             print("Failed adding a refugee")

    def add_food(self, food_item: Food):
        """Adds food to the distribution list."""
        try:
            self.food_list[food_item.id] = food_item
        except:
            print("Failed adding a food item")

    def get_distribution(self):
        """
        Retrieves details of the distribution, including date, refugee list, and food list.
        """
        return {
            "id": self.id,
            "release_date": self.release_date,
            "foods": [self.food_list[food].get_details() for food in self.food_list],
            "refugees": [self.refugees_list[refugee].get_details() for refugee in self.refugees_list]
        }

    def distribute(self, inventory):
        """Distributes food and updates inventory."""
        try:
            # Ensure enough stock is available in the inventory
            for food_item in self.food_list:
                num_refugees = inventory.get_total_refugees()
                available_quantity = inventory.get_stock_count(food_item)
                if available_quantity < food_item.quantity_needed_for_distribution(num_refugees):
                    raise ValueError(f"Not enough {food_item.name} in stock.")
                # Release food from inventory
                inventory.release_food(food_item, food_item.quantity_needed_for_distribution(num_refugees))
            # Record the distribution
            inventory.record_distribution(self)
        except:
            print("Distribution failed ")

class Inventory:
    """
    Represents an inventory for managing supplies, donations, distributions, and records of donors and refugees.

    Attributes:
        supplies_list (list): A list of all supplies in the inventory.
        distribution_list (list): A list of all distributions made from the inventory.
        donation_list (list): A list of all donations received in the inventory.
        donors_list (list): A list of all registered donors.
        refugees_list (list): A list of all registered refugees.
    """
    def __init__(self):
        self.dict_supplies_list = {}
        self.dict_distribution_list = {}
        self.dict_donation_list = {}
        self.dict_donors_list = {}
        self.dict_refugees_list = {}
        self.dict_stock_count_list = {}

    def get_stock(self):
        """Displays all food items in stock."""
        return {supply.food_item.name: supply.quantity_available for supply in self.supplies_list}
  
    def get_stock_count(self, food_item=None):
        """
        Returns the total quantity available for a specific food item if passed,
        or returns a dictionary with total available quantity for all food items.
        """
        try:
            if food_item:
                for supply in self.supplies_list:
                    if supply.food_item.name == food_item.name:
                        return supply.get_quantity_available()
                return 0
            else:
                # Return dictionary for all food items
                food_totals = {}
                for supply in self.supplies_list:
                    food_name = supply.food_item.name
                    quantity_available = supply.get_quantity_available()
                    if food_name in food_totals:
                        food_totals[food_name] += quantity_available
                    else:
                        food_totals[food_name] = quantity_available
                return food_totals
        except:
            print("Count stock failed, please try again ")

    def get_total_refugees(self):
        """
        get total refugees, loopoing through refugee objects for their family_sizes
        """
        try:
            total_refugees = 0
            for refugee in self.refugees_list:
                    total_refugees += refugee.family_size  # Adding family size of each refugee
            return total_refugees
        except:
            print("Get total refugees failed, please try again ")
    
    def release_food(self, food_item, quantity_needed):
        """Reduces the quantity of a specific food item in stock."""
        try:
            for supply in self.supplies_list:
                if supply.food_item.name == food_item.name:
                    supply.update_quantity(quantity_needed)
        except:
            print("Release food failed, please try again ")

    def record_distribution(self, distribution):
        """Records the distribution event."""
        try:
            self.distribution_list.append(distribution)
        except:
            print("Record distribution has failed, please try again ")