from CQs.cq03.point import Point

my_point = Point(5.0, 2.0)
print(f"Initial Point: ({my_point.x}, {my_point.y})")

scaled_point = my_point.scale(2)

print(f"Original point is still: ({my_point.x}, {my_point.y})")
print(f"New scaled point is: ({scaled_point.x}, {scaled_point.y})")

my_point.scale_by(2)

print(f"Original point has now changed to: ({my_point.x}, {my_point.y})")
