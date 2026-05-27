import csv

def create_csv_file(filename):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['User ID', 'Password'])
            print("CSV file created successfully.")
    except Exception as e:
        print("An error occurred:", e)

def add_credentials(filename, user_id, password):
    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_id, password])
        print("Credentials added successfully.")
    except Exception as e:
        print("An error occurred:", e)

def search_credentials(filename, user_id):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] == user_id:
                    print(f"User ID: {row[0]}, Password: {row[1]}")
                    return
            print("User ID not found.")
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print("An error occurred:", e)

filename = "Information.csv"

# Uncomment below line to create the CSV file initially
# create_csv_file(filename)

while True:
    choice = input("Enter '1' to add credentials, '2' to search, or 'q' to quit: ")
    if choice == '1':
        user_id = input("Enter User ID: ")
        password = input("Enter Password: ")
        add_credentials(filename, user_id, password)
    elif choice == '2':
        user_id = input("Enter User ID to search: ")
        search_credentials(filename, user_id)
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid choice. Please try again.")
