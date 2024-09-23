'''# This is where I will document variaous ways to write Hello, World! and the basics of Python

# The most simple way
print("Hello, World!")

# Hello, World! as a variable
helloworld = "Hello, World!"
print(helloworld)

# Artirhmatic Operators
x = 2
y = 3
print(x + y)    # Addition + operator returns the sum of x plus y
print(x - y)    # Subtraction - operator returns the difference of x minus y
print(x * y)    # Multiplication * operator returns the product of x times y
print(x / y)    # Division / operator returns the quotient of x divided by y
print(x**y)     # Exponent ** operator returns the result of raising x to the power of y 
print(x**2)     # Square expression returns x squared
print(x**3)     # Cube expression returns x cubed
print(x**(1/2)) # Square root (½) or (0.5) fractional exponent operator returns the square root of x
print(x // y)   # Floor division operator returns the integer part of the integer division of x by y
print(x % y)    # Modulo operator returns the remainder part of the integer division of x by y'''

'''# Function luas lingkaran
def luas_lingkaran(r):
    x = 22/7 * r**2
    return "Luas lingkaran dengan diameter " + str(r*2) + "adalah " + str(x)

print(luas_lingkaran(7))
'''
def main():
    arr = [2, 7, 20, 19, 27]
    n = len(arr)
    x, y = 0, 0

    for i in range(n):
        if arr[i] % 2 != 0:
            x += 1
        else:
            y += 1

    print("X = %d, " % x, end="")
    print("Y = %d" % y)

if __name__ == "__main__":
    main()