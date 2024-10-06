
#Write Python code that prints your name, student number and email address
# print("Seetha V")
# print("32")
# print("seetha917@gmail.com")

# Write Python code that prints your name, student number and email address using escape sequences.
# print("Seetha V\n32\nseetha917@gmail.com")

# Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.
# x=14
# y=7
# print(x,"+",y,"=",x+y)
# print(x,"*",y,"=",x*y)
# print(x,"-",y,"=",x-y)
# print(x,"/",y,"=",x//y)

# Write Python code that displays the numbers from 1 to 5 as steps.
# for i in range(1,6):
#     print(i)

# Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:
# An example runs of the program: "SDK" stands for "Software Development Kit", whereas "IDE" stands for "Integrated Development Environment".
# print('\"SDK\" stands for \"Software Development Kit\", whereas\n\"IDE\" stands for \"Integrated Development Environment\" ')

#Practice and check the output
# print("python is an \"awesome\" language.")
# print("python\n\t2023")
# print('I\'m from Entri.\b')
# print("\65")
# print("\x65")
# print("Entri", "2023", sep="\n")
# print("Entri", "2023", sep="\b")
# print("Entri", "2023", sep="*", end="\b\b\b\b")

#Define the variables below. Print the types of each variable.
#What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum? num=23 textnum="57" decimal=98.3
# num=23
# textnum="57"
# decimal=98.3
#
# print("TYPE OF NUM IS",type(num))
# print("TYPE OF TEXTSUM IS",type(textnum))
# print("TYPE OF DECIMAL IS",type(decimal))
#
# sum = num + int(textnum) + decimal
# print("SUM=",sum)
# print("TYPE OF SUM IS",type(sum))

# calculate the number of minutes in a year using variables for each unit of time. print a statement that describes what your code does also.
# Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and
# print the values (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour
# Variables for time units
# no_of_days_in_year = 365
# hours_in_a_day = 24
# minutes_in_a_hour = 60
#
# total_minutes_in_an_year = no_of_days_in_year * hours_in_a_day * minutes_in_a_hour
#
# print("This code calculates the total number of minutes in a year.")
# print("Total minutes in a year:", total_minutes_in_an_year,"minutes")

#Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
#An example runs of the program: Please enter you name: Tony Hi Tony, welcome to Python programming :)
# Ask the user to enter their name

user_name = input("Please enter your name: ")
print(f"Hi {user_name}, Welcome to Python programming :)")

