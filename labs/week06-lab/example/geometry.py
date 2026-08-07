def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area_rectangle = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area_rectangle}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)


def calculate_triangle_area(height, base):
    """Calculates and displays triangle area"""
    area_triangle = 0.5 * height * base
    print(f"Triangle with height {height} and base {base}")
    print(f"Area = 0.5 × {height} × {base} = {area_triangle}")
    print()

print("Calculating Triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)
