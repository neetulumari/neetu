# calculator #
first =int(input ("enter first number"))
second =int(input ("enter first number"))
operator =(input ("enter first operator(+,-,*,/,%) :"))
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("invalid number")


