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
    else:
        raise ValueError("Unknown shape value")
    
rectangle = {'type': 'rectangle', 'length': 4, 'width': 3}
triangle = {'type': 'triangle', 'base': 6, 'height': 3}

print(f"The area of the rectangle is {calculate_area(rectangle)}")    
print(f"The area of the triangle is {calculate_area(triangle)}")     