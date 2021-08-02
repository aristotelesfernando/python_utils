class Retangle:
    def __init__(self, length, width = 0):
        self.length = length
        if width > 0:
            self.width = width
        else:
            self.width = length

    def area(self):
        return self.length * self.width

class Square(Retangle):
    pass
    
