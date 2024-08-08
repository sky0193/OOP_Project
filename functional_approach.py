def calculate_area(shape):
    
    if shape['type'] == 'rectangle':
        length = shape['length']
        width = shape['width']
        area = length * width
        return area
    
    elif shape['type'] == 'triangle':
        base = shape['base']
        height = shape['height']
        area = 0.5 * base * height
        return area
        
    elif shape['type'] == 'square':
        side = shape['side']
        area = side ** 2
        return area
    elif shape['type'] == 'trapezoid':
        base1 = shape['base1']
        base2 = shape['base2']
        height = shape['height']
        area = 0.5 * (base1 + base2) * height
        return area
    
    elif shape['type'] == 'parallelogram':
        base = shape['base']
        height = shape['height']
        area = base * height
        return area
    else:
        raise ValueError("Unknown shape value")
    
rectangle = {'type': 'rectangle', 'length': 4, 'width': 3}
triangle = {'type': 'triangle', 'base': 6, 'height': 3}
square = {'type': 'square', 'side': 4}
trapezoid = {'type': 'trapezoid', 'base1': 3, 'base2': 5, 'height': 2}
parallelogram = {'type': 'parallelogram', 'base': 4, 'height': 3}


print(f"The area of the triangle is {calculate_area(triangle)}")     
print(f"The area of the rectangle is {calculate_area(rectangle)}")    
print(f"The area of the square is {calculate_area(square)}")     
print(f"The area of the trapezoid is {calculate_area(trapezoid)}")     
print(f"The area of the parallelogram is {calculate_area(parallelogram)}")     