class Bike:
    def __init__(self, bike_id, name):
        self.bike_id = bike_id
        self.name = name
        self.available = True
        self.customer = None

    def book(self, customer_name):
        if not self.available:
            return False, "Bike is already booked"

        if not customer_name.strip():
            return False, "Customer name cannot be empty"

        self.available = False
        self.customer = customer_name
        return True, f"Bike '{self.name}' booked for {customer_name}"

    def return_bike(self):
        if self.available:
            return False, "Bike is not currently booked"

        self.available = True
        self.customer = None
        return True, f"Bike '{self.name}' returned successfully"


class RentalSystem:
    def __init__(self):
        self.bikes = {}

    def add_bike(self, bike):
        self.bikes[bike.bike_id] = bike

    def find_bike(self, bike_id):
        return self.bikes.get(bike_id)

    def show_bikes(self):
        print("\nAvailable Bikes:")
        for bike in self.bikes.values():
            status = "Available" if bike.available else f"Booked by {bike.customer}"
            print(f"ID: {bike.bike_id} | Name: {bike.name} | Status: {status}")

    def book_bike(self, bike_id, customer_name):
        bike = self.find_bike(bike_id)
        if not bike:
            return False, "Bike not found"

        return bike.book(customer_name)

    def return_bike(self, bike_id):
        bike = self.find_bike(bike_id)
        if not bike:
            return False, "Bike not found"

        return bike.return_bike()


def main():
    system = RentalSystem()

    # Preload bikes
    system.add_bike(Bike(1, "Royal Enfield"))
    system.add_bike(Bike(2, "Pulsar"))
    system.add_bike(Bike(3, "Apache"))

    while True:
        print("\n--- Bike Rental System ---")
        print("1. Show Bikes")
        print("2. Book Bike")
        print("3. Return Bike")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            system.show_bikes()

        elif choice == "2":
            try:
                bike_id = int(input("Enter Bike ID: "))
                name = input("Enter Customer Name: ")
                status, message = system.book_bike(bike_id, name)
                print(message)
            except ValueError:
                print("Invalid Bike ID")

        elif choice == "3":
            try:
                bike_id = int(input("Enter Bike ID: "))
                status, message = system.return_bike(bike_id)
                print(message)
            except ValueError:
                print("Invalid Bike ID")

        elif choice == "4":
            print("Exiting system. Bye.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()