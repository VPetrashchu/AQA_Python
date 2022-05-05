class Hause():
    
    def __init__(self, wall, lacation, plane):
        self.wall = wall
        self.lacation = lacation
        self.plane = plane
    
    def display(self):
        print(f"Hause has {self.wall}, {self.lacation}, {self.plane}\n")
    
class Building(Hause):
    
    def __init__(self, floor, wall, lacation, plane):
        super().__init__(wall, lacation, plane)
        self.floor = floor
        
    def display(self):
        super().display()
        print(f"floor: {self.floor}")


class Pool(): 
    
    def __init__(self, length, width, depth):
        self.length = length
        self.width = width
        self.depth = depth        
        
    def display(self):
        print(f"length {self.length}, width: {self.width}, depth: {self.depth}")


class Cottage(Hause):
    def __init__(self, length, width, depth, wall, lacation, plane):
        super().__init__(wall, lacation, plane)
        
        self.pool = Pool(length, width, depth)
        
    def display(self):
        super().display()
        
        self.pool.display()



h1 = Hause("wall", "location", "plane")
h1.display()

b1 = Building("floor-b", "wall-b", "locatoin-b", "plane-b")
b1.display()

c1 = Cottage("len-c", "width-c", "depth-c", "wall-c", "location-c", "plane-c")
c1.display()