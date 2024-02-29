# Enrique Noriega
# 2/29/2024
# P2LAB2
# A program that will create a dictionary where the key and value pairs are as follows


car_dict = {
    "Camero": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
    }
car_list = car_dict
print("The keys in the dictionary are:")
print(*car_list, sep=", ")
print()
vehicle = input("Enter a vehicle to see it's mpg: ")
print()
mpg = car_dict[vehicle]
print("The", vehicle, "gets", mpg, "mpg.")
print()
miles = float(input("How many miles will your drive the Silverado? "))
gallons = miles/mpg
print(f'{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.')
