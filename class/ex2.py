class Hause():
    
    def __init__(self, wall, lacation, squaled, plane):
        self.wall = wall
        self.lacation = lacation
        self.squaled = squaled
        self.plane = plane

class Pool(Hause):
    
class Building(Hause):
    
    def __init__(self, floor):
        self.floor = floor

class Cottage(Hause):
    def __init__(self, length, width, depth):
        super.__init__(self, length, width, depth)
        self.pool = Pool(self.length, self.width, self.depth)
