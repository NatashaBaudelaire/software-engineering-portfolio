def convert_to_integers(string_list):
    integer_numbers = []

    for element in string_list:
        try:
            number = int(element)
            integer_numbers.append(number)
            print(f"[OK] '{element}' converted to {number}")

        except ValueError:
            print(f"[ERROR] '{element}' cannot be converted to an integer")

        except Exception as e:
            print(f"[ERROR] Unexpected error converting '{element}': {e}")
    return integer_numbers

def main():
    test_list = ["10", "25", "3.14", "abc", "100", "42text", "-15", "0", ""]
    
    print("Original list:", test_list)
    print("\nProcessing conversion...\n")
    
    result = convert_to_integers(test_list)
    
    print(f"\nConverted list: {result}")
    print(f"Total converted elements: {len(result)}")
    
def test_with_different_cases():
    print("\n" + "="*50)
    print("ADDITIONAL TESTS")
    print("="*50)

    case1 = ["1", "2", "3", "4", "5"]
    print(f"\nCase 1 - Only valid: {case1}")
    result1 = convert_to_integers(case1)
    print(f"Result: {result1}")
    
    case2 = ["abc", "12.34", "text", "123abc"]
    print(f"\nCase 2 - Only invalid: {case2}")
    result2 = convert_to_integers(case2)
    print(f"Result: {result2}")
    
    case3 = []
    print(f"\nCase 3 - Empty list: {case3}")
    result3 = convert_to_integers(case3)
    print(f"Result: {result3}")
    
if __name__ == "__main__":
    main()
    test_with_different_cases()
