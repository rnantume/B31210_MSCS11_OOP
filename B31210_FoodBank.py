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
        self.food_received = {}  # Dictionary to store food items and quantities

    def get_details(self):
        _details = super().get_details()
        _details += f", Family size: {self.family_size}, Origin Country: {self.origin_country}"
        return _details

    def receive_food(self, food_item, quantity):
        """Records the food item received by the refugee."""
        if food_item.name in self.food_received:
            self.food_received[food_item.name] += quantity
        else:
            self.food_received[food_item.name] = quantity

    def get_food_received(self):
        """Returns a string representation of received food items and quantities."""
        return ', '.join([f"{item}: {quantity}" for item, quantity in self.food_received.items()])

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
    
    #def add_to_defined_units(self):
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
    
    def quantity_needed_for_distribution(self, num_refugees):
        """Calculates the total quantity needed of a particulat food based on the number of refugees."""
        return self.unit.get_unit_cap() * num_refugees

    def get_food_name(self):
        """Returns the name of the food item."""
        return self.name
    
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
    def __init__(self, release_date, inventory, food_list=None):
        self.id = str(uuid.uuid1())
        self.release_date = release_date
        self.inventory = inventory  # Inventory instance refereced
        self.food_list = food_list if food_list is not None else []

        # Initialize the refugees_list with existing refugees from the inventory
        self.refugees_list = list(self.inventory.refugees_list)

    def add_refugee(self, refugee):
        """Adds refugee directly to inventory and distribution lists, if not already present."""
        if not isinstance(refugee, Refugee):
            raise TypeError("variable 'refugee' must be of type 'Refugee'")
        
        # Check if the refugee is already in the distribution's refugee list
        if any(existing_refugee.id == refugee.id for existing_refugee in self.refugees_list):
            print(f"Refugee {refugee.get_name()} is already in the distribution list.")
        else:
            self.refugees_list.append(refugee)  # Add new refugee
            self.inventory.add_refugee(refugee)  # Optionally add to inventory too
            print(f"Refugee {refugee.get_name()} has been added to the distribution list.")
        
        self.inventory.add_refugee(refugee)

    def add_food(self, food_item):
        """Adds food to the distribution list."""
        self.food_list.append(food_item)

    def distribute(self):
        """Distributes food and updates inventory."""
        # Ensure enough stock is available in the inventory
        for food_item in self.food_list:
            num_refugees = self.inventory.get_total_refugees() #gets total refugees factoring in family size
            available_quantity = self.inventory.get_stock_count(food_item)
            if available_quantity < food_item.quantity_needed_for_distribution(num_refugees):
                raise ValueError(f"Not enough {food_item.name} in stock.")
            
            # Distribute food to each refugee
            for refugee in self.refugees_list:
                refugee_qty = refugee.family_size * food_item.unit.get_unit_cap()
                refugee.receive_food(food_item, refugee_qty) 

            # Release food from inventory
            self.inventory.release_food(food_item, food_item.quantity_needed_for_distribution(num_refugees))
            
        # Record the distribution
        self.inventory.record_distribution(self)

