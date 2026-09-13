
# Colour codes for terminal output (British English)
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
END_COLOUR = '\033[0m'


def get_grade(number):
    """Prompt the user for a grade, ensuring valid input between 0.0 and 10.0."""
    while True:
        try:
            grade = float(input(f"Enter Grade {number} (0.0 - 10.0): ").replace(',', '.'))
            if 0.0 <= grade <= 10.0:
                return grade
            else:
                print(f"{YELLOW}Error: Grade must be between 0.0 and 10.0.{END_COLOUR}")
        except ValueError:
            print(f"{YELLOW}Error: Invalid input. Please enter a number.{END_COLOUR}")


def calculate_and_show_status():
    """Calculate and display the student's grade status using British English and clear output."""
    print("\n--- Student Grade Status Checker ---\n")

    grade1 = get_grade(1)
    grade2 = get_grade(2)

    average = (grade1 + grade2) / 2

    print(f"\nEntered Grades: {grade1:.1f} and {grade2:.1f}")
    print(f"Calculated Average: {average:.2f}")

    if average >= 7.0:
        status = "STATUS: PASS"
        colour = GREEN
    elif 5.0 <= average < 7.0:
        status = "STATUS: RECOVERY"
        colour = YELLOW
    else:
        status = "STATUS: FAIL"
        colour = RED

    print(f"{colour}{status}{END_COLOUR}\n")

if __name__ == "__main__":
    calculate_and_show_status()
