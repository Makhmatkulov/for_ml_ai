import math

# Problem 1 - Perimeter of a square
def square_perimeter():
    a = float(input("Enter the side length of the square: "))
    perimeter = 4 * a
    print(f"Perimeter of the square: {perimeter}")

# Problem 2 - Area of a square
def square_area():
    a = float(input("Enter the side length of the square: "))
    area = a ** 2
    print(f"Area of the square: {area}")

# Problem 3 - Area and perimeter of a rectangle
def rectangle_area_perimeter():
    a = float(input("Enter the length of the rectangle: "))
    b = float(input("Enter the width of the rectangle: "))
    area = a * b
    perimeter = 2 * (a + b)
    print(f"Area: {area}, Perimeter: {perimeter}")

# Problem 4 - Circumference of a circle given diameter
def circle_circumference():
    d = float(input("Enter the diameter of the circle: "))
    L = math.pi * d
    print(f"Circumference of the circle: {L}")

# Problem 5 - Volume and surface area of a cube
def cube_volume_surface_area():
    a = float(input("Enter the side length of the cube: "))
    volume = a ** 3
    surface_area = 6 * a ** 2
    print(f"Volume: {volume}, Surface area: {surface_area}")

# Problem 6 - Volume and surface area of a parallelepiped
def parallelepiped_properties():
    a = float(input("Enter the length: "))
    b = float(input("Enter the width: "))
    c = float(input("Enter the height: "))
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + a * c)
    print(f"Volume: {volume}, Surface area: {surface_area}")

# Problem 7 - Circumference and area of a circle given radius
def circle_properties():
    R = float(input("Enter the radius of the circle: "))
    L = 2 * math.pi * R
    area = math.pi * R ** 2
    print(f"Circumference: {L}, Area: {area}")

# Problem 8 - Arithmetic mean of two numbers
def arithmetic_mean():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    mean = (a + b) / 2
    print(f"Arithmetic mean: {mean}")

# Problem 9 - Geometric mean of two positive numbers
def geometric_mean():
    a = float(input("Enter the first positive number: "))
    b = float(input("Enter the second positive number: "))
    mean = math.sqrt(a * b)
    print(f"Geometric mean: {mean}")

# Problem 10 - Sum, product, and squares of two numbers
def sum_product_square():
    a = float(input("Enter the first non-zero number: "))
    b = float(input("Enter the second non-zero number: "))
    sum_ab = a + b
    product_ab = a * b
    squares = a ** 2 + b ** 2
    print(f"Sum: {sum_ab}, Product: {product_ab}, Sum of squares: {squares}")

# Problem 11 - Sum, difference, and absolute difference of two numbers
def sum_difference_abs():
    a = float(input("Enter the first non-zero number: "))
    b = float(input("Enter the second non-zero number: "))
    sum_ab = a + b
    difference_ab = abs(a - b)
    abs_a = abs(a)
    abs_b = abs(b)
    print(f"Sum: {sum_ab}, Absolute difference: {difference_ab}, |a|: {abs_a}, |b|: {abs_b}")

# Problem 12 - Hypotenuse and perimeter of a right triangle
def right_triangle_properties():
    a = float(input("Enter the first leg of the triangle: "))
    b = float(input("Enter the second leg of the triangle: "))
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    perimeter = a + b + hypotenuse
    print(f"Hypotenuse: {hypotenuse}, Perimeter: {perimeter}")

# Problem 13 - Difference of areas of two concentric circles
def concentric_circle_areas():
    R1 = float(input("Enter the radius of the larger circle: "))
    R2 = float(input("Enter the radius of the smaller circle: "))
    if R1 > R2:
        area1 = math.pi * R1 ** 2
        area2 = math.pi * R2 ** 2
        area_difference = area1 - area2
        print(f"Area of larger circle: {area1}, Area of smaller circle: {area2}, Difference: {area_difference}")
    else:
        print("R1 must be greater than R2.")

# Problem 14 - Circumference and area of a circle given length
def circle_by_length():
    L = float(input("Enter the circumference of the circle: "))
    R = L / (2 * math.pi)
    area = math.pi * R ** 2
    print(f"Radius: {R}, Area: {area}")

# Problem 15 - Diameter and radius of a circle given area
def circle_by_area():
    S = float(input("Enter the area of the circle: "))
    R = math.sqrt(S / math.pi)
    d = 2 * R
    print(f"Radius: {R}, Diameter: {d}")


# Problem 16 - Distance between two points on a number line
def distance_between_points():
    x1 = float(input("Enter point 1 (x1): "))
    x2 = float(input("Enter point 2 (x2): "))
    distance = abs(x2 - x1)
    print(f"Distance between points: {distance}")