class Inventory:
    def __init__(self):
        self.supplies_list = []
        self.distribution_list = []
        self.donation_list = []
        self.donors_list = []
        self.refugees_list = []

    def get_supplies(self):
        """returns the list of all supplies"""
        return self.supplies_list
    
    def get_stock(self):
        """Displays all food items in stock."""
        return {supply.food_item.name: supply.quantity_available for supply in self.supplies_list}
  
    def get_stock_count(self, food_item=None):
        """
        Returns the total quantity available for a specific food item if passed,
        or returns a dictionary with total available quantity for all food items.
        """
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

    def notify_stock_levels(self):
        """
        Checks stock levels of all items.
        Notifies if any item has less than 50 units available.
        """
        low_stock_items = []
        stock_counts = self.get_stock_count()  # returns a dictionary of all items and their totals

        for food_name, quantity_available in stock_counts.items():
            if quantity_available < 50:
                low_stock_items.append(f"{food_name}: {quantity_available} units available")

        if low_stock_items:
            print("Low stock alert! The following items have less than 50 units available:")
            for item in low_stock_items:
                print(item)
        else:
            print("All items are have enough stock.")

    def notify_expired_supplies(self):
        today = datetime.datetime.now()
        expired_supplies = [supply for supply in self.supplies_list if supply.expiration_date < today]
        if expired_supplies:
            print("Expired Food Supplies:")
            for supply in expired_supplies:
                print(f"{supply.food_item.get_food_name()} (Expires on: {supply.expiration_date.strftime('%Y-%m-%d')})")
        else:
            print("No expired food supplies.")

    def get_all_refugees(self):
        return self.refugees_list

    def get_total_refugees(self):
        """
        get total refugees, loopoing through refugee objects for their family_sizes
        """
        total_refugees = 0
        for refugee in self.refugees_list:
                total_refugees += refugee.family_size  # Adding family size of each refugee
        return total_refugees

    def release_food(self, food_item, quantity_needed):
        """Reduces the quantity of a specific food item in stock."""
        quantity_remaining = quantity_needed  # Keep track of how much we still need to deduct

        for supply in self.supplies_list:
            if supply.food_item.name == food_item.name:
                available_quantity = supply.get_quantity_available()
                
                if available_quantity > 0:
                    if available_quantity >= quantity_remaining:
                        supply.update_quantity(quantity_remaining)  # Deduct the needed amount from this supply
                        quantity_remaining = 0  # All needed quantity has been deducted
                        break  # Exit loop since we've satisfied the requirement
                    else:
                        supply.update_quantity(available_quantity)  # Deduct all available quantity
                        quantity_remaining -= available_quantity  # Reduce the remaining quantity needed

        if quantity_remaining > 0:
            raise ValueError(f"Not enough {food_item.name} in stock to fulfill the request. Remaining: {quantity_remaining}")

    def show_food_distribution(self):
        """Displays the food distribution for each refugee."""
        print("Food Distribution to Refugees:")
        for refugee in self.refugees_list:
            food_details = refugee.get_food_received()
            print(f"Refugee: {refugee.get_name()}, Food Received: {food_details}")

    def record_distribution(self, distribution):
        """Records the distribution event."""
        self.distribution_list.append(distribution)

    def get_distributions(self):
        return self.distribution_list

    def add_donor(self, _donor):
        """
        Adds a new donor to donors_list if not already added.
        """
        if not isinstance(_donor, Donor):
            raise TypeError("variable '_donor' must be of type 'Donor'")
        
        if _donor not in self.donors_list:
            self.donors_list.append(_donor)
            print(f"Donor {_donor.get_name()} has been added.")
        else:
            print(f"Donor {_donor.get_name()} is already in the list.")

    def add_refugee(self, refugee):
        """Adds a refugee to the inventory's refugee list, ensuring no duplication."""
        if not isinstance(refugee, Refugee):
            raise TypeError("variable 'refugee' must be of type 'Refugee'")
        
        # Ensures the refugee is not already in the list by checking their unique id
        if all(existing_refugee.id != refugee.id for existing_refugee in self.refugees_list):
            self.refugees_list.append(refugee)
            print(f"Refugee {refugee.get_name()} has been added to the refugees list.")
        else:
            print(f"Refugee {refugee.get_name()} is already in the refugees list.")

    def get_all_donations(self):
        """Returns a list of all donations with their details."""
        all_donations = []
        for donation in self.donation_list:
            donation_details = donation.get_donation()  # Assuming get_donation() retrieves relevant details
            all_donations.append(donation_details)
        return all_donations

    def get_donations_by_donor(self, donor):
        """Returns a list of donations made by a specific donor."""
        if not isinstance(donor, Donor):
            raise TypeError("The parameter 'donor' must be of type 'Donor'")
        
        donor_donations = []
        for donation in self.donation_list:
            if donation.donor.id == donor.id:  # Check if the donation is made by the specified donor
                donation_details = donation.get_donation()
                donor_donations.append(donation_details)
        return donor_donations
    
    def record_donation(self, donation):
        """Records a new donation and adds it to the donation list
          as well its supplies appended the supplies_list."""
        if not isinstance(donation, Donation):
            raise TypeError("The parameter 'donation' must be of type 'Donation'")
        
        # Check for duplicate donation by ID
        if any(existing_donation.id == donation.id for existing_donation in self.donation_list):
            print(f"Donation with ID {donation.id} already exists and will not be added.")
            return  # Exit the method without adding

        self.donation_list.append(donation)
        print(f"Donation by {donation.donor.get_name()} has been recorded.")

        # Append each supply to the supplies_list
        for supply in donation.supply_list:
            self.supplies_list.append(supply)
        
        print(f"Supplies from donation added to inventory.")






