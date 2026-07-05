def grade_to_point(grade):
    grade = grade.upper()

    if grade == "A":
        return 5
    elif grade == "B":
        return 4
    elif grade == "C":
        return 3
    elif grade == "D":
        return 2
    elif grade == "E":
        return 1
    elif grade == "F":
        return 0
    else:
        print("Invalid grade entered!")
        return None


def main():
    total_units = 0
    total_points = 0

    num_courses = int(input("How many courses do you have? "))

    for i in range(num_courses):
        print(f"\nCourse {i + 1}")

        units = int(input("Enter course units: "))
        grade = input("Enter grade (A-F): ")

        point = grade_to_point(grade)

        if point is None:
            print("Skipping this course due to invalid grade.")
            continue

        total_units += units
        total_points += point * units

    if total_units == 0:
        print("\nNo valid courses entered.")
    else:
        cgpa = total_points / total_units
        print("\n======================")
        print(f"Your CGPA is: {cgpa:.2f}")
        print("======================")


main()