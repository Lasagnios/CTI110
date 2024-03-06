##Enrique Noriega
##3/6/2024
##P2HW2
##This program will find the highest,lowest,sum, and average of your grades 

my_list = []
x= float(input(" Enter grade for Module 1: "))
my_list.append(x)
x= float(input(" Enter grade for Module 2: "))
my_list.append(x)
x= float(input(" Enter grade for Module 3: "))
my_list.append(x)
x= float(input(" Enter grade for Module 4: "))
my_list.append(x)
x= float(input(" Enter grade for Module 5: "))
my_list.append(x)
x= float(input(" Enter grade for Module 6: "))
my_list.append(x)
print()
print("------------Results------------")
lowest = min(my_list)
print(f"Lowest Grade:        {lowest:.2f}")
highest = max(my_list)
print(f"Highest Grade:       {highest:.2f}")
sum1 = sum(my_list)
print(f"Sum of Grades:       {sum1:.2f}")
length = len(my_list)
ave = sum1/length
print(f"Average:             {sum(my_list)/len(my_list):.2}")
print("----------------------------------------")

##Psudocode
##User inputs their grades from modules 1-6
##Program then sorts the lowest and highest grade
##Program then adds all the values and calculates the sum of grades
##Program finally uses the sum and divides it by the length to find the average