# Problem 17 - Calculate AC and BC segment lengths
def segment_lengths():
    A = float(input("Enter point A: "))
    B = float(input("Enter point B: "))
    C = float(input("Enter point C: "))
    AC = abs(C - A)
    BC = abs(C - B)
    print(f"AC length: {AC}, BC length: {BC}")


# Problem 19 - Perimeter and area of a rectangle
def rectangle_properties():
    x1 = float(input("Enter x1 coordinate of one corner: "))
    y1 = float(input("Enter y1 coordinate of one corner: "))
    x2 = float(input("Enter x2 coordinate of opposite corner: "))
    y2 = float(input("Enter y2 coordinate of opposite corner: "))
    length = abs(x2 - x1)
    width = abs(y2 - y1)
    perimeter = 2 * (length + width)
    area = length * width
    print(f"Perimeter: {perimeter}, Area: {area}")


# Problem 20 - Distance between two points in 2D space
def distance_2d(x1=None, y1=None, x2=None, y2=None):
    if x1 is None:
        x1 = float(input("Enter x1: "))
    if y1 is None:
        y1 = float(input("Enter y1: "))
    if x2 is None:
        x2 = float(input("Enter x2: "))
    if y2 is None:
        y2 = float(input("Enter y2: "))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# Problem 21 - Area of a triangle using Heron's formula
def triangle_area():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))
    a = distance_2d(x1, y1, x2, y2)
    b = distance_2d(x2, y2, x3, y3)
    c = distance_2d(x3, y3, x1, y1)
    s = (a + b + c) / 2  # semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Area of the triangle: {area}")


# Problems 22, 23, 24 - Swap values of A, B, C
def swap_values():
    A = float(input("Enter value of A: "))
    B = float(input("Enter value of B: "))
    C = float(input("Enter value of C: "))
    print(f"Original: A = {A}, B = {B}, C = {C}")

    # Swap A with B
    A, B = B, A
    print(f"After swapping A and B: A = {A}, B = {B}, C = {C}")

    # Swap A with C
    A, C = C, A
    print(f"After swapping A and C: A = {A}, B = {B}, C = {C}")


# Problem 25 - Evaluate cubic function
def evaluate_cubic():
    x = float(input("Enter value of x: "))
    result = 3 * x ** 5 - 6 * x ** 2 - 7
    print(f"Cubic function result: {result}")


# Problem 26 - Evaluate quartic function
def evaluate_quartic():
    x = float(input("Enter value of x: "))
    result = 4 * (x - 3) ** 5 - 7 * (x - 3) ** 3 + 2
    print(f"Quartic function result: {result}")


# Problem 27 - Calculate powers of a number
def power_of_number():
    base = float(input("Enter base number: "))
    exponent = int(input("Enter exponent: "))
    result = base ** exponent
    print(f"Result of {base}^{exponent}: {result}")


# Problem 28 - Power of a number (specific exponents)
def specific_powers():
    A = float(input("Enter value of A: "))
    print(f"A^2: {A ** 2}, A^3: {A ** 3}, A^15: {A ** 15}")


# Problem 29 - Convert degrees to radians
def degrees_to_radians():
    deg = float(input("Enter angle in degrees: "))
    rad = math.radians(deg)
    print(f"{deg} degrees is {rad} radians")


# Problem 30 - Convert radians to degrees
def radians_to_degrees():
    rad = float(input("Enter angle in radians: "))
    deg = math.degrees(rad)
    print(f"{rad} radians is {deg} degrees")


# Problem 31 and 32 - Fahrenheit to Celsius and Celsius to Fahrenheit
def fahrenheit_to_celsius():
    T_F = float(input("Enter temperature in Fahrenheit: "))
    T_C = (T_F - 32) * 5 / 9
    print(f"Temperature in Celsius: {T_C}")


def celsius_to_fahrenheit():
    T_C = float(input("Enter temperature in Celsius: "))
    T_F = (T_C * 9 / 5) + 32
    print(f"Temperature in Fahrenheit: {T_F}")


# Problem 33 - Total cost of X kg of candy A and Y kg of candy B
def total_candy_cost():
    X = float(input("Enter the weight of candy A (in kg): "))
    Y = float(input("Enter the weight of candy B (in kg): "))
    price_A = float(input("Enter the price per kg of candy A: "))
    price_B = float(input("Enter the price per kg of candy B: "))
    total_cost = X * price_A + Y * price_B
    print(f"Total cost: {total_cost}")


# Problem 34 - Cost of 1 kg chocolate if given cost of X kg chocolate and Y kg candy B
def chocolate_cost():
    X = float(input("Enter the weight of chocolate (in kg): "))
    Y = float(input("Enter the weight of candy (in kg): "))
    total_cost = float(input("Enter the total cost: "))
    price_per_kg = total_cost / (X + Y)
    print(f"Cost of 1 kg of chocolate: {price_per_kg}")


