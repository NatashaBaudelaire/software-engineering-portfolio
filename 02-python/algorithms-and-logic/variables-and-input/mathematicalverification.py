GREEN = '\033[92m'      
YELLOW = '\033[93m'      
RESET = '\033[0m'        

def gdr(n):
    value = 1
    for i in range(2, n + 1):
        value = value * i + 1
    return value

def main():
    try:
        X = int(input("Enter the expected value (X): "))
        Z = int(input("Enter the sequence number (Z): "))
    except ValueError:
        print(f"{YELLOW}Invalid input. Please enter integers only.{RESET}")
        return

    result = gdr(Z)

    print(f"\nComputed value for gdr({Z}) = {result}")

    if result == X:
        print(f"{GREEN}We found another clue! We're almost there!{RESET}")
    else:
        print(f"{YELLOW}Oops, still some work to do...{RESET}")

if __name__ == "__main__":
    main()
