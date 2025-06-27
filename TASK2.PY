Number1=int(input("enter first number"))
Number2=int(input("enter second number"))
operator=input("enter your operator(+,-,*,/): ")
if operator == '+':
    print("Addition of number1 and number2 is",Number1+Number2)
elif operator == '-':
    print("Subtraction of number1 and number2 is",Number1-Number2)
elif operator == '*':
    print("Multiplication of number1 and number2 is",Number1*Number2)
elif operator=='/':
    if Number2!=0:
        print("Division of number1 and number2 is",Number1/Number2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid ooperator.")