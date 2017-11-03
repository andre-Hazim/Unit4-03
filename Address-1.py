# Created by : Andre Hazim and Ray Octavious
# Created on : 30 Oct. 2017
# Created for : ICS3UR
# this program nicely displays the users address information

def address (apt_number , street_address , city , province , postal_code):
    if apt_number == "":
        print(street_address + "," + city + "," + province + "," + postal_code)
    else:
        print(apt_number + "," + street_address + "," + city + "," + province + "," + postal_code)

apartment = raw_input("Do you live in an apartment: ")

if apartment == "yes"  :
   apartment_number = raw_input("What is the apartment number: ")
   street_address_number = raw_input("What is the street address: ")
   living_city = raw_input("What city do you live in: ")
   living_province = raw_input("What province do you live in: ")
   living_postal_code = raw_input("What is your postal code: ")
else:
   street_address_number = raw_input("What is the street address: ")
   living_city = raw_input("What city do you live in: ")
   living_province = raw_input("What province do you live in: ")
   living_postal_code = raw_input("What is your postal code: ")
if apartment == "yes"  :
    print ("Your Apartment: " + apartment_number)
print("Your Street address is: " + street_address_number)
print("Your City: " +living_city)
print("Your Province: " +living_province)
print("Your Postal Code: " +living_postal_code)
