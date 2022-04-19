class StaticTest:
    x = 1

t1 = StaticTest()
print(f'via instance:{t1.x}')
print(f'via class:{StaticTest.x}')

t1.x = 2
print(f'via instance:{t1.x}')
print(f'via class:{StaticTest.x}')

StaticTest.x = 3
print(f'via instance:{t1.x}')
print(f'via class:{StaticTest.x}')

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
        
    def display(self):
        return f"{self.month} - {self.day} - {self.year}"
    
    @classmethod #decorator
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)
    
    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)
    
d1 = Date.millenium_c(6, 9)
d2 = Date.millenium_s(6, 9)
    
print(d1.display())
print(d2.display())