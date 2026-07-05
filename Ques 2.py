print("=" * 55)
print("      PERSONAL POCKET CGPA CALCULATOR")
print("=" * 55)

while True:

    course_total = int(input("\nHow many courses did you offer? "))

    unit_sum = 0
    point_sum = 0

    for count in range(1, course_total + 1):

        print(f"\nCourse {count}")

        unit = int(input("Course Unit: "))
        mark = int(input("Course Score: "))

        match mark:

            case m if 70 <= m <= 100:
                letter = "A"
                grade_point = 5

            case m if 60 <= m <= 69:
                letter = "B"
                grade_point = 4

            case m if 50 <= m <= 59:
                letter = "C"
                grade_point = 3

            case m if 45 <= m <= 49:
                letter = "D"
                grade_point = 2

            case m if 40 <= m <= 44:
                letter = "E"
                grade_point = 1

            case m if 0 <= m <= 39:
                letter = "F"
                grade_point = 0

            case _:
                print("Invalid Score!")
                continue

        earned_points = unit * grade_point

        unit_sum += unit
        point_sum += earned_points

        print("Grade:", letter)
        print("Point Earned:", earned_points)

    gpa = point_sum / unit_sum

    print("\n========== RESULT ==========")
    print("Total Units :", unit_sum)
    print("Total Points:", point_sum)
    print("CGPA :", round(gpa, 2))
    print("============================")

    again = input("\nDo another calculation? (Y/N): ").upper()

    match again:
        case "Y":
            continue
        case "N":
            print("\nProgram Ended.")
            break
        case _:
            print("\nInvalid Input.")
            break