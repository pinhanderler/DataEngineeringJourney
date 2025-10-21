class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


class SUV(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

    def display_info(self):
        super().display_info()
        print("4WD:", "Yes" if self.four_wheel_drive else "No")


class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f"Max Speed: {self.max_speed} km/h")


if __name__ == "__main__":
    suv = SUV("Toyota", "Land Cruiser", 2022, True)
    sportscar = SportsCar("Ferrari", "F8", 2023, 340)

    suv.display_info()
    print()
    sportscar.display_info()
