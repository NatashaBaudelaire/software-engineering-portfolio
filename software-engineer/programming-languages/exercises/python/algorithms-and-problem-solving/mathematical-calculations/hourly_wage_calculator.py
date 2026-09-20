salary = float(input("Enter your monthly salary: "))
hours_per_day = int(input("Enter hours worked per day: "))
days_worked = int(input("Enter number of days worked: "))

total_hours = hours_per_day * days_worked
hourly_rate = salary / total_hours

print(f"I earn a measly £{hourly_rate:.1f} per hour worked.")
