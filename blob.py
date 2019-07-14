class Blob:

    def __init__(self): 

        self._mass = 0  
        self._x = 0.0
        self._y = 0.0  

    def add(self, i, j):
    
        self._x = (self._x * self._mass + i) / (self._mass + 1)
        self._y = (self._y * self._mass + j) / (self._mass + 1)

        self._mass += 1

    def mass(self):

        return self._mass

    def distanceTo(self, other):

        x1 = self._x
        y1 = self._y
        x2 = other._x
        y2 = other._y

        dx = (x1 - x2) ** 2
        dy = (y1 - y2) ** 2
        d = (dx + dy) ** 0.5

        return d

    def __str__(self):
        
        return '%d (%.4f, %.4f)' % (self._mass, self._x, self._y)