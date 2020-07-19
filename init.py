# initiate the class
class Point:
    'Represent a point in two-dimensional geometric corridinates'

    def __init__(self, x=0, y=0): # default arguments value
        '''Initialize the position of a new point. The x and y coordinates can be specified. If they are 
        are not, the point defaults to the origin'''
        self.move(x, y)

    def move(self, x, y):
        "Move the Point to a new location in 2D space"
        self.x = x
        self.y = y

    def reset(self):
        'Reset the point back to the geometric origin: 0, 0'
        self.move(0, 0)

# Constructing a Point
point = Point(3)
print(point.x, point.y)
