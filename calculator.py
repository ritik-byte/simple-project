first=input("enter your first no.: ")
operator=input("enter your operater(+,-,*,/,%).:")
second=input("enter your 2nd no.:")
first=int(first)
second=int(second)
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
    print("invailid operater")
