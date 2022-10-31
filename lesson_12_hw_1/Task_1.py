import random


class Vehicle:
    def __init__(self, speed, gas_capacity, power):
        self.speed = speed
        self.gas_capacity = gas_capacity
        self.power = power

    def calculate_distance(self):
        return self.gas_capacity / self.power * 100


class Train(Vehicle):
    def __init__(self, speed, gas_capacity, power, count_of_stations):
        super().__init__(speed, gas_capacity, power)
        self.count_of_stations = count_of_stations

    def average_station_distance(self):
        return self.calculate_distance() / self.count_of_stations


class Plane(Vehicle):
    def __init__(self, speed, gas_capacity, power, height_of_plane):
        super().__init__(speed, gas_capacity, power)
        self.height_of_plane = height_of_plane

    def calculate_flight_distance(self):
        if self.height_of_plane > 10000 and self.power < 5:
            return 0
        else:
            if self.power > 10:
                return self.calculate_distance() * 0.8
            else:
                return self.calculate_distance() * 0.4


class Bus(Vehicle):
    def __init__(self, speed, gas_capacity, power, isCityBus: bool):
        super().__init__(speed, gas_capacity, power)
        self.isCityBus = isCityBus

    def ticket_price(self):
        if self.calculate_distance() > 100 and self.isCityBus:
            return self.calculate_distance() / 10
        elif self.calculate_distance() > 100 and self.isCityBus is not True:
            return self.calculate_distance() / 5
        else:
            return 12


def main():
    vehicle_object = Vehicle(random.randint(1, 101), random.randint(1, 101), random.randint(1, 101))
    print('Максимальная дистанция (км):', vehicle_object.calculate_distance())

    train_object = Train(random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), random.randint(1, 101))
    print('Расстояние между станциями(км):', train_object.average_station_distance())

    plain_object = Plane(random.randint(1, 101), random.randint(1, 101), random.randint(1, 101),
                         random.randint(1, 12000))
    print('Максимальная дальность полета самолета на высоте', plain_object.height_of_plane, '=',
          plain_object.calculate_flight_distance())

    bus_object = Bus(random.randint(1, 101), random.randint(1, 101), random.randint(1, 101), False)
    print('Стоимость проезда состовляет:', bus_object.ticket_price())


if __name__ == '__main__':
    main()
