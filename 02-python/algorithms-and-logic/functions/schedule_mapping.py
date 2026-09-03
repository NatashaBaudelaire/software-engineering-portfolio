import sys

def create_schedule():
    """Creates and returns the IC schedule dictionary."""
    return {
        "25/05/2021": "Introduction and course overview / History of Computing",
        "01/06/2021": "Computer Architecture",
        "08/06/2021": "Interactive Visualisation Presentation - Professor Nivan",
        "15/06/2021": "Smart Cities Presentation - Professor Kiev",
        "22/06/2021": "GIT Tutoring / Web Development Tutoring",
        "29/06/2021": "Artificial Intelligence / Machine Learning - Professor Adriano Oliveira",
        "06/07/2021": "Robotics Presentation - Professor Hansenclever",
        "13/07/2021": "Free Software Presentation - Professor Castor / (Web Project Submission)",
        "20/07/2021": "LaTeX Tutoring",
        "27/07/2021": "Process Mining Presentation / (LaTeX Project Submission)",
        "03/08/2021": "AI Project",
        "10/08/2021": "AI Project Follow-up",
        "17/08/2021": "AI Project Follow-up",
        "24/08/2021": "AI Project Presentation"
    }

def get_user_input():
    """Gets date input from user."""
    try:
        return sys.stdin.readline().strip()
    except:
        return None

def check_schedule(schedule, date_input):
    """Checks if there's a class on the given date and returns the subject."""
    if date_input in schedule:
        return schedule[date_input]
    return None

def display_result(date_input, subject):
    """Displays the result to the user."""
    if subject:
        print(f"On {date_input} there will be IC class and the subject will be: {subject}")
    else:
        print(f"On {date_input} there is no IC class")

def main():
    """Main function that orchestrates the schedule checking process."""
    ic_schedule = create_schedule()
    date_input = get_user_input()
    
    if date_input:
        subject = check_schedule(ic_schedule, date_input)
        display_result(date_input, subject)

if __name__ == "__main__":
    main()
