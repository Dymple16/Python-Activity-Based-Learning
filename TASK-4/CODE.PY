import math


def main():
    print("Campus Event Financial Planning")

    participants = int(input("Expected number of participants: "))
    contribution = float(input("Contribution per participant (₹): "))

    venue = float(input("Venue cost (₹): "))
    equipment = float(input("Equipment cost (₹): "))
    catering = float(input("Catering cost (₹): "))
    transport = float(input("Transport cost (₹): "))
    certificates = float(input("Certificate cost (₹): "))
    sponsorship = float(input("Sponsorship amount (₹): "))

    values = [
        participants,
        contribution,
        venue,
        equipment,
        catering,
        transport,
        certificates,
        sponsorship,
    ]

    if any(value < 0 for value in values):
        print("Error: Inputs cannot be negative.")
        return

    total_cost = venue + equipment + catering + transport + certificates
    participant_revenue = participants * contribution
    total_funds = sponsorship + participant_revenue
    shortfall = max(0, total_cost - total_funds)
    surplus = max(0, total_funds - total_cost)

    remaining_after_sponsorship = max(0, total_cost - sponsorship)

    if remaining_after_sponsorship == 0:
        break_even_registrations = 0
        break_even_message = "0 registrations (sponsorship covers the total cost)"
    elif contribution > 0:
        break_even_registrations = math.ceil(
            remaining_after_sponsorship / contribution
        )
        break_even_message = str(break_even_registrations)
    else:
        break_even_registrations = None
        break_even_message = "Not possible with a zero participant contribution"

    print("\nEvent Cost Breakdown")
    print(f"Venue:                 ₹{venue:,.2f}")
    print(f"Equipment:             ₹{equipment:,.2f}")
    print(f"Catering:              ₹{catering:,.2f}")
    print(f"Transport:             ₹{transport:,.2f}")
    print(f"Certificates:          ₹{certificates:,.2f}")
    print(f"Total event cost:      ₹{total_cost:,.2f}")
    print(f"Sponsorship:           ₹{sponsorship:,.2f}")
    print(f"Participant revenue:   ₹{participant_revenue:,.2f}")
    print(f"Funding shortfall:     ₹{shortfall:,.2f}")
    print(f"Surplus:               ₹{surplus:,.2f}")
    print(f"Break-even registrations: {break_even_message}")


if __name__ == "__main__":
    main()
