from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, start, destination):
        pass


class CarRouteStrategy(RouteStrategy):
    def build_route(self, start, destination):
        return f"Constructed a car route from {start} to {destination}"


class WalkingRouteStrategy(RouteStrategy):
    def build_route(self, start, destination):
        return f"Constructed a walking route from {start} to {destination}"


class Navigator:
    def __init__(self, route_strategy):
        self.route_strategy = route_strategy

    def set_route_strategy(self, route_strategy):
        self.route_strategy = route_strategy

    def build_route(self, start, destination):
        return self.route_strategy.build_route(start, destination)


if __name__ == "__main__":
    car_rout = CarRouteStrategy()
    walk_rout = WalkingRouteStrategy()

    nav = Navigator(car_rout)
    rt = nav.build_route("Home", "Work")
    print(rt)

    nav2 = Navigator(walk_rout)
    rt2 = nav2.build_route("Park", "Home")
    print(rt2)
