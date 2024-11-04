import math

# Task 1
def task1_square_perimeter():
    a = float(input("Enter side length of the square: "))
    print("Perimeter of the square:", 4 * a)

# Task 2
def task2_square_area():
    a = float(input("Enter side length of the square: "))
    print("Area of the square:", a ** 2)

# Task 3
def task3_rectangle_area_perimeter():
    a = float(input("Enter side 'a' of the rectangle: "))
    b = float(input("Enter side 'b' of the rectangle: "))
    area = a * b
    perimeter = 2 * (a + b)
    print("Area of the rectangle:", area)
    print("Perimeter of the rectangle:", perimeter)

# Task 4
def task4_circle_circumference():
    d = float(input("Enter the diameter of the circle: "))
    print("Circumference of the circle:", math.pi * d)

# Task 5
def task5_cube_volume_surface_area():
    a = float(input("Enter side length of the cube: "))
    volume = a ** 3
    surface_area = 6 * (a ** 2)
    print("Volume of the cube:", volume)
    print("Surface area of the cube:", surface_area)

# Task 6
def task6_parallelepiped_volume_surface_area():
    a = float(input("Enter side 'a' of the parallelepiped: "))
    b = float(input("Enter side 'b' of the parallelepiped: "))
    c = float(input("Enter side 'c' of the parallelepiped: "))
    volume = a * b * c
    surface_area = 2 * (a * b + b * c + c * a)
    print("Volume of the parallelepiped:", volume)
    print("Surface area of the parallelepiped:", surface_area)

# Task 7
def task7_circle_properties():
    R = float(input("Enter radius of the circle: "))
    circumference = 2 * math.pi * R
    area = math.pi * (R ** 2)
    print("Circumference of the circle:", circumference)
    print("Area of the circle:", area)

# Task 8
def task8_average_of_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Average:", (a + b) / 2)

# Task 9
def task9_geometric_mean_of_two_numbers():
    a = float(input("Enter first positive number: "))
    b = float(input("Enter second positive number: "))
    print("Geometric mean:", math.sqrt(a * b))

# Task 10
def task10_sum_index_and_square_of_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum:", a + b)
    print("Index:", abs(a - b))
    print("Square of each:", a ** 2, b ** 2)

# Task 11
def task11_absolute_value_and_square_of_two_numbers():
    a = float(input("Enter first number (non-zero): "))
    b = float(input("Enter second number (non-zero): "))
    print("Absolute value:", abs(a), abs(b))
    print("Square of each:", a ** 2, b ** 2)

# Task 12
def task12_triangle_hypotenuse_and_perimeter():
    a = float(input("Enter side 'a' of the triangle: "))
    b = float(input("Enter side 'b' of the triangle: "))
    c = math.sqrt(a ** 2 + b ** 2)
    perimeter = a + b + c
    print("Hypotenuse:", c)
    print("Perimeter:", perimeter)

# Task 13
def task13_circle_area_difference():
    R1 = float(input("Enter radius R1: "))
    R2 = float(input("Enter radius R2 (smaller than R1): "))
    area1 = math.pi * (R1 ** 2)
    area2 = math.pi * (R2 ** 2)
    print("Difference in area:", area1 - area2)

# Task 14
def task14_circle_length_and_area():
    L = float(input("Enter circumference: "))
    radius = L / (2 * math.pi)
    area = math.pi * (radius ** 2)
    print("Radius:", radius)
    print("Area:", area)

# Task 15
def task15_circle_radius_from_area():
    S = float(input("Enter area of the circle: "))
    radius = math.sqrt(S / math.pi)
    print("Radius:", radius)

# Task 16
def task16_distance_between_points():
    x1, y1 = map(float, input("Enter coordinates of first point (x1, y1): ").split())
    x2, y2 = map(float, input("Enter coordinates of second point (x2, y2): ").split())
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("Distance:", distance)

# Task 17
def task17_triangle_area_perimeter():
    x1, y1 = map(float, input("Enter coordinates of first vertex (x1, y1): ").split())
    x2, y2 = map(float, input("Enter coordinates of second vertex (x2, y2): ").split())
    x3, y3 = map(float, input("Enter coordinates of third vertex (x3, y3): ").split())
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Perimeter:", perimeter)
    print("Area:", area)

# Task 18
def task18_swap_values():
    A = float(input("Enter value of A: "))
    B = float(input("Enter value of B: "))
    A, B = B, A
    print("Swapped values - A:", A, "B:", B)

# Task 19
def task19_y_value_for_function():
    x = float(input("Enter x: "))
    print("y = 3*x^5 - 6*x^2 - 7:", 3 * (x ** 5) - 6 * (x ** 2) - 7)

# Task 20
def task20_linear_equation_solution():
    A = float(input("Enter coefficient A: "))
    B = float(input("Enter coefficient B: "))
    if A != 0:
        x = -B / A
        print("Solution x:", x)
    else:
        print("No solution (A cannot be zero)")

# Task 21
def task21_arithmetic_mean():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Arithmetic mean:", (x + y) / 2)

# Task 22
def task22_geometric_mean():
    x = float(input("Enter first positive number: "))
    y = float(input("Enter second positive number: "))
    if x > 0 and y > 0:
        print("Geometric mean:", math.sqrt(x * y))
    else:
        print("Both numbers must be positive.")

# Task 23
def task23_circle_area_difference():
    R1 = float(input("Enter the larger radius R1: "))
    R2 = float(input("Enter the smaller radius R2: "))
    if R1 > R2:
        area_difference = math.pi * (R1 ** 2 - R2 ** 2)
        print("Area difference:", area_difference)
    else:
        print("R1 must be greater than R2.")

