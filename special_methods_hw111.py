class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors += floors
        print(self.numberOfFloors)


h1 = House()
print(h1.numberOfFloors)
h1.setNewNumberOfFloors(1111)
