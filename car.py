def vehicle_info(vehicle_number, owner_name, vehicle_type, year_of_manufacture):
    result = (
        f"Vehicle Number: {vehicle_number}\n"
        f"Owner Name: {owner_name}\n"
        f"Vehicle Type: {vehicle_type}\n"
        f"Year of Manufacture: {year_of_manufacture}"
    )
    return result


def main():
    vehicle_number = "KA27EJ0147"
    owner_name = "Nandan"
    vehicle_type = "Car"
    year_of_manufacture = 2021

    print(vehicle_info(vehicle_number, owner_name, vehicle_type, year_of_manufacture))

if __name__ == "__main__":
    main()
