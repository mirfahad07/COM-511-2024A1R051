#write a python program to store two points as tuples and calculate the distance between them
point1 = (2, 3)
point2 = (6, 6)

x1, y1 = point1
x2, y2 = point2

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Distance between the points:", distance)
