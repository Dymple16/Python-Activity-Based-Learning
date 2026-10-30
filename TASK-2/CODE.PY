def main():
    print("Manufacturing Cost and Profitability Analysis")

    units = int(input("Number of units to produce: "))
    material_per_unit = float(input("Material cost per unit: ₹"))
    wastage_percentage = float(input("Material wastage percentage: "))
    labour_per_unit = float(input("Labour cost per unit: ₹"))
    machine_cost = float(input("Total machine cost: ₹"))
    selling_price_per_unit = float(input("Selling price per unit: ₹"))
    profit_target = float(input("Required profit target (%): "))

    if units <= 0:
        print("Error: Number of units must be greater than zero.")
        return

    if min(
        material_per_unit,
        wastage_percentage,
        labour_per_unit,
        machine_cost,
        selling_price_per_unit,
        profit_target,
    ) < 0:
        print("Error: Costs, percentages, and selling price cannot be negative.")
        return

    base_material_cost = units * material_per_unit
    wastage_cost = base_material_cost * wastage_percentage / 100
    total_material_cost = base_material_cost + wastage_cost
    total_labour_cost = units * labour_per_unit
    total_production_cost = (
        total_material_cost + total_labour_cost + machine_cost
    )
    total_sales_revenue = units * selling_price_per_unit
    profit = total_sales_revenue - total_production_cost

    if total_production_cost == 0:
        profit_percentage = 0.0 if profit == 0 else float("inf")
    else:
        profit_percentage = profit / total_production_cost * 100

    print("\nCost and Profit Report")
    print(f"Base material cost:    ₹{base_material_cost:,.2f}")
    print(f"Wastage cost:          ₹{wastage_cost:,.2f}")
    print(f"Total material cost:   ₹{total_material_cost:,.2f}")
    print(f"Total labour cost:     ₹{total_labour_cost:,.2f}")
    print(f"Machine cost:          ₹{machine_cost:,.2f}")
    print(f"Total production cost: ₹{total_production_cost:,.2f}")
    print(f"Total sales revenue:   ₹{total_sales_revenue:,.2f}")
    print(f"Profit:                ₹{profit:,.2f}")

    if profit_percentage == float("inf"):
        print("Profit percentage:     Not defined (zero production cost)")
    else:
        print(f"Profit percentage:     {profit_percentage:.2f}%")

    if profit_percentage >= profit_target:
        print(f"Result: Profit target of {profit_target:.2f}% met.")
    else:
        print(f"Result: Profit target of {profit_target:.2f}% not met.")


if __name__ == "__main__":
    main()
