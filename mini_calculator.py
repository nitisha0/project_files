                                                #mini calculator
first= int(input("enter first number : "))
second= int(input("enter second number : "))
operator= input("enter operator (+,-,*,% ) : ")

if operator == "+":
    print (first + second)
elif operator == "-":
    print (first - second)
elif operator == "%":
    print (first % second)
elif  operator == "*":
    print (first * second)
else:
    print ("invalid operation")