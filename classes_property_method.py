# getters and setters - instance methods that get/set attribute properties on an object, a getter reads a value and a setter overwrites a value

# example
class Height():
    def __init__(self, feet):
        self._inches = feet * 12
        
    def _get_feet(self):
        return self._inches / 12
    
    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12
            
    feet = property(_get_feet, _set_feet)

height = Height(5)
print(height.feet)
height.feet = 6
print(height.feet)
height.feet = -10
print(height.feet)

