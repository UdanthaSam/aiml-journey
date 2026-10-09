
import csv

FILE_PATH = "car_fleet.csv"


# Car Class
class Car:
    def __init__(self, registration_no, brand, model, year, mileage, daily_rate, available):
        self.registration_no = registration_no
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.daily_rate = daily_rate
        self.available = available

    # Display car information
    def display(self):
        status = "Yes" if self.available else "No"

        print(f"{self.registration_no:<18} {self.brand:<15} {self.model:<15} {self.year:<8} {self.mileage:<12.1f} {self.daily_rate:<12.2f} {status:<10}")

    # Update an attribute
    def update_attribute(self, attribute, value):
        if attribute in ["brand", "model", "year", "mileage", "daily_rate", "available"]:
            setattr(self, attribute, value)
            print(f"{attribute} updated successfully!")
        else:
            print("Invalid attribute!")

    # Search by any attribute
    def search_attribute(self, attribute, value):
        if hasattr(self, attribute):
            current_value = getattr(self, attribute)

            return value.lower() in str(current_value).lower()

        return False


# Dictionary to store Car objects
cars = {}


# Display Table Header
def table_header():
    print("\n" + "=" * 100)
    print(f"{'Registration No':<18} {'Brand':<15} {'Model':<15} {'Year':<8} {'Mileage':<12} {'Daily Rate':<12} {'Available':<10}")
    print("-" * 100)


# Import CSV Data
def import_data():
    try:
        with open(FILE_PATH, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            cars.clear()

            for row in reader:
                registration_no = row[0].strip().upper()
                brand = row[1]
                model = row[2]
                year = int(row[3])
                mileage = float(row[4])
                daily_rate = float(row[5])
                available = row[6].strip().lower() == "true"

                car = Car(
                    registration_no,
                    brand,
                    model,
                    year,
                    mileage,
                    daily_rate,
                    available
                )

                cars[registration_no] = car

        print("Fleet data imported successfully!")

    except FileNotFoundError:
        print("CSV file not found!")


# Save Dictionary to CSV
def save_to_csv():
    with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Registration No",
            "Brand",
            "Model",
            "Year",
            "Mileage",
            "Daily Rate",
            "Available"
        ])

        for car in cars.values():
            writer.writerow([
                car.registration_no,
                car.brand,
                car.model,
                car.year,
                car.mileage,
                car.daily_rate,
                car.available
            ])

    print("Fleet data saved to CSV successfully!")


# Show All Cars
def show_all():
    if not cars:
        print("No cars available in the fleet!")
        return

    table_header()

    for car in cars.values():
        car.display()

    print("=" * 100)
    print(f"Total cars: {len(cars)}")


# Search by Any Attribute
def search_by_attribute():
    print("\nSearch by:")
    print("registration_no, brand, model, year, mileage, daily_rate, available")

    attribute = input("Enter attribute to search: ").strip().lower()

    if attribute not in [
        "registration_no", "brand", "model", "year",
        "mileage", "daily_rate", "available"
    ]:
        print("Invalid attribute!")
        return

    value = input("Enter search value: ").strip()

    found = False

    table_header()

    for car in cars.values():
        if car.search_attribute(attribute, value):
            car.display()
            found = True

    if not found:
        print("No matching cars found!")

    print("=" * 100)
    print("Search completed!\n")


# Update Car Details
def updating():
    registration_no = input("Enter car registration number: ").strip().upper()

    if registration_no in cars:
        car = cars[registration_no]

        print("\nWhat do you want to update?")
        print("brand, model, year, mileage, daily_rate, available")

        attribute = input("Enter attribute to update: ").strip().lower()

        if attribute in [
            "brand", "model", "year",
            "mileage", "daily_rate", "available"
        ]:

            if attribute == "available":
                car.available = not car.available
                print("Availability changed!")

            else:
                value = input("Enter new value: ").strip()

                try:
                    if attribute == "year":
                        value = int(value)

                    elif attribute in ["mileage", "daily_rate"]:
                        value = float(value)

                except ValueError:
                    print("Invalid numeric value!")
                    return

                car.update_attribute(attribute, value)

        else:
            print("Invalid attribute!")

    else:
        print("Car not found!")


# Change Car Availability
def change_availability():
    registration_no = input("Enter car registration number: ").strip().upper()

    if registration_no in cars:
        car = cars[registration_no]

        car.available = not car.available

        print(f"{registration_no}'s availability changed to {car.available}.")

    else:
        print(f"No car found with registration number {registration_no}.")


# Add New Car
def add_new():
    registration_no = input("Enter registration number: ").strip().upper()

    if not registration_no:
        print("Registration number cannot be empty!")
        return

    if registration_no in cars:
        print("A car with this registration number already exists!")
        return

    brand = input("Enter brand: ").strip().title()
    model = input("Enter model: ").strip()

    try:
        year = int(input("Enter manufacturing year: "))
        mileage = float(input("Enter mileage (km): "))
        daily_rate = float(input("Enter daily rental rate (LKR): "))

    except ValueError:
        print("Invalid numeric value!")
        return

    if year < 1886 or mileage < 0 or daily_rate < 0:
        print("Invalid year, mileage, or rental rate!")
        return

    available = input("Available (yes/no): ").strip().lower() == "yes"

    car = Car(
        registration_no,
        brand,
        model,
        year,
        mileage,
        daily_rate,
        available
    )

    cars[registration_no] = car

    print("New car added successfully!")


# Main Menu
def main_menu():
    while True:
        print("\n" + "=" * 47)
        print("          CAR FLEET MANAGEMENT SYSTEM")
        print("=" * 47)

        print("  1. Add New Car")
        print("  2. View All Cars")
        print("  3. Search by Any Attribute")
        print("  4. Update Car Details")
        print("  5. Change Car Availability")
        print("-" * 47)
        print("  6. Import Fleet Data from CSV")
        print("  7. Save Fleet Data to CSV")
        print("-" * 47)
        print("  0. Exit")
        print("=" * 47)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_new()

        elif choice == "2":
            show_all()

        elif choice == "3":
            search_by_attribute()

        elif choice == "4":
            updating()

        elif choice == "5":
            change_availability()

        elif choice == "6":
            import_data()

        elif choice == "7":
            save_to_csv()

        elif choice == "0":
            print("\nThank you for using the Car Fleet Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Start the Program
main_menu()
