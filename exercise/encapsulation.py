import math

class Square:
    def __init__(self, length_of_side: float):
        self._side = length_of_side
        self._update_properties()

    # --- internal helper ---
    def _update_properties(self):
        self._perimeter = 4 * self._side
        self._area = self._side ** 2
        self._diagonal = self._side * math.sqrt(2)

    # --- getters ---
    def get_side(self):
        return self._side
    
    def get_perimeter(self):
        return self._perimeter
    
    def get_area(self):
        return self._area
    
    def get_diagonal(self):
        return self._diagonal
    
    # --- setters ---
    def set_side(self, new_length: float):
        self._side = new_length
        self._update_propertpies()

    def set_perimeter(self, new_perimeter: float):
        self._perimeter = new_perimeter / 4
        self._update_properties()

    def set_area(self, new_area: float):
        self._area = math.sqrt(new_area)
        self._update_properties()

    def set_diagonal(self, new_diagonal: float):
        self._diagonal = new_diagonal / math.sqrt(2)
        self._update_properties()




sq = Square(4)

print(sq.get_side())
print(sq.get_perimeter())
print(sq.get_area())
print(sq.get_diagonal())


sq.set_side(32)
print(sq.get_side())
print(sq.get_perimeter())
print(sq.get_area())
print(sq.get_diagonal())