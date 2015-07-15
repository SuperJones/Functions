class Point:
 
    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY
 
    def getX(self):
        return self.x
 
    def getY(self):
        return self.y
 
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
 
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
 
    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

    def slope_from_origin(self):
        #slope equals rise over run
        #y2-y1 over x2-x2
        # if the orgin is zero then there will be an issue. because
        # a number divided by 0 is an error.
        
        if self.x == 0:
            return none 
        else:
            return (self.y - 0) / (self.x -0 )
       
p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)
 
print(mid)
print(mid.getX())
print(mid.getY())
print(p.slope_from_origin())

