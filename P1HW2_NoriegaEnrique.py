#Enrique Noriega
#2/20/2024
#P1HW2
#This program will calculate a budget

print("This program calculates and displays travel expenses")

user_num=int(input("Enter your budget: "))
print("")
dest=input("Enter your destination: ")
print("")
gmon= int(input("How much do you think you will spend on gas? "))
print("")
hmon= int(input("How much do you think you need for accomodation/hotel? "))
print("")
fmon= int(input("Last, how much do you need for food? "))
print("")
print("------------Travel Expenses------------")
print("Location:",dest)
print("Initial Budget:", user_num)
print("")
print("Fuel:", gmon)
print("Accomodation:", hmon)
print("Food:", fmon)
print("")
print("Remaining Balance:", user_num-gmon-hmon-fmon)

##Pseudocode
#Took the budget, destination, gas, accomodation and hotel, food expenses
#Displayed the Travel Expenses and calculated the remaining balance
