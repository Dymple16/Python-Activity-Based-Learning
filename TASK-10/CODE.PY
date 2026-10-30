# Each student is stored as a dictionary.
# Attendance is a nested list: [student_id, [(date, status), ...]]
# Events and resources use tuples for fixed details.

students = []
attendance_records = []
events = [
    ("E101", "Tech Fest", []),
    ("E102", "Cultural Day", []),
]
resources = [
    ("R101", "Projector", "Available"),
    ("R102", "Laptop", "Available"),
    ("R103", "Lab Seat", "Available"),
]
allocations = []


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student():
    student_id = input("Student ID: ").strip()

    if find_student(student_id):
        print("That student ID already exists.")
        return

    name = input("Student name: ").strip()
    course = input("Course: ").strip()

    if not student_id or not name or not course:
        print("ID, name, and course cannot be empty.")
        return

    students.append({
        "id": student_id,
        "name": name,
        "course": course,
        "marks": [],
    })
    print(f"Student {name} added.")


def record_attendance():
    student_id = input("Student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    date = input("Date (e.g. 2026-10-30): ").strip()
    status = input("Status (P for present, A for absent): ").strip().upper()

    if status not in ("P", "A"):
        print("Enter P or A.")
        return

    # Find an existing attendance list, or create one.
    record = None
    for item in attendance_records:
        if item[0] == student_id:
            record = item
            break

    if record is None:
        record = [student_id, []]
        attendance_records.append(record)

    record[1].append((date, status))
    print(f"Attendance recorded for {student['name']}.")


def enter_marks():
    student_id = input("Student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    subject = input("Subject: ").strip()
    try:
        score = float(input("Mark (0-100): "))
    except ValueError:
        print("Enter a valid numeric mark.")
        return

    if not subject or not 0 <= score <= 100:
        print("Subject is required and marks must be from 0 to 100.")
        return

    student["marks"].append((subject, score))
    print(f"Mark recorded for {subject}.")


def register_for_event():
    student_id = input("Student ID: ").strip()

    if find_student(student_id) is None:
        print("Student not found.")
        return

    print("Events:")
    for event_id, event_name, _registrations in events:
        print(f"{event_id}: {event_name}")

    event_id = input("Event ID: ").strip()
    for event in events:
        if event[0] == event_id:
            if student_id in event[2]:
                print("Student is already registered for this event.")
            else:
                event[2].append(student_id)
                print(f"Registered for {event[1]}.")
            return

    print("Event not found.")


def allocate_resource():
    student_id = input("Student ID: ").strip()

    if find_student(student_id) is None:
        print("Student not found.")
        return

    print("Resources:")
    for resource_id, resource_name, status in resources:
        print(f"{resource_id}: {resource_name} ({status})")

    resource_id = input("Resource ID: ").strip()

    for index, (current_id, name, status) in enumerate(resources):
        if current_id == resource_id:
            if status != "Available":
                print("Resource is not available.")
                return

            # Tuple unpacking reads the resource fields.
            resources[index] = (current_id, name, "Allocated")
            allocations.append((resource_id, student_id))
            print(f"{name} allocated to {student_id}.")
            return

    print("Resource not found.")


def show_summary():
    print("\n--- Campus Summary ---")
    print(f"Students: {len(students)}")

    for student in students:
        print(
            f"{student['id']} | {student['name']} | {student['course']}"
        )

        if student["marks"]:
            marks_text = ", ".join(
                f"{subject}: {score:g}"
                for subject, score in student["marks"]
            )
            print(f"  Marks: {marks_text}")
        else:
            print("  Marks: No marks recorded")

    print("\nAttendance:")
    if not attendance_records:
        print("No attendance recorded.")
    for student_id, entries in attendance_records:
        present = sum(1 for _date, status in entries if status == "P")
        total = len(entries)
        percentage = (present / total * 100) if total else 0
        print(f"{student_id}: {present}/{total} present ({percentage:.1f}%)")

    print("\nEvents:")
    for event_id, name, registrations in events:
        print(f"{event_id} | {name} | {len(registrations)} registered")

    print("\nResources:")
    for resource_id, name, status in resources:
        print(f"{resource_id} | {name} | {status}")

    print(f"\nResource allocations: {len(allocations)}")


def main():
    while True:
        print(
            "\n=== Smart Campus Management ===\n"
            "1. Add student\n"
            "2. Record attendance\n"
            "3. Enter marks\n"
            "4. Register for event\n"
            "5. Allocate resource\n"
            "6. Summary report\n"
            "0. Exit"
        )

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            record_attendance()
        elif choice == "3":
            enter_marks()
        elif choice == "4":
            register_for_event()
        elif choice == "5":
            allocate_resource()
        elif choice == "6":
            show_summary()
        elif choice == "0":
            print("Exiting Smart Campus Management.")
            break
        else:
            print("Invalid choice. Select an option from 0 to 6.")


if __name__ == "__main__":
    main()
