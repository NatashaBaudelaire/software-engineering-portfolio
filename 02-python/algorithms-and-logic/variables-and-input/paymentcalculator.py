GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
END_COLOR = '\033[0m'

def get_product_value():
    while True:
        try:
            value = float(input(f"{BLUE}Enter the product total value (£): {END_COLOR}").replace(',', '.'))
            if value > 0:
                return value
            else:
                print(f"{YELLOW}Error: Value must be positive.{END_COLOR}")
        except ValueError:
            print(f"{YELLOW}Error: Invalid input. Enter a valid number.{END_COLOR}")

def get_payment_option():
    print("\n" + "="*30)
    print(f"{BLUE}Choose your payment option:{END_COLOR}")
    print(f" {GREEN}[1] Cash / Bank Transfer - 10% discount{END_COLOR}")
    print(f" {GREEN}[2] Card upfront - 5% discount{END_COLOR}")
    print(f" {YELLOW}[3] 2x on Card - 5% increase{END_COLOR}")
    print(f" {YELLOW}[4] 3x to 10x on Card - 10% increase{END_COLOR}")
    print("="*30)

    while True:
        try:
            option = int(input(f"{BLUE}Enter your choice (1-4): {END_COLOR}"))
            if 1 <= option <= 4:
                return option
            else:
                print(f"{YELLOW}Invalid option. Choose 1, 2, 3, or 4.{END_COLOR}")
        except ValueError:
            print(f"{YELLOW}Invalid input. Enter a number.{END_COLOR}")

def calculate_final_value():
    print(f"\n{BLUE}--- Shop Payment Calculator ---{END_COLOR}")
    
    original_value = get_product_value()
    option = get_payment_option()

    final_value = original_value
    adjustment = 0
    instalments = 1

    if option == 1:
        adjustment = 0.10 * original_value
        final_value -= adjustment
        colour_msg = GREEN
    elif option == 2:
        adjustment = 0.05 * original_value
        final_value -= adjustment
        colour_msg = GREEN
    elif option == 3:
        adjustment = 0.05 * original_value
        final_value += adjustment
        instalments = 2
        colour_msg = YELLOW
    elif option == 4:
        adjustment = 0.10 * original_value
        final_value += adjustment
        while True:
            try:
                instalments = int(input(f"{BLUE}Enter number of instalments (3 to 10): {END_COLOR}"))
                if 3 <= instalments <= 10:
                    break
                else:
                    print(f"{YELLOW}Invalid number. Choose between 3 and 10.{END_COLOR}")
            except ValueError:
                print(f"{YELLOW}Invalid input. Enter a whole number.{END_COLOR}")
        colour_msg = YELLOW

    print("\n" + "-"*35)
    print(f"{BLUE}Original value:{END_COLOR} £{original_value:.2f}")

    if adjustment > 0 and option in (1, 2):
        print(f"{colour_msg}Discount: £{adjustment:.2f}{END_COLOR}")
    elif adjustment > 0 and option in (3, 4):
        print(f"{colour_msg}Increase: £{adjustment:.2f}{END_COLOR}")

    print(f"\n{CYAN}TOTAL TO PAY:{END_COLOR} {CYAN}£{final_value:.2f}{END_COLOR}")

    if instalments > 1:
        instalment_value = final_value / instalments
        print(f"{BLUE}Payment plan:{END_COLOR} {instalments}x of £{instalment_value:.2f} (with increase of £{adjustment:.2f})")
    elif option in (1, 2):
        print(f"{BLUE}Payment plan:{END_COLOR} Upfront payment (with discount of £{adjustment:.2f})")

    print("-"*35)

if __name__ == "__main__":
    calculate_final_value()