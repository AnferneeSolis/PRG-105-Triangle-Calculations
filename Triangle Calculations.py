# the variable cannot be negative
x = raw_input()
y = raw_input()
z = raw_input()
#function
def is_triangle():
    if int(x) + int(y) < int(z):
        print("no.")
    elif int(x) + int(z) < int(y):
        print("no.")
    elif int(y) + int(z) < int(x):
        print("no.")
    else:
        print("yes.")

is_triangle()
#Will still be considered a triangle is the sides create a degerate triangle
