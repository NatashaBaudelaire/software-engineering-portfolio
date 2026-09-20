def collect_client_data():

    clients = []
    num_clients = 10

    print("--- Client Data Collection ---")

    for i in range(num_clients):
        print(f"\nCollecting data for Client {i + 1}/{num_clients}:")

        while True:
            name = input("Enter name: ").strip()
            if name and not name.isdigit():
                break
            else:
                print("Error: Name cannot be empty or numeric. Please enter a valid name.")
        while True:
            try:
                age_str = input("Enter age: ").strip()
                age = int(age_str)
                if age > 0:
                    break
                else:
                    print("Error: Age must be a positive number.")
            except ValueError:
                print("Error: Age must be a valid integer.")
                
        while True:
            gender = input("Enter sex/gender: ").strip()
            if gender and not gender.isdigit():
                break
            else:
                print("Error: Sex/Gender cannot be empty or numeric. Please enter a valid value.")

        client = {
            'Name': name,
            'Age': age,
            'Sex': gender
        }
        clients.append(client)

    print("\n--- Data Collection Completed ---")

    print("\nData of all clients:")
    for j, c in enumerate(clients):
        print(f"Client {j + 1}: Name: {c['Name']}, Age: {c['Age']}, Sex: {c['Sex']}")

    return clients

client_list = collect_client_data()
