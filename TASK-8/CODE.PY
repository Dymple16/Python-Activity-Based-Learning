def main():
    print("Bus Passenger Occupancy Simulation")

    capacity = int(input("Bus capacity: "))
    passengers = int(input("Passengers on bus before first stop: "))
    stop_count = int(input("Number of stops: "))

    if capacity <= 0:
        print("Error: Capacity must be greater than zero.")
        return
    if passengers < 0 or passengers > capacity:
        print("Error: Starting passengers must be between 0 and capacity.")
        return
    if stop_count <= 0:
        print("Error: Number of stops must be greater than zero.")
        return

    results = []

    for stop in range(1, stop_count + 1):
        print(f"\nStop {stop}")
        alighting = int(input("Passengers alighting: "))
        boarding = int(input("Passengers boarding: "))

        if alighting < 0 or boarding < 0:
            print("Error: Boarding and alighting counts cannot be negative.")
            return

        if alighting > passengers:
            print(
                f"Error: Only {passengers} passengers are on the bus; "
                f"{alighting} cannot alight."
            )
            return

        passengers -= alighting
        passengers += boarding

        status = "CAPACITY VIOLATION" if passengers > capacity else "Within capacity"
        results.append((stop, alighting, boarding, passengers, status))

    print("\nOccupancy by Stop")
    print("Stop | Alighted | Boarded | Passengers | Status")
    print("-" * 62)

    for stop, alighting, boarding, count, status in results:
        print(
            f"{stop:>4} | {alighting:>8} | {boarding:>7} | "
            f"{count:>10} | {status}"
        )


if __name__ == "__main__":
    main()
