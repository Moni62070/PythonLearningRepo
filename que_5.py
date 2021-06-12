x=int(input("Enter your first number: "))
y=int(input("Enter your second number: "))
choice=input("select operation.")
print("select operation")
print("+")
print("-")
print("*")
print("/")

if choice =='+':
    print('{}+{}='.format(x,y))
    print(x+y)
elif choice == '-':
    print('{}-{}='.format(x,y))
    print(x-y)
elif choice == '*':
    print('{}*{}='.format(x,y))
    print(x*y)
elif choice =='/':
    print('{}/{}='.format(x,y))
    print(x/y)
else:
    print('Enter a valid operator, please run the program again,Thank you.!!!!!!!!!!!')
    


