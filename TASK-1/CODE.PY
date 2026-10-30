AGGREGATE_MIN = 70
SUBJECT_MIN = 60
ATTENDANCE_MIN = 75
INCOME_MAX = 300_000

SUBJECTS = ["Mathematics", "Science", "English"]


def is_eligible(applicant):
    return (
        applicant["aggregate"] >= AGGREGATE_MIN
        and all(mark >= SUBJECT_MIN for mark in applicant["subjects"].values())
        and applicant["attendance"] >= ATTENDANCE_MIN
        and applicant["income"] <= INCOME_MAX
    )


def ranking_key(applicant):
    # Higher aggregate and attendance rank first.
    # Lower income ranks first when the first two values are tied.
    # Name provides a final deterministic tie-break.
    return (
        -applicant["aggregate"],
        -applicant["attendance"],
        applicant["income"],
        applicant["name"].casefold(),
    )


def main():
    applicant_count = int(input("Enter number of applicants: "))
    scholarship_count = int(input("Enter number of scholarships available: "))

    eligible = []

    for index in range(applicant_count):
        print(f"\nApplicant {index + 1}")
        name = input("Name: ").strip()
        aggregate = float(input("Aggregate marks (%): "))

        subjects = {}
        for subject in SUBJECTS:
            subjects[subject] = float(input(f"{subject} marks (%): "))

        attendance = float(input("Attendance (%): "))
        income = float(input("Annual family income (₹): "))

        applicant = {
            "name": name,
            "aggregate": aggregate,
            "subjects": subjects,
            "attendance": attendance,
            "income": income,
        }

        if is_eligible(applicant):
            eligible.append(applicant)

    eligible.sort(key=ranking_key)

    print("\nRanked Eligible Applicants")
    if not eligible:
        print("No eligible applicants.")
        return

    for rank, applicant in enumerate(eligible, start=1):
        award = "Awarded" if rank <= scholarship_count else "Waitlisted"
        print(
            f"{rank}. {applicant['name']} | "
            f"Aggregate: {applicant['aggregate']:.1f}% | "
            f"Attendance: {applicant['attendance']:.1f}% | "
            f"Income: ₹{applicant['income']:,.0f} | "
            f"{award}"
        )


if __name__ == "__main__":
    main()
