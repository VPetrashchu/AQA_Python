class Hause():
    
    def __init__(self, wall, lacation, plane):
        self.wall = wall
        self.lacation = lacation
        self.plane = plane
    
class Building(Hause):
    
    def __init__(self, floor, wall, lacation, plane):
        super.__init__(self, wall, lacation, plane)
        self.floor = floor
        

class Cottage(Hause):
    def __init__(self, length, width, depth, wall, lacation, plane):
        super.__init__(self, wall, lacation, plane)
        
        self.pool = Pool(length, width, depth)

class Pool(): 
    
    def __init__(self, length, width, depth):
        self.length = length
        self.width = width
        self.depth = depth

