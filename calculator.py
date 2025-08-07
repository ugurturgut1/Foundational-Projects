#Importing Math Class
import math

class Calculator:
#Storing past results
    pastResults = []

    #Factorial
    def Factorial(num1):
        if(num1 == 0 or num1 == 1):
            return 1
        else:
            return num1 * Calculator.Factorial(num1 - 1)

    #Operations
    def Operations(num1,num2):
        if(num2 == 1):
            num3 = float(input("Enter second number: "))
            result = num1 + num3
            print(result)
        if(num2 == 2):
            num3 = float(input("Enter second number: "))
            result = num1 - num3
            print(result)
        if(num2 == 3):
            num3 = float(input("Enter second number: "))
            result = num1 * num3
            print(result)
        if(num2 == 4):
            num3 = float(input("Enter second number: "))
            if(num3 == 0):
                print("Can not divide by 0")
            else:
                result = num1 / num3
                print(result)
        if(num2 == 5):
            num3 = float(input("Enter second number: "))
            result = num1 ** num3
            print(result)
        if(num2 == 6):
            num3 = float(input("Enter second number: "))
            result = num1 ** (1 / num3)
            print(result)
        if(num2 == 7):
            print(Calculator.Factorial(num1))
        if(num2 == 8):
            num1 = -1 * num1
            print(num1)
        if(num2 == 9):
            num3 = float(input("Enter second number: "))
            result = math.log(num1,num3)
            print(result)
        if(num2 == 10):
            result = math.sin(num1)
            print(result)
        if(num2 == 11):
            result = math.cos(num1)
            print(result)
        if(num2 == 12):
            result = math.tan(num1)
            print(result)
        Calculator.pastResults.append(result)

#Getting input from the user       
num1 = float(input("Enter first number: "))

#Choosing operation
num2 = int(input("Choose Operation\n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\5-Power\n6-Root\n7-Factorial\n8-Negation\n9-Logarithm\n10-Sine\n11-Cosine\n12-Tangent\n: "))

Calculator.Operations(num1,num2)
print(f"Past Results: {Calculator.pastResults}")
