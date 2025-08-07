class Fibonacci:

    #Start of the fibonacci series
    fibonacci = [0,1]

    #Generate the fibonacci series until the user-defined limit
    def generate(limit):
        if(limit<=len(Fibonacci.fibonacci)):
            print(f"The fibonacci series is: {Fibonacci.fibonacci}")
        else:
            for i in range(limit-2):
                Fibonacci.fibonacci.append(Fibonacci.fibonacci[-1]+Fibonacci.fibonacci[-2])
            print(f"The fibonacci series is: {Fibonacci.fibonacci}")
        
    #Calculate the partial sum until the user-defined limit
    def partialSum(limit):
        Fibonacci.generate(limit)
        sum = 0
        for i in range(limit):
            sum = sum + Fibonacci.fibonacci[i]
        print(f"The partial sum is: {sum}")

    #User input and method selection
    def main():
        print("Welcome to the fibonacci series generator!")
        print("Choose if you want to generate the series or calculate the partial sum (1/2)")
        choice = int(input("Enter 1 or 2: "))
        if(choice == 1):
            limit = int(input("Enter the number of fibonacci numbers to generate: "))
            while(limit<0):
                limit = int(input("Please enter another number: "))
            Fibonacci.generate(limit)
        elif(choice == 2):
            limit = int(input("Enter the number of fibonacci numbers to generate: "))
            while(limit<0):
                limit = int(input("Please enter another number: "))
            Fibonacci.partialSum(limit)
        else:
            print("Invalid Input")
    
#Calling the method
Fibonacci.main()
    
