# this function adds two numbers
def add(x,y):
    print(x+y)


# this function subtracts two numbers
def subtract(x,y):
    print(x-y)



# this function divides two numbers
def divide(x,y):
    print(x/y)


# this function multiplies two numbers
def multiply(x,y):
    print(x*y)



####start of program

print("Welcome to my awesome calc app!!")
print("What would you like to do?")
print("Type (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")

user_choice = input(":  ")
#print(user_choice)

if user_choice == 'a':
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    add(x,y)

elif user_choice == 's':
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    subtract(x,y)

elif user_choice == 'm':
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    multiply(x,y)

elif user_choice == 'd':
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))   
    divide(x,y)

elif user_choice == 'q':
    print("Thanks for using my awesome calc app!!")

else:
    print("Invalid input. Please try again.")  

