import name

def main():
    print('''Simple Calculator
~~~~~~~~~~~~~~~~~~''')
    n = name.name()

    a = int(input("Enter a value for A : "))
    b = int(input("Enter a value for B : "))
    print('''

Enter + for Addition
Enter - for Subraction
Enter * for Multiplication
Enter / for Division
Enter square for square
''')
    op = input("Enter the operator to operate : ")

    if '+' in op:
        print("answer : ",a+b)
    elif '-' in op:
        print("answer : ",a-b)
    elif '*' in op:
        print("answer : ",a*b)
    elif '/' in op:
        print("answer : ",a/b)
    elif 'square' in op:
        ans = 0
        while (b>0):
            ans += a*a
            b = b-1
        print("answer : ",ans)

if __name__ == "__main__":
    main()