# Problem 35 - Calculate distance for a boat against and with current
def boat_distance():
    U = float(input("Enter boat's speed with current (in km/h): "))
    V = float(input("Enter boat's speed against current (in km/h): "))
    T1 = float(input("Enter time moving with the current (in hours): "))
    T2 = float(input("Enter time moving against the current (in hours): "))
    distance_with_current = U * T1
    distance_against_current = V * T2
    print(f"Distance with current: {distance_with_current}, Distance against current: {distance_against_current}")


# Problem 36 - Distance between two cars moving in the same direction
def cars_distance_same_direction():
    V1 = float(input("Enter speed of car 1 (in km/h): "))
    V2 = float(input("Enter speed of car 2 (in km/h): "))
    S = float(input("Enter initial distance between the cars (in km): "))
    T = float(input("Enter time after which you want to find the distance (in hours): "))
    distance = S + (V2 - V1) * T
    print(f"Distance between the cars after {T} hours: {distance}")


# Problem 37 - Distance between two cars moving towards each other
def cars_distance_opposite_direction():
    V1 = float(input("Enter speed of car 1 (in km/h): "))
    V2 = float(input("Enter speed of car 2 (in km/h): "))
    S = float(input("Enter initial distance between the cars (in km): "))
    T = float(input("Enter time after which you want to find the distance (in hours): "))
    distance = S - (V1 + V2) * T
    print(f"Distance between the cars after {T} hours: {distance}")


# Problem 38 - Solve linear equation Ax + B = 0
def solve_linear_equation():
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter constant B: "))
    if A != 0:
        x = -B / A
        print(f"Solution for the equation {A}x + {B} = 0: x = {x}")
    else:
        print("No solution (A cannot be zero)")


# Problem 39 - Solve quadratic equation Ax^2 + Bx + C = 0
def solve_quadratic():
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    C = float(input("Enter coefficient C: "))
    discriminant = B ** 2 - 4 * A * C
    if discriminant < 0:
        print("No real solutions")
    elif discriminant == 0:
        x = -B / (2 * A)
        print(f"One solution: x = {x}")
    else:
        root1 = (-B + math.sqrt(discriminant)) / (2 * A)
        root2 = (-B - math.sqrt(discriminant)) / (2 * A)
        print(f"Two solutions: x1 = {root1}, x2 = {root2}")


# Problem 40 - Solve system of linear equations
def solve_system():
    A1 = float(input("Enter A1: "))
    B1 = float(input("Enter B1: "))
    C1 = float(input("Enter C1: "))
    A2 = float(input("Enter A2: "))
    B2 = float(input("Enter B2: "))
    C2 = float(input("Enter C2: "))
    determinant = A1 * B2 - A2 * B1
    if determinant == 0:
        print("No unique solution (determinant is 0)")
    else:
        x = (C1 * B2 - C2 * B1) / determinant
        y = (A1 * C2 - A2 * C1) / determinant
        print(f"Solution: x = {x}, y = {y}")


# Call the desired functions
# problem 1
square_perimeter()

# problem 2
# square_area()

# problem 3
# rectangle_area_perimeter()

# problem 4
# circle_circumference()

# problem 5
# cube_volume_surface_area()

# problem 6
# parallelepiped_properties()

# problem 7
# circle_properties()

# problem 8
# arithmetic_mean()

# problem 9
# geometric_mean()

# problem 10
# sum_product_square()

# problem 11
# sum_difference_abs()

# problem 12
# right_triangle_properties()

# problem 13
# concentric_circle_areas()

# problem 14
# circle_by_length()

# problem 15
# circle_by_area()

# problem 16
# distance_between_points()

# problem 17
# segment_lengths()

# problem 19
# rectangle_properties()

# problem 20
# distance_2d()

# problem 21
# triangle_area()

# problem 22 23 24
# swap_values()

# problem 25
# evaluate_cubic()

# problem 26
# evaluate_quartic()

# problem 27
# power_of_number()

# problem 28
# specific_powers()

# problem 29
# degrees_to_radians()

# problem 30
# radians_to_degrees()

# problem 31
# fahrenheit_to_celsius()

# problem 32
# celsius_to_fahrenheit()

# problem 33
# total_candy_cost()

# problem 34
# chocolate_cost()

# problem 35
# boat_distance()

# problem 36
# cars_distance_same_direction()

# problem 37
# cars_distance_opposite_direction()

# problem 38
# solve_linear_equation()

# problem 39
# solve_quadratic()

# problem 40
# solve_system()