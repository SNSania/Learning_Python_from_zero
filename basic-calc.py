print("Perform basic calculations")
print("select an option between 1 and 4")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
    
choice = float(input("Select your option"))   #input from user
    
if(choice in [1,2,3,4]):
    if(choice == 1):
        print("Addition")    #addition
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = (num1 + num2)
    elif(choice == 2):
        print("Subtraction") #subtraction
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = (num1 - num2)  
    elif(choice == 3):
        print("Multiplication") #multiplication   
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = (num1 * num2)  
    elif(choice == 4):
        print("Division") #division
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = (num1 / num2)


    else:
        print("Invalid option")

print("The result of this calculation is ", format(result)) 

    #next_calculation = input("Let's do next calculation? (yes/no): ")
       # if next_calculation == "no":
         # break
    #else:
      #  print("Invalid Input")