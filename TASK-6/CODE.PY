def main():
    print("Multi-Day Water Tank Simulation")

    capacity = float(input("Tank capacity (litres): "))
    initial_level = float(input("Initial water level (litres): "))
    threshold = float(input("Target threshold (litres): "))
    days = int(input("Number of days: "))

    if capacity <= 0:
        print("Error: Tank capacity must be greater than zero.")
        return
    if not 0 <= initial_level <= capacity:
        print("Error: Initial level must be between zero and capacity.")
        return
    if not 0 <= threshold <= capacity:
        print("Error: Threshold must be between zero and capacity.")
        return
    if days <= 0:
        print("Error: Number of days must be greater than zero.")
        return

    schedule = []
    for day in range(1, days + 1):
        print(f"\nDay {day}")
        inflow = float(input("Inflow (litres): "))
        outflow = float(input("Outflow (litres): "))

        if inflow < 0 or outflow < 0:
            print("Error: Inflow and outflow cannot be negative.")
            return

        schedule.append((inflow, outflow))

    level = initial_level
    first_threshold_day = 0 if level >= threshold else None
    results = []

    for day, (inflow, outflow) in enumerate(schedule, start=1):
        shortage = outflow > level
        level = max(0, level - outflow)

        level += inflow
        overflow = level > capacity
        if overflow:
            level = capacity

        if first_threshold_day is None and level >= threshold:
            first_threshold_day = day

        results.append((day, inflow, outflow, level, shortage, overflow))

    print("\nDaily Simulation Results")
    print("Day | Inflow | Outflow | Final Level | Status")
    print("-" * 58)

    for day, inflow, outflow, final_level, shortage, overflow in results:
        statuses = []
        if shortage:
            statuses.append("SHORTAGE")
        if overflow:
            statuses.append("OVERFLOW")
        status = ", ".join(statuses) if statuses else "Normal"

        print(
            f"{day:>3} | {inflow:>6.1f} | {outflow:>7.1f} | "
            f"{final_level:>11.1f} | {status}"
        )

    if first_threshold_day is None:
        print(f"\nThe tank did not reach the threshold of {threshold:.1f} litres.")
    elif first_threshold_day == 0:
        print(
            f"\nThe tank was already at or above the threshold "
            f"({threshold:.1f} litres) at the start."
        )
    else:
        print(
            f"\nThe tank first reached the threshold of {threshold:.1f} litres "
            f"on Day {first_threshold_day}."
        )


if __name__ == "__main__":
    main()
