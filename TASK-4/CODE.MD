# Campus Event Financial Planning

## Problem Statement

Campus Event Financial Planning: Calculate venue, equipment, catering, transport, and
certificate costs; determine participant contributions, sponsorship shortfalls, and the minimum
registration count needed to break even.

## Algorithm

1. Read the number of expected participants and the contribution per participant.
2. Read the costs for venue, equipment, catering, transport, and certificates.
3. Read the sponsorship amount.
4. Calculate total event cost by adding all five cost categories.
5. Calculate participant contribution revenue: `participants × contribution per participant`.
6. Calculate the funding shortfall: `max(0, total cost − sponsorship − participant revenue)`.
7. Calculate the minimum registration count needed to break even:
   - If sponsorship covers the total cost, the minimum is 0.
   - Otherwise, divide the remaining cost by the contribution per participant and round up.
8. Display the cost breakdown, revenue, shortfall, and break-even count.

## Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Input expected participants and contribution per participant/]
    B --> C[/Input venue, equipment, catering, transport, and certificate costs/]
    C --> D[/Input sponsorship amount/]
    D --> E[Calculate total event cost]
    E --> F[Calculate participant contribution revenue]
    F --> G[Calculate funding shortfall]
    G --> H{Sponsorship covers total cost?}
    H -- Yes --> I[Minimum registrations = 0]
    H -- No --> J{Contribution per participant > 0?}
    J -- Yes --> K[Calculate registrations needed using ceiling]
    J -- No --> L[Break-even is not possible with current contribution]
    I --> M[Display financial summary]
    K --> M
    L --> M
    M --> N([End])
```



## Sample Input

```text
Expected number of participants: 100
Contribution per participant (₹): 300
Venue cost (₹): 12000
Equipment cost (₹): 8000
Catering cost (₹): 18000
Transport cost (₹): 7000
Certificate cost (₹): 5000
Sponsorship amount (₹): 15000
```

## Sample Output

```text
Event Cost Breakdown
Venue:                 ₹12,000.00
Equipment:             ₹8,000.00
Catering:              ₹18,000.00
Transport:             ₹7,000.00
Certificates:          ₹5,000.00
Total event cost:      ₹50,000.00
Sponsorship:           ₹15,000.00
Participant revenue:   ₹30,000.00
Funding shortfall:     ₹5,000.00
Surplus:               ₹0.00
Break-even registrations: 117
```
