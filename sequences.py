class Sequence:

#Getting input from the user
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    num3 = float(input("Enter your third number: "))
    n = int(input("Enter the maximum term number: "))

#Handling the "division by 0" errors
    if(num1 == 0):
            num1 = float(input("Enter another first number: "))
    if(num2 == 0):
            num2 = float(input("Enter another second number: "))
    if(num3 == 0):
            num3 = float(input("Enter another third number: "))

    numlist = [num1, num2, num3] 
    
#Determining if a sequence progresses geometrically or arithmetically 
    def determine(numlist,n):
        if len(numlist) != 3:
            return False
        num1, num2, num3 = numlist
        if(num1 == num2 and num2 == num3):
            print("The sequence is both geometric and arithmetic")
        else:
            if(num2/num1 == num3/num2):
                print("The sequence is geometric")
                ratio = num2/num1
                for i in range(3,n):
                    numlist.append(numlist[i-1]*ratio) 
                    print(f"The {i+1}. term is: {numlist[i]}") 
            elif(num2-num1 == num3-num2):
                print("The sequnce is arithmetic")
                difference = num2-num1
                for i in range(3,n):
                    numlist.append(numlist[i-1]+difference)
                    print(f"The {i+1}. term is: {numlist[i]}")
            else:
                    print("The sequence is neither geometric nor arithmetic")
             

#Calculating partial sums
    def partialSum(numlist,n):
            sum = 0
            for i in range(len(numlist)):
                sum = sum + numlist[i]
            print(f"The partial sum of the sequence is: {sum}")

#Calling the student developed procedures
Sequence.determine(Sequence.numlist,Sequence.n) 
Sequence.partialSum(Sequence.numlist,Sequence.n) 
