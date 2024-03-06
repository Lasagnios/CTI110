##Enrique Noriega
##3/6/2024
##P2HW1
##This is a formated version of a program that will calculate travel expenses
print("This program calculates and displays travel expenses")

user_num=int(input("Enter your budget: "))
user_num= float(user_num)
print("")
dest=input("Enter your destination: ")

print("")
gmon= int(input("How much do you think you will spend on gas? "))
gmon=float(gmon)
print("")
hmon= int(input("How much do you think you need for accomodation/hotel? "))
hmon=float(hmon)
print("")
fmon= int(input("Last, how much do you need for food? "))
fmon=float(fmon)
print("")
print("------------Travel Expenses------------")
print("Location:          ", "$", dest)
print(f'Initial Budget:     ${user_num:.2f}')
print(f"Fuel:               ${gmon:.2f}")
print(f"Accomodation:       ${hmon:.2f}")
print(f"Food:               ${fmon:.2f}")
print("---------------------------------------")
print()
total= user_num-gmon-hmon-fmon
print(f"Remaining Balance:  ${total:.2f}")

