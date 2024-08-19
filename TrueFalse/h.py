class Car:

    def __init__(self, seat):
        self.seats = seat


    def enter_race_mode(self):
        self.seats = 2

car = Car(5)
print(car.seats)

car.enter_race_mode()
print(car.seats)

