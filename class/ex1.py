class Brick():
    
    def __init__(self, width, legth, height, color):      
        self.width = width
        self.legth = legth
        self.height = height
        self.color = color
    
    def display(self):
        print(f"Values of brick {self.width}, {self.legth}, {self.height} and {self.color}, all are good look")
    
b1 = Brick(10, 15, 30, 'red')
b2 = Brick(11, 16, 31, 'blue')
b3 = Brick(12, 17, 32, 'white')
b4 = Brick(13, 18, 33, 'black')

l = [b1, b2, b3, b4]

for i in l: #'i' is element of the list not addinal counter
    i.display()

for i in range(len(l)): 
    l[i].display()
    
#enumarate
for i, el in enumerate(l):
    print(i)
    el.display()

