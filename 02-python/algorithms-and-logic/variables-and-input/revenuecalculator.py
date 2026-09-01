GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
END_COLOR = '\033[0m'

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print(f"{YELLOW}Error: Please enter a positive number.{END_COLOR}")
        except ValueError:
            print(f"{YELLOW}Error: Invalid input. Please enter a whole number.{END_COLOR}")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt).replace(',', '.'))
            if value >= 0:
                return value
            else:
                print(f"{YELLOW}Error: Please enter a positive number.{END_COLOR}")
        except ValueError:
            print(f"{YELLOW}Error: Invalid input. Please enter a number.{END_COLOR}")

def calculate_ticket_revenue():
    print(f"{CYAN}--- Ticket Revenue Calculator ---{END_COLOR}\n")
    
    total_tickets = get_positive_int("Enter the total number of tickets: ")
    percent_half = get_positive_int("Enter the percentage of half-price tickets: ")
    full_price = get_positive_float("Enter the full ticket price (£): ")

    half_tickets = int(total_tickets * percent_half / 100)
    full_tickets = total_tickets - half_tickets

    revenue_half = half_tickets * (full_price / 2)
    revenue_full = full_tickets * full_price
    total_revenue = revenue_half + revenue_full

    print("\n" + "-"*40)
    print(f"{GREEN}Half-price tickets: {half_tickets}{END_COLOR}")
    print(f"{GREEN}Full-price tickets: {full_tickets}{END_COLOR}")
    print(f"{CYAN}Revenue from half-price tickets: £{revenue_half:.2f}{END_COLOR}")
    print(f"{CYAN}Revenue from full-price tickets: £{revenue_full:.2f}{END_COLOR}")
    print(f"{CYAN}Total revenue: £{total_revenue:.2f}{END_COLOR}")
    print("-"*40 + "\n")

if __name__ == "__main__":
    calculate_ticket_revenue()