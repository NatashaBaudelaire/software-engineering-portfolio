
# Colour codes for terminal output (British English)
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
END_COLOUR = '\033[0m'


def get_positive_int(prompt):
    """Prompt for a positive integer, ensuring valid input."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print(f"{YELLOW}Error: Enter a positive number.{END_COLOUR}")
        except ValueError:
            print(f"{YELLOW}Error: Invalid input. Enter an integer.{END_COLOUR}")


def get_positive_float(prompt):
    """Prompt for a positive float, ensuring valid input."""
    while True:
        try:
            value = float(input(prompt).replace(',', '.'))
            if value >= 0:
                return value
            else:
                print(f"{YELLOW}Error: Enter a positive number.{END_COLOUR}")
        except ValueError:
            print(f"{YELLOW}Error: Invalid input. Enter a number.{END_COLOUR}")


def calculate_ticket_revenue():
    """Calculate and display ticket revenue using British English and clear output."""
    print(f"{CYAN}--- Ticket Revenue Calculator ---{END_COLOUR}\n")
    
    total_tickets = get_positive_int("Enter total number of tickets: ")
    percent_half = get_positive_int("Enter percentage of half-price tickets: ")
    full_price = get_positive_float("Enter full ticket price (£): ")

    half_tickets = int(total_tickets * percent_half / 100)
    full_tickets = total_tickets - half_tickets

    revenue_half = half_tickets * (full_price / 2)
    revenue_full = full_tickets * full_price
    total_revenue = revenue_half + revenue_full

    print("\n" + "-"*40)
    print(f"{GREEN}Half-price tickets: {half_tickets}{END_COLOUR}")
    print(f"{GREEN}Full-price tickets: {full_tickets}{END_COLOUR}")
    print(f"{CYAN}Revenue from half-price tickets: £{revenue_half:.2f}{END_COLOUR}")
    print(f"{CYAN}Revenue from full-price tickets: £{revenue_full:.2f}{END_COLOUR}")
    print(f"{CYAN}Total revenue: £{total_revenue:.2f}{END_COLOUR}")
    print("-"*40 + "\n")

if __name__ == "__main__":
    calculate_ticket_revenue()
