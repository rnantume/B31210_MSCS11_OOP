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
        return f"ID: {self.id}, Name: {self.name}, Contact No: {self.contact}, Address: {self.address}"
    
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
        _details = super().get_details()
        _details += f", Is Organisation: {str(self.is_organisation)}"
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
        _details = super().get_details()
        _details += f", Family size: {self.family_size}, Origin Country: {self.origin_country}"
        return _details

class Unit:
    """
    Represents the quantity per foot type allocated per family member.
    Attributes:
    id (str): Unique identifier for the unit.
    name(str): Name of the food.
    quantity_per_family_member(int): Quantity of food allocated per family member.
    Methods:
    get_unit_cap(): returns the quantity allocated per family member.
    """
    def __init__(self, _name, _quantity_per_family_member) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.quantity_per_family_member = _quantity_per_family_member
    
    #def add_to_defined_units()(self):
    #    return self.name
    
    def get_unit_cap(self):
        return self.quantity_per_family_member

class Food:
    """
    Represents a food item in the foodbank with attributes below:
    - id: Unique identifier od food item
    - name: Name of the food item (e.g., Rice, Beans)
    - unit: Unit of release for this food item, which must be an instance of Unit class)
    """
    def __init__(self, _name, _unit) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.unit = _unit   #_unit is an instance of Unit class
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

    def get_details(self):
        """Returns food details."""
        unit_qty = self.unit.get_unit_cap()
        return f"Food ID: {self.id}, Food Name: {self.name}, Unit of Release: {unit_qty}"
         
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
        if self.quantity_available > 0:
            if (self.quantity_available - _quantity_used) >= 0:
                self.quantity_available -= _quantity_used
        return self.quantity_available

    def get_quantity_available(self):
        return self.quantity_available

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
            "supplies": [supply.food_item.get_details() for supply in self.supply_list]
        }

class Distribution:
    def __init__(self, release_date, refugees_list=None, food_list=None):
        self.id = str(uuid.uuid1())
        self.release_date = release_date
        self.refugees_list = refugees_list if refugees_list is not None else []
        self.food_list = food_list if food_list is not None else []

    def add_refugee(self, refugee):
        """Adds refugee to the list of those receiving food."""
        if refugee not in self.refugees_list:
            self.refugees_list.append(refugee)

    def add_food(self, food_item):
        """Adds food to the distribution list."""
        self.food_list.append(food_item)

    def distribute(self, inventory):
        """Distributes food and updates inventory."""
        # Ensure enough stock is available in the inventory
        for food_item in self.food_list:
            available_quantity = inventory.get_stock_count(food_item)
            if available_quantity < food_item.quantity_needed():
                raise ValueError(f"Not enough {food_item.name} in stock.")
            # Release food from inventory
            inventory.release_food(food_item, food_item.quantity_needed())
        # Record the distribution
        inventory.record_distribution(self)

class Inventory:
    def __init__(self):
        self.supplies_list = []
        self.distribution_list = []
        self.donation_list = []
        self.donors_list = []
        self.refugees_list = []

    def get_stock(self):
        """Displays all food items in stock."""
        return {supply.food_item.name: supply.quantity_available for supply in self.supplies_list}
  
    def get_stock_count(self, food_item):
        #Returns the available quantity of a specific food item.
        for supply in self.supplies_list:
            if supply.food_item.name == food_item.name:
                return supply.get_quantity_available()
        return 0

    def get_stock_count(self):
        """
        Returns a dictionary with total available quantity for each food type.
        """
        food_totals = {}  # Dictionary to hold the total quantities for each food type

         # Iterate through each supply in the supplies list
        for supply in self.supplies_list:
            food_name = supply.food_item.name  # Get the name of the food item
            quantity_available = supply.get_quantity_available()  # Get the available quantity of the supply
        
            # Add the quantity to the corresponding food type in the dictionary
            if food_name in food_totals:
                food_totals[food_name] += quantity_available  # If food already exists, add to the total
            else:
                food_totals[food_name] = quantity_available  # If food doesn't exist, set initial value
    
        return food_totals  # Return the dictionary with food totals

    def release_food(self, food_item, quantity_needed):
        """Reduces the quantity of a specific food item in stock."""
        for supply in self.supplies_list:
            if supply.food_item.name == food_item.name:
                supply.update_quantity(quantity_needed)

    def record_distribution(self, distribution):
        """Records the distribution event."""
        self.distribution_list.append(distribution)