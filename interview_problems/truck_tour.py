from collections import deque


def truck_tour(petrolpumps: list[list[int]]) -> int:
    queue = deque()

    position = fuel = distance = 0

    for pump in range(len(petrolpumps)):
        pump_fuel, pump_distance = petrolpumps[pump]
        queue.append(petrolpumps[pump])
        fuel += pump_fuel
        distance += pump_distance
        while fuel < distance:
            station = queue.popleft()
            station_fuel, station_distance = station
            fuel -= station_fuel
            distance -= station_distance
            position += 1

    pump = 0
    while pump < position:
        pump_fuel, pump_distance = petrolpumps[pump]
        queue.append(petrolpumps[pump])
        fuel += pump_fuel
        distance += pump_distance
        while fuel < distance:
            station = queue.popleft()
            station_fuel, station_distance = station
            fuel -= station_fuel
            distance -= station_distance
            position += 1

        pump += 1

    return position
