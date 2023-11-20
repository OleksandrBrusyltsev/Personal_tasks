from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        return "Auto Deliver"


class Ship(Transport):
    def deliver(self):
        return "Ship Deliver"


class LogisticCompany(ABC):
    def create_transport(self, ) -> Transport:
        pass


class CarTransportation(LogisticCompany):
    def create_transport(self, ) -> Transport:
        return Truck()


class ShipTransportation(LogisticCompany):
    def create_transport(self, ) -> Transport:
        return Ship()


def car_transportation_process(logistic_company: LogisticCompany):
    transport = logistic_company.create_transport()
    return transport.deliver()


def ship_transportation_process(logistic_company: LogisticCompany):
    transport = logistic_company.create_transport()
    return transport.deliver()


if __name__ == "__main__":
    car_transporter = CarTransportation()
    car_transport = car_transporter.create_transport()
    print(car_transport.deliver())

    print(ship_transportation_process(car_transporter))

    ship_transporter = ShipTransportation()
    ship_transport = ship_transporter.create_transport()
    print(ship_transport.deliver())
