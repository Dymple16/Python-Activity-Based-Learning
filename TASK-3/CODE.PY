def calculate_plan_cost(plan, usage):
    """Return excess amounts, total cost, and eligibility for a plan."""
    excess_data = max(0, usage["data"] - plan["data"])
    excess_calls = max(0, usage["calls"] - plan["calls"])
    excess_sms = max(0, usage["sms"] - plan["sms"])

    total_cost = (
        plan["price"]
        + excess_data * plan["data_rate"]
        + excess_calls * plan["call_rate"]
        + excess_sms * plan["sms_rate"]
    )

    eligible = (
        plan["validity"] >= usage["validity"]
        and total_cost <= usage["budget"]
    )

    return {
        "excess_data": excess_data,
        "excess_calls": excess_calls,
        "excess_sms": excess_sms,
        "total_cost": total_cost,
        "eligible": eligible,
    }


def main():
    print("Multi-Plan Telecommunications Cost Optimization")

    usage = {
        "data": float(input("Required data (GB): ")),
        "calls": int(input("Required call minutes: ")),
        "sms": int(input("Required SMS count: ")),
        "validity": int(input("Required validity (days): ")),
        "budget": float(input("Budget (₹): ")),
    }

    plan_count = int(input("Number of plans to compare: "))
    if plan_count <= 0:
        print("Enter at least one plan.")
        return

    plans = []

    for index in range(plan_count):
        print(f"\nPlan {index + 1}")
        plan = {
            "name": input("Plan name: ").strip(),
            "data": float(input("Included data (GB): ")),
            "calls": int(input("Included call minutes: ")),
            "sms": int(input("Included SMS count: ")),
            "price": float(input("Base price (₹): ")),
            "validity": int(input("Validity (days): ")),
            "data_rate": float(input("Charge per excess GB (₹): ")),
            "call_rate": float(input("Charge per excess call minute (₹): ")),
            "sms_rate": float(input("Charge per excess SMS (₹): ")),
        }
        plans.append(plan)

    results = []
    for plan in plans:
        result = calculate_plan_cost(plan, usage)
        results.append((plan, result))

    print("\nPlan Comparison")
    for plan, result in results:
        status = "Eligible" if result["eligible"] else "Not eligible"
        print(
            f"{plan['name']}: total ₹{result['total_cost']:.2f} | "
            f"Excess: {result['excess_data']:.2f} GB data, "
            f"{result['excess_calls']} call minutes, "
            f"{result['excess_sms']} SMS | {status}"
        )

    eligible_plans = [
        (plan, result)
        for plan, result in results
        if result["eligible"]
    ]

    if eligible_plans:
        best_plan, best_result = min(
            eligible_plans,
            key=lambda item: (item[1]["total_cost"], item[0]["name"].casefold()),
        )
        print(
            f"\nMost economical eligible plan: {best_plan['name']} "
            f"(₹{best_result['total_cost']:.2f})"
        )
    else:
        print("\nNo plan meets both the validity and budget requirements.")


if __name__ == "__main__":
    main()
