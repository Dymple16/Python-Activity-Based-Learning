import re


MIN_LENGTH = 8
MAX_CONSECUTIVE_REPEATS = 2
PROHIBITED_SUBSTRINGS = ["password", "admin", "1234"]


def validate_password(password):
    failures = []

    if len(password) < MIN_LENGTH:
        failures.append(
            f"Must be at least {MIN_LENGTH} characters long "
            f"(current length: {len(password)})."
        )

    categories = [
        ("lowercase letter", r"[a-z]"),
        ("uppercase letter", r"[A-Z]"),
        ("digit", r"\d"),
        ("special character", r"[^A-Za-z0-9]"),
    ]

    for category, pattern in categories:
        if not re.search(pattern, password):
            failures.append(f"Must contain at least one {category}.")

    # Find any run of the same character longer than the allowed limit.
    repeated_run = re.search(
        rf"(.)\1{{{MAX_CONSECUTIVE_REPEATS},}}",
        password
    )
    if repeated_run:
        failures.append(
            "Must not contain the same character more than "
            f"{MAX_CONSECUTIVE_REPEATS} times consecutively "
            f"(found '{repeated_run.group()}')."
        )

    password_lower = password.lower()
    found_prohibited = [
        text for text in PROHIBITED_SUBSTRINGS
        if text.lower() in password_lower
    ]
    if found_prohibited:
        failures.append(
            "Must not contain prohibited substring(s): "
            + ", ".join(found_prohibited)
            + "."
        )

    return failures


def main():
    print("Password Policy Validation Engine")
    count = int(input("Number of passwords to check: "))

    for index in range(1, count + 1):
        password = input(f"\nPassword {index}: ")
        failures = validate_password(password)

        if failures:
            print("Result: Invalid")
            print("Failed conditions:")
            for failure in failures:
                print(f"- {failure}")
        else:
            print("Result: Valid")


if __name__ == "__main__":
    main()
