import uuid
import datetime

class Person:
    """
    Represents a person that could be either a donor or refugee with the attributes below:
    id(int): uniquely identified,
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
    """"""
    id = ""
    name = ""
    quantity_per_family_member = 0
    def __init__(self, _name, _quantity_per_family_member) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.quantity_per_family_member = _quantity_per_family_member
    
    def get_name(self):
        return self.name
    
    def get_unit_cap(self):
        return self.quantity_per_family_member

class Food:
    """"""
    id = ""
    name = ""

    def __init__(self, _name, _unit) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.unit = _unit
        if not isinstance(_unit, Unit):
            raise TypeError("variable '_unit' must be of type 'Unit")
    
    def get_details(self):
        #return "Name: " + self.name + ", Contact: " + self.unit + ", Address: " + self.address
        pass
        
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
        if not isinstance(_food_item, Food):
            raise ValueError("variable '_quantity' must be greater than zero")
        if not isinstance(_expiration_date, datetime.datetime):
            raise TypeError("variable '_quantity' must be of type 'datetime.datetime'")
        
        self.id = str(uuid.uuid1())
        self.food_item = _food_item
        self.quantity = _quantity
        self.expiration_date = _expiration_date
    
    def add_expire_date(self, _new_expire_date):
        self.expiration_date = _new_expire_date

    def is_expired(self):
        return (self.expiration_date > datetime.datetime.now)   
    
    def update_quantity(self, _quantity_used):
        if self.quantity_available > 0 :
            if (self.quantity_available - _quantity_used) >= 0 :
                self.quantity_available -= _quantity_used
        return self.quantity_available

    def get_quantity_available(self):
        return self.quantity_available

class Donation:
    id = ""
    delivered_date = datetime.datetime.now
    supply_list = []
    def __init__(self, _donor, _supply_list) -> None:
        if not isinstance(_donor, Donor):
            raise TypeError("variable '_donor' must be of type 'Donor'")
        
        self.id = str(uuid.uuid1())
        self.donor = _donor
        self.supply_list = _supply_list

    def add_donor(self, _donor):
        if not isinstance(_donor, Donor):
            raise TypeError("variable '_donor' must be of type 'Donor'")
        self.donor = _donor

    def add_supply(self, _supply):
        if not isinstance(_supply, Supply):
            raise TypeError("variable '_supply' must be of type 'Supply'")
        self.supply_list.append(_supply)

    def get_donation(self):
        pass

        
class Distribution:
    """"""
    id = ""
    release_date = datetime.datetime.now
    food_list = []
    refugee_list = []
    def __init__(self, _release_date, _food_list, _refugee_list) -> None:
        if not isinstance(_release_date, datetime.datetime):
            raise TypeError("variable '_release_date' must be of type 'datetime.datetime'")
        self.id = str(uuid.uuid1())
        self.release_date = _release_date
        self.food_list = _food_list
        self.refugee_list = _refugee_list

    def add_refugee(self, _refugee):
         if not isinstance(_refugee, Refugee):
            raise TypeError("variable '_refugee' must be of type 'Refugee'")   
         self.refugee_list.append(_refugee)
    
    def add_food(self, _food):
        if not isinstance(_food, Food):
            raise TypeError("variable '_food' must be of type 'Food'")   
        self.food_list.append(_food)

    def get_details(self):
        pass


class StockCount:
    id = ""
    quantity = 0
    def __init__(self, _food_item) -> None:
        if not isinstance(_food_item, Food):
            raise TypeError("variable '_food_item' must be of type 'Food'")
        
        self.id = str(uuid.uuid1())
        self.food_item = _food_item
    
    def get_count(self, _food):
        if not isinstance(_food, Food):
            raise TypeError("variable '_food' must be of type 'Food'")

    def set_count(self, _food):
        if not isinstance(_food, Food):
            raise TypeError("variable '_food' must be of type 'Food'")

    def get_details(self):
        pass

      
class Inventory:
    """"""
    id = ""
    stock_count_list = []
    store_list = []
    donation_list = []
    distribution_list = []
    release_date = datetime.datetime.now
    def __init__(self) -> None:
        self.id = str(uuid.uuid1())

    def get_stock_count(self, _food):
        if not isinstance(_food, Food):
            raise TypeError("variable '_food' must be of type 'Food'")

    def get_stock_count_details(self):
        return ""    
    
    def add_donation(self, _donation):
        if not isinstance(_donation, Donation):
            raise TypeError("variable '_donation' must be of type 'Donation'")
        return True
    
    def release_distibution(self, _distribution):
        if not isinstance(_distribution, Distribution):
            raise TypeError("variable '_distribution' must be of type 'Distribution'")
        return True
    
    def get_history(self, _person):
        if not isinstance(_person, Person):
            raise TypeError("variable '_person' must be of type 'Person'")
        return True
    

    person = Person("Robin", "0750111222", "Mukono 1st str")