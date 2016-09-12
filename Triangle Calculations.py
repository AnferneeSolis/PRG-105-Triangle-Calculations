# numbers need to be given smallest to largest
x = raw_input()
y = raw_input()
z = raw_input()

def is_triangle():
    if x + y > z:
        print("yes.")
    if x + z > y:
        print("yes")
    if y + z > x:
        print("yes")
    else:
        print("no.")
# if any of the checks fail, then the sides do not create a triangle.
is_triangle()
