# Application that allows an agent to manage properties available for
# purchase or rent. The project will allow the agent to interact with
# the objects using the Python interpreter prompt.
class Property:
    '''
    Represent the information about some property. Gives specific
    data like number of bedrooms, bathroomd, square feet
    '''

    def __init__(self, square_feet='', beds='', baths=''):
        '''
        Initializing an object...
        '''
        # All essentioal properties
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        '''
        Represent all details about property that is comfortable for user
        '''
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        '''
        Return a dictionary for adding and representing all information
        later
        '''
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))


class Apartment(Property):
    '''
    Represent the information about some apartment. Gives specific
    data like availability of balcony and laundry
    '''
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        '''
        Initializing an object...
        '''
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        '''
        Represent all details about apartment that is comfortable for user
        '''
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        '''
        Return a dictionary for adding and representing all information
        later.
        '''
        # Took the first version of a dictionary in Property class
        parent_init = Property.prompt_init()
        # Asking additional information
        laundry = get_valid_input(
            "What laundry facilities does the property have?",
            Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony? ",
                                  Apartment.valid_balconies)
        # Updating a dictionary
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        # Return updated dictionary
        return parent_init

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    '''
    Get user's input each time when it is needed
    '''
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    # Rules of inputting
    while response.lower() not in valid_options:
        response = input(input_string)
    # Return the answer of user
    return response


class House(Property):
    '''
    Represent the information about some house. Gives specific
    data like aviability of garage, fence and the number of stories
    '''
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        '''
        Initializing an object...
        '''
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        '''
        Represent all details abouthouse that is comfortable for user
        '''
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        '''
        Return a dictionary for adding and representing all information
        later.
        '''
        # Get an old dictionary
        parent_init = Property.prompt_init()
        # Ask the additional information
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")

        # Updating...
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        # Return an updated dictionary
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    '''
    Represent the price and taxes of something
    '''
    def __init__(self, price='', taxes='', **kwargs):
        '''
        Initializing an object...
        '''
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        '''
        Represent all details about price and taxes that is comfortable
        for user
        '''
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        '''
        Return a dictionary for adding and representing all information
        later.
        '''
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? ")
        )

    prompt_init = staticmethod(prompt_init)


class Rental:
    '''
    Represent the information about some property that wil be rented
    '''
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        '''
        Initializing an object...
        '''
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        '''
        Represent all details about price and common data about property
        that is comfortable for user
        '''
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        '''
        Return a dictionary for adding and representing all information
        later.
        '''
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    '''
    For calling another classes and getting information from user about
    a house which will be rented. Kind of boss;)
    '''
    def prompt_init():
        '''
        Update and return the dictionary with all information about a house
        '''
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    '''
    For calling another classes and getting information from user about
    an apartment which will be rented. Kind of boss;)
    '''
    def prompt_init():
        '''
        Update and return the dictionary with all information about an
        apartment
        '''
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    '''
    For calling another classes and getting information from user about
    an apartment which will be purchased. Kind of boss;)
    '''
    def prompt_init():
        '''
        Update and return the dictionary with all information about an
        apartment
        '''
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    '''
    For calling another classes and getting information from user about
    a house which will be purchased. Kind of boss;)
    '''
    def prompt_init():
        '''
        Update and return the dictionary with all information about a house
        '''
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    type_map = {("house", "rental"): HouseRental,
                ("house", "purchase"): HousePurchase,
                ("apartment", "rental"): ApartmentRental,
                ("apartment", "purchase"): ApartmentPurchase}

    def add_property(self):
        property_type = get_valid_input("What type of property? ",
                                        ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ",
                                       ("purchase", "rental")).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
    

agent = Agent()
agent.add_property()
agent.display_properties()
