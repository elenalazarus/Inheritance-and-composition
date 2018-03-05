from property import Agent
from property import Property
from property import House
from property import Purchase
from property import Rental
from property import ApartmentRental
from property import HouseRental
from property import ApartmentPurchase
from property import HousePurchase


agent = Agent()
agent.add_property()
agent.display_properties()

# What type of property?  (house, apartment) apartment
# What payment type?  (purchase, rental) purchase
# Enter the square feet: 20000
# Enter number of bedrooms:
# Enter number of baths: 3
# What laundry facilities does the property have? (coin, ensuite, none) none
# Does the property have a balcony?  (yes, no, solarium) solarium
# What is the selling price? 3225256
# What are the estimated taxes? 35000
# PROPERTY DETAILS
# ================
# square footage: 20000
# bedrooms:
# bathrooms: 3
#
# APARTMENT DETAILS
# laundry: none
# has balcony: solarium
# PURCHASE DETAILS
# selling price: 3225256
# estimated taxes: 35000
# What type of property?  (house, apartment)

print(Property.prompt_init())

# Enter the square feet: 500
# Enter number of bedrooms: 1
# Enter number of baths: 1

# {'square_feet': '500', 'beds': '1', 'baths': '1'}

print(House.prompt_init())

# Enter the square feet: 500
# Enter number of bedrooms: 2
# Enter number of baths: 3
# Is the yard fenced?  (yes, no) no
# Is there a garage?  (attached, detached, none) detached
# How many stories? 5

# {'square_feet': '500', 'beds': '2', 'baths': '3', 'fenced': 'no', 'garage':
# 'detached', 'num_stories': '5'}

print(Purchase.prompt_init())

# What is the selling price? 100000
# What are the estimated taxes? 10000

# {'price': '100000', 'taxes': '10000'}

print(Rental.prompt_init())

# What is the monthly rent? 7000
# What are the estimated utilities? 6
# Is the property furnished?  (yes, no) no

# {'rent': '7000', 'utilities': '6', 'furnished': 'no'}

print(HouseRental.prompt_init())

# Enter the square feet: 130
# Enter number of bedrooms: 2
# Enter number of baths: 1
# Is the yard fenced?  (yes, no) yes
# Is there a garage?  (attached, detached, none) attached
# How many stories? 5
# What is the monthly rent? 1000
# What are the estimated utilities? 8
# Is the property furnished?  (yes, no) yes

# {'square_feet': '130', 'beds': '2', 'baths': '1', 'fenced': 'yes', 'garage':
#     'attached', 'num_stories': '5', 'rent': '1000', 'utilities': '8',
#  'furnished': 'yes'}

print(ApartmentRental.prompt_init())

# Enter the square feet: 60
# Enter number of bedrooms: 2
# Enter number of baths: 1
# What laundry facilities does the property have? (coin, ensuite, none) coin
# Does the property have a balcony?  (yes, no, solarium) yes
# What is the monthly rent? 500
# What are the estimated utilities? 7
# Is the property furnished?  (yes, no) yes

# {'square_feet': '60', 'beds': '2', 'baths': '1', 'laundry': 'coin', 'balcony':
#     'yes', 'rent': '500', 'utilities': '7', 'furnished': 'yes'}

print(ApartmentPurchase.prompt_init())

# Enter the square feet: 300
# Enter number of bedrooms: 4
# Enter number of baths: 3
# What laundry facilities does the property have? (coin, ensuite, none) ensuite
# Does the property have a balcony?  (yes, no, solarium) no
# What is the selling price? 500000
# What are the estimated taxes? 30000
# {'square_feet': '300', 'beds': '4', 'baths': '3', 'laundry': 'ensuite',
#  'balcony': 'no', 'price': '500000', 'taxes': '30000'}

print(HousePurchase.prompt_init())

# Enter the square feet: 10000
# Enter number of bedrooms: 4
# Enter number of baths: 4
# Is the yard fenced?  (yes, no) yes
# Is there a garage?  (attached, detached, none) attached
# How many stories? 5
# What is the selling price? 300000
# What are the estimated taxes? 40000

# {'square_feet': '10000', 'beds': '4', 'baths': '4', 'fenced': 'yes',
# 'garage': 'attached', 'num_stories': '5', 'price': '300000', 'taxes':
# '40000'}

