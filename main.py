# calculator using functions
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


print("Enter choices +,-,*,/")

print("1 for addition")
print("2 for substration")
print("3 for multiply")
print("4 for Devision")
# Enter operator
x = int(input("Enter any number for choosing operator listed above\n"))

# Enter input operands

n1 = float(input("Enter first Number"))
n2 = float(input("Enter Second Number"))

if x == 1:
    print(n1, "+", n2, "=", add(n1, n2))

elif x == 2:
    print(n1, "-", n2, "=", sub(n1, n2))

elif x == 3:
    print(n1, "*", n2, "=", multi(n1, n2))

elif x == 4:
    print(n1, "/", n2, "=", div(n1, n2))

else:
    print("Invalid operator")
