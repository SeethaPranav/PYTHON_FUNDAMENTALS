# PYTHON_FUNDAMENTALS
Python basic program covering python fundamentals

1.Write Python code that prints your name, student number and email address 

print(“Seetha V”)
print(“32”)
print(“seetha917@gmail.com”)

![image](https://github.com/user-attachments/assets/9966c234-6eb3-451a-b612-52ddd84c1a9c)

 

2.Write Python code that prints your name, student number and email address using escape sequences.  

print(“Seetha V\n32\nseetha917@gmail.com”)

![image](https://github.com/user-attachments/assets/59faa0a6-e1ce-42e1-aa74-0f6e076b4ffb)

 
3.Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.

x=14
y=7
print( x , "+", y , "=", x+y )
print( x , "*", y ,"=", x*y )
print( x , "-" , y , "=" , x-y )
print( x , "/" , y , "=" , x//y )

![image](https://github.com/user-attachments/assets/ab0be74b-e322-46d1-978f-2aa1c6fe587f)


4.Write Python code that displays the numbers from 1 to 5 as steps. 

for i in range(1,6):
    print(i)  
    
![image](https://github.com/user-attachments/assets/78922213-0127-4c9b-851b-073d6b70af8f)

 
5.Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen: An example runs of the program: "SDK" stands for "Software Development Kit", whereas "IDE" stands for "Integrated Development Environment". 

print( ' \"SDK\" stands for \"Software Development Kit\", whereas\n\"IDE\" stands
for \"Integrated Development Environment\" ' )

![image](https://github.com/user-attachments/assets/6e7b1c23-a170-49ea-b46f-1eaf6dd7440b)

 
6. Practice and check the output print("python is an \"awesome\" language.") print("python\n\t2023") print('I\'m from Entri.\b') print("\65") print("\x65") print("Entri", "2023", sep="\n") print("Entri", "2023", sep="\b") print("Entri", "2023", sep="*", end="\b\b\b\b")
   
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

![image](https://github.com/user-attachments/assets/19408478-fe88-4c73-9faf-0d40e18b75bc)

 
7. Define the variables below. Print the types of each variable. What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum? num=23 textnum="57" decimal=98.3
8. 
num=23
textnum="57"
decimal=98.3

print("TYPE OF NUM IS", type(num))
print("TYPE OF TEXTSUM IS", type(textnum))
print("TYPE OF DECIMAL IS", type(decimal))

sum = num + int(textnum) + decimal
print("SUM=",sum)
print("TYPE OF SUM IS", type(sum))

![image](https://github.com/user-attachments/assets/693d3d4f-b651-4104-af1a-cbc2833a8593)

 
8.Calculate the number of minutes in a year using variables for each unit of time. print a statement that describes what your code does also. Create three variables to store no of days in a year, minute in a hour, hours in a day, then calculate the total minutes in a year and print the values (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour

no_of_days_in_year = 365
hours_in_a_day = 24
minutes_in_a_hour = 60

total_minutes_in_an_year = no_of_days_in_year * hours_in_a_day * minutes_in_a_hour

print("This code calculates the total number of minutes in a year.")
print("Total minutes in a year:", total_minutes_in_an_year,"minutes")

![image](https://github.com/user-attachments/assets/8ae37f66-4ab0-45fa-a061-f5fce6297b7e)

 
9. Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting. An example runs of the program: Please enter you name: Tony Hi Tony, welcome to Python programming :)
    
 user_name = input("Please enter your name: ")
 
print(f "Hi {user_name}, Welcome to Python programming :)")

![image](https://github.com/user-attachments/assets/c8d6685f-ff1b-49ef-baa0-83c2517c02cb)

 
10. Name your file: PoundsToDollars.py Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($) An example runs of the program: Please enter amount in pounds: XXX £ XXX are $ XXX
     
pounds = float(input("Please enter amount in pounds (£): "))
dollars = pounds * 1.33

print(f"£{pounds} = ${dollars}")

![image](https://github.com/user-attachments/assets/d9a30d75-79e3-47c6-8bc5-be84e1925b72)

 

