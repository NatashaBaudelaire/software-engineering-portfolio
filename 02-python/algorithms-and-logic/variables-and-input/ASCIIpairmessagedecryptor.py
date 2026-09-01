def decrypt_message(encrypted):
    L = len(encrypted)
    num_chars = L // 2
    decrypted = ""

    for j in range(num_chars):
        digit_a = encrypted[j]
        digit_b = encrypted[L - 1 - j]
        ascii_code = int(digit_a + digit_b)
        decrypted += chr(ascii_code)

    return decrypted

def main():
    try:
        N = int(input("Enter the number of messages to decrypt: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    for i in range(N):
        encrypted = input(f"Enter encrypted message #{i + 1}: ").strip()
        if len(encrypted) < 2:
            print("Message too short to decrypt.")
            continue
        try:
            decrypted = decrypt_message(encrypted)
            print(f"Decrypted message: {decrypted}")
        except ValueError:
            print("Invalid message format. Only digits are allowed.")

if __name__ == "__main__":
    main()
