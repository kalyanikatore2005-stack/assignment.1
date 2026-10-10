#1. Check Positive, Negative, or Zero

n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
  
  
#2. Check Even or Odd


n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")    
 
 #3. Greater of Two Numbers
 
 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater:", a)
elif b > a:
    print("Greater:", b)
else:
    print("Both are equal")
    
 #4. Greatest of Three Numbers
 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)
    
 #5. Voting Eligibility
 
 
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    
 #6. Check Leap Year
 
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
    
    
#7. Vowel or Consonant

ch = input("Enter an alphabet: ").lower()

if len(ch) == 1 and ch.isalpha():
    if ch in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Enter a single alphabet")
    
#8. Divisible by 5 and 11

n = int(input("Enter a number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by both")
    
    
#9. Multiple of Both 3 and 7

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both")
    
    
#10. Assign Grades Based on Marks

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
    
    
#11. Uppercase or Lowercase

ch = input("Enter a character: ")

if len(ch) == 1 and ch.isupper():
    print("Uppercase")
elif len(ch) == 1 and ch.islower():
    print("Lowercase")
else:
    print("Not an alphabetic character")
    
#12. Vowel Using if-elif

ch = input("Enter an alphabet: ").lower()

if ch == "a":
    print("Vowel")
elif ch == "e":
    print("Vowel")
elif ch == "i":
    print("Vowel")
elif ch == "o":
    print("Vowel")
elif ch == "u":
    print("Vowel")
else:
    print("Consonant or invalid input")
    
    
#13. Check Whether Three Sides Form a Triangle

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Triangle is possible")
else:
    print("Triangle is not possible")
    
    
#14. Type of Triangle

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    
    
#15. Largest Among Four Numbers

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if a >= b and a >= c and a >= d:
    print("Largest:", a)
elif b >= a and b >= c and b >= d:
    print("Largest:", b)
elif c >= a and c >= b and c >= d:
    print("Largest:", c)
else:
    print("Largest:", d)
    
    
#16. Check Three-Digit Number

n = int(input("Enter a number: "))

if 100 <= abs(n) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")
    
    
#17. Electricity Bill Using Slab Rates


units = int(input("Enter units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.50
    print("Bill:", bill)
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
    print("Bill:", bill)
else:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4
    print("Bill:", bill)
    
    
#18. Income Tax Based on Income Slabs


income = float(input("Enter income: "))

if income < 0:
    print("Invalid income")
elif income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 0.05
else:
    tax = 300000 * 0.05 + (income - 600000) * 0.10

if income >= 0:
    print("Tax:", tax)
    
#19. Student Pass or Fail



a = int(input("Enter subject 1 marks: "))
b = int(input("Enter subject 2 marks: "))
c = int(input("Enter subject 3 marks: "))

if a < 0 or b < 0 or c < 0 or a > 100 or b > 100 or c > 100:
    print("Invalid marks")
elif a >= 35 and b >= 35 and c >= 35:
    print("Pass")
else:
    print("Fail")
    
#20. Check Whether a Number Is Within a Range

n = int(input("Enter a number: "))

if 10 <= n <= 50:
    print("Within range")
else:
    print("Outside range")
    
#21. Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
    
#22. Century Leap Year

year = int(input("Enter year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year, not a leap year")
elif year % 4 == 0:
    print("Leap year, not a century year")
else:
    print("Not a leap year")
    
#23. Determine Season by Month



month = int(input("Enter month (1-12): "))

if month in (12, 1, 2):
    print("Winter")
elif month in (3, 4, 5):
    print("Spring")
elif month in (6, 7, 8):
    print("Summer")
elif month in (9, 10, 11):
    print("Autumn")
else:
    print("Invalid month")
    
#24. Number of Days in a Month

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
elif month in (4, 6, 9, 11):
    print("30 days")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
else:
    print("Invalid month")
    
#25. Password Validation


password = input("Enter password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Password meets the conditions")
else:
    print("Password must have 8 characters and a digit")
    
#26. Ticket Price Based on Age

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 12:
    print("Ticket price: ₹50")
elif age < 60:
    print("Ticket price: ₹100")
else:
    print("Ticket price: ₹70")
    
#27. Discount Based on Purchase Amount


amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = amount * 0.20
    print("Discount:", discount)
elif amount >= 2000:
    discount = amount * 0.10
    print("Discount:", discount)
else:
    discount = 0
    print("No discount")

if amount >= 0:
    print("Final amount:", amount - discount)
    
#28. Driving License Eligibility


age = int(input("Enter age: "))
eyesight = input("Pass eyesight test? (yes/no): ").lower()

if age >= 18 and eyesight == "yes":
    print("Eligible to apply")
else:
    print("Not eligible")
    
#29. Login System

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")            
    
    # 30. Menu-Driven Calculator

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you!")
        break
    elif choice in ("1", "2", "3", "4"):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")
    else:
        print("Invalid choice")