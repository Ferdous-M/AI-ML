class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

my_car = Car("Toyota", "Black")

print(my_car.brand)
my_car.start()