# Task 24
def task24_rectangle_diagonal():
    a = float(input("Enter side 'a' of the rectangle: "))
    b = float(input("Enter side 'b' of the rectangle: "))
    diagonal = math.sqrt(a ** 2 + b ** 2)
    print("Diagonal:", diagonal)

# Task 25
def task25_cube_diagonal():
    a = float(input("Enter side length of the cube: "))
    diagonal = a * math.sqrt(3)
    print("Diagonal of the cube:", diagonal)

# Task 26
def task26_parallelepiped_diagonal():
    a = float(input("Enter side 'a' of the parallelepiped: "))
    b = float(input("Enter side 'b' of the parallelepiped: "))
    c = float(input("Enter side 'c' of the parallelepiped: "))
    diagonal = math.sqrt(a ** 2 + b ** 2 + c ** 2)
    print("Diagonal of the parallelepiped:", diagonal)

# Task 27
def task27_fahrenheit_to_celsius():
    F = float(input("Enter temperature in Fahrenheit: "))
    C = (F - 32) * 5 / 9
    print("Temperature in Celsius:", C)

# Task 28
def task28_celsius_to_fahrenheit():
    C = float(input("Enter temperature in Celsius: "))
    F = C * 9 / 5 + 32
    print("Temperature in Fahrenheit:", F)

# Task 29
def task29_quadratic_equation_discriminant():
    a = float(input("Enter coefficient 'a': "))
    b = float(input("Enter coefficient 'b': "))
    c = float(input("Enter coefficient 'c': "))
    discriminant = b ** 2 - 4 * a * c
    print("Discriminant:", discriminant)

# Task 30
def task30_quadratic_roots():
    a = float(input("Enter coefficient 'a' (non-zero): "))
    b = float(input("Enter coefficient 'b': "))
    c = float(input("Enter coefficient 'c': "))
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Roots are real and different:", root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Roots are real and same:", root)
    else:
        print("No real roots.")

# Task 31
def task31_factorial():
    n = int(input("Enter a non-negative integer: "))
    if n >= 0:
        factorial = math.factorial(n)
        print("Factorial:", factorial)
    else:
        print("Number should be non-negative.")

# Task 32
def task32_degrees_to_radians():
    degrees = float(input("Enter angle in degrees: "))
    radians = math.radians(degrees)
    print("Angle in radians:", radians)

# Task 33
def task33_radians_to_degrees():
    radians = float(input("Enter angle in radians: "))
    degrees = math.degrees(radians)
    print("Angle in degrees:", degrees)

# Task 34
def task34_permutation():
    n = int(input("Enter total items (n): "))
    r = int(input("Enter items to arrange (r): "))
    if 0 <= r <= n:
        permutation = math.factorial(n) // math.factorial(n - r)
        print("Permutation (nPr):", permutation)
    else:
        print("Invalid values. Ensure that 0 <= r <= n.")

# Task 35
def task35_combination():
    n = int(input("Enter total items (n): "))
    r = int(input("Enter items to choose (r): "))
    if 0 <= r <= n:
        combination = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        print("Combination (nCr):", combination)
    else:
        print("Invalid values. Ensure that 0 <= r <= n.")

# Task 36
def task36_power():
    x = float(input("Enter base number: "))
    n = int(input("Enter exponent (integer): "))
    print("Result:", x ** n)

# Task 37
def task37_sum_of_integers():
    n = int(input("Enter a positive integer: "))
    if n > 0:
        total_sum = sum(range(1, n + 1))
        print("Sum of integers from 1 to n:", total_sum)
    else:
        print("Number should be positive.")

# Task 38
def task38_product_of_integers():
    n = int(input("Enter a positive integer: "))
    if n > 0:
        product = math.prod(range(1, n + 1))
        print(f"Product of integers from 1 to {n}:", product)
    else:
        print("Number should be positive.")

# Task 39
def task39_average_of_integers():
    n = int(input("Enter a positive integer: "))
    if n > 0:
        total_sum = sum(range(1, n + 1))
        average = total_sum / n
        print("Average of integers from 1 to n:", average)
    else:
        print("Number should be positive.")

# Task 40
def task40_sum_of_squares():
    n = int(input("Enter a positive integer: "))
    if n > 0:
        sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
        print("Sum of squares from 1 to n:", sum_of_squares)
    else:
        print("Number should be positive.")





# task1_square_perimeter()
# task2_square_area()
# task3_rectangle_area_perimeter()
# task4_circle_circumference()
# task5_cube_volume_surface_area()
# task6_parallelepiped_volume_surface_area()
# task7_circle_properties()
# task8_average_of_two_numbers()
# task9_geometric_mean_of_two_numbers()
# task10_sum_index_and_square_of_two_numbers()
# task11_absolute_value_and_square_of_two_numbers()
# task12_triangle_hypotenuse_and_perimeter()
# task13_circle_area_difference()
# task14_circle_length_and_area()
# task15_circle_radius_from_area()
# task16_distance_between_points()
# task17_triangle_area_perimeter()
# task18_swap_values()
# task19_y_value_for_function()
# task20_linear_equation_solution()
# task21_arithmetic_mean()
# task22_geometric_mean()
# task23_circle_area_difference()
# task24_rectangle_diagonal()
# task25_cube_diagonal()
# task26_parallelepiped_diagonal()
# task27_fahrenheit_to_celsius()
# task28_celsius_to_fahrenheit()
# task29_quadratic_equation_discriminant()
# task30_quadratic_roots()
# task31_factorial()
# task32_degrees_to_radians()
# task33_radians_to_degrees()
# task34_permutation()
# task35_combination()
# task36_power()
# task37_sum_of_integers()
# task38_product_of_integers()
# task39_average_of_integers()
# task40_sum_of_squares()

