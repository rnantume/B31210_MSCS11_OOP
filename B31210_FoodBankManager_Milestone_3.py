import uuid
import datetime

class Person:
    id = ""
    name = ""
    contact = ""
    address = ""

    def __init__(self, _name, _contact, _address) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.contact = _contact
        self.address = _address

    def print_history():
        print("-------------------------------------")


class Donor(Person):
    isOrganisation = False
    def __init__(self, _name, _contact, _address, _isOrganisation) -> None:
        super().__init__(_name, _contact, _address)
        self.isOrganisation = _isOrganisation

    def get_details():
        print("---------------------------------------")
    
    def print_history():
        print("---------------------------------------")

class Refugee(Person):
    family_size = 1
    origin_country = ""
    def __init__(self, _name, _contact, _address, _family_size, _origin_country) -> None:
        super().__init__(_name, _contact, _address)
        self.family_size = _family_size
        self.origin_country = _origin_country

    def print_history():
        print("---------------------------------------")

class Unit:
    id = ""
    name = ""
    quantity_per_family_member = 0
    def __init__(self, _name, _quantity_per_family_member) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.quantity_per_family_member = _quantity_per_family_member

class Food:
    id = ""
    name = ""
    def __init__(self, _name, _unit) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.unit = _unit
        if not isinstance(_unit, Unit):
            raise TypeError("variable '_unit' must be of type 'Unit")
        
class Supply:
    id = ""
    quantity = 0
    quantity_available = 0
    def __init__(self, _food_item, _quantity) -> None:
        self.id = str(uuid.uuid1())
        self.food_item = _food_item
        self.quantity = _quantity
        if not isinstance(_food_item, Food):
            raise TypeError("variable '_food_item' must be of type 'Food")

class Donation:
    id = ""
    delivered_date = datetime.datetime.now
    supply_list = []
    def __init__(self, _delivered_date, _supply_list) -> None:
        self.id = str(uuid.uuid1())
        self.delivered_date = _delivered_date
        self.supply_list = _supply_list
        if not isinstance(_supply_list, datetime.datetime):
            raise TypeError("variable '_supply_list' must be of type 'datetime.datetime")

class StockCount:
    id = ""
    quantity = 0
    def __init__(self, _food_item) -> None:
        self.id = str(uuid.uuid1())
        self.food_item = _food_item
        if not isinstance(_food_item, Food):
            raise TypeError("variable '_food_item' must be of type 'Food")
        
class Distribution:
    id = ""
    release_date = datetime.datetime.now
    food_list = []
    refugee_list = []
    def __init__(self, _release_date, _food_list, _refugee_list) -> None:
        self.id = str(uuid.uuid1())
        self.release_date = _release_date
        self.food_list = _food_list
        self.refugee_list = _refugee_list
        if not isinstance(_release_date, datetime.datetime):
            raise TypeError("variable '_release_date' must be of type 'datetime.datetime")
        
class Inventory:
    id = ""
    stock_count_list = []
    store_list = []
    donation_list = []
    distribution_list = []
    release_date = datetime.datetime.now
    def __init__(self, _stock_count_list, _store_list, _donation_list, _distribution_list) -> None:
        self.id = str(uuid.uuid1())
        self.stock_count_list = _stock_count_list
        self.store_list = _store_list
        self.donation_list = _donation_list
        self.distribution_list = _distribution_list