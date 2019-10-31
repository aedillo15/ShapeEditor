class Shape:
    #Constructor for Shape
    def __init__(self):
        self._color = 'black'
        self._location = 0.0
        self._isFilled = False
    #Acessor for color
    def getColor(self):
        return self._color
    #Mutator for color
    def setColor(self, color):
        self._color = color
    #Accessor for location
    def getLocation(self):
        return self._location
    #Mutator for location
    def setLocation(self, location):
        self._location = location
    #Accessor for isFilled
    def getIsFilled(self):
        return self._isFilled
    #Mutator for isFilled
    def setIsFilled(self, isFilled):
        self._isFilled = isFilled

