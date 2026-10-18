readings = [28, 31, 35, 37, 29]


def classify_reading(reading, warning_limit, critical_limit):
    """Classify one reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def view_readings(readings):
    """Display all readings."""
    print("\nCURRENT READINGS")
    print("----------------")
    for i in range(len(readings)):
        print("Reading", i + 1, ":", readings[i], "°C")


def add_reading(readings):
    """Check and add a new reading."""
    value = input("Enter new reading: ")

    if value == "":
        print("Invalid input. The reading cannot be empty.")
    elif value.isdigit():
        number = int(value)
        if number <= 100:
            readings.append(number)
            print("Reading added successfully.")
        else:
            print("Invalid reading. Enter a value from 0 to 100.")
    elif value.startswith("-"):
        print("Invalid reading. Enter a value from 0 to 100.")
    else:
        print("Invalid input. Enter a whole number only.")


def classify_readings(readings):
    """Display the category of each reading."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        print(reading, "°C ->", classify_reading(reading, 30, 35))


def compute_total(readings):
    """Calculate the total."""
    total = 0
    for reading in readings:
        total += reading
    return total


def display_summary(readings):
    """Display the reading summary."""
    count = len(readings)
    total = compute_total(readings)
    average = total / count
    smallest = readings[0]
    largest = readings[0]

    normal = 0
    warning = 0
    critical = 0

    for reading in readings:
        if reading < smallest:
            smallest = reading
        if reading > largest:
            largest = reading

        category = classify_reading(reading, 30, 35)
        if category == "NORMAL":
            normal += 1
        elif category == "WARNING":
            warning += 1
        else:
            critical += 1

    print("\nMONITORING SUMMARY")
    print("------------------")
    print("Number of readings :", count)
    print("Total of readings  :", total)
    print(f"Average temperature: {average:.2f} °C")
    print("Minimum temperature:", smallest, "°C")
    print("Maximum temperature:", largest, "°C")
    print()
    print(f"NORMAL   : {normal} ({normal / count * 100:.2f}%)")
    print(f"WARNING  : {warning} ({warning / count * 100:.2f}%)")
    print(f"CRITICAL : {critical} ({critical / count * 100:.2f}%)")

    if critical > 0:
        print("Overall Status: ATTENTION REQUIRED")
    elif warning > 0:
        print("Overall Status: MONITOR")
    else:
        print("Overall Status: NORMAL")


def main(readings):
    """Run the menu."""
    while True:
        print("\nSIMULATED DEVICE MONITORING SYSTEM")
        print("----------------------------------")
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            classify_readings(readings)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main(readings)