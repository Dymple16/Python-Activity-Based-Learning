def classify_student(average):
    if average >= 75:
        return "Excellent"
    elif average >= 60:
        return "Good"
    else:
        return "Needs Improvement"


def main():
    print("Student Performance Trend Analysis")

    exam_count = int(input("Number of examinations: "))
    subject_count = int(input("Number of subjects: "))

    if exam_count < 2:
        print("Enter at least two examinations to analyze trends.")
        return
    if subject_count <= 0:
        print("Enter at least one subject.")
        return

    weak_threshold = 40
    subjects = {}

    for _ in range(subject_count):
        name = input("\nSubject name: ").strip()
        scores = []

        for exam in range(exam_count):
            score = float(input(f"Score in Exam {exam + 1} (0-100): "))
            if not 0 <= score <= 100:
                print("Scores must be between 0 and 100.")
                return
            scores.append(score)

        subjects[name] = scores

    exam_averages = []
    for exam_index in range(exam_count):
        average = sum(
            scores[exam_index] for scores in subjects.values()
        ) / subject_count
        exam_averages.append(average)

    print("\nExamination Averages")
    for index, average in enumerate(exam_averages, start=1):
        print(f"Exam {index}: {average:.2f}%")

    print("\nSubject Trends")
    weak_subjects = []

    for name, scores in subjects.items():
        change = scores[-1] - scores[0]

        if change > 0:
            trend = f"Improved by {change:.1f} points"
        elif change < 0:
            trend = f"Declined by {abs(change):.1f} points"
        else:
            trend = "No change"

        is_weak = all(score < weak_threshold for score in scores)
        if is_weak:
            weak_subjects.append(name)
            weakness = " | Consistently weak"
        else:
            weakness = ""

        print(
            f"{name}: {scores[0]:.1f} -> {scores[-1]:.1f} | "
            f"{trend}{weakness}"
        )

    latest_average = exam_averages[-1]
    classification = classify_student(latest_average)

    print("\nConsistently Weak Subjects")
    if weak_subjects:
        print(", ".join(weak_subjects))
    else:
        print("None")

    print(f"\nStudent Classification: {classification}")


if __name__ == "__main__":
    main()
