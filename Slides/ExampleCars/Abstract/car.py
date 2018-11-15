import vehicle


class Car(vehicle.Vehicle):
    def __int__(self, id, colour, base_bill, wheels):
        super().__init__(id, colour, base_bill)
        self.wheels = wheels

    def beep(self):
        print("BEEEEEPPPPP")


car = Car(22, "Blue", 200)
print(car._colour)
