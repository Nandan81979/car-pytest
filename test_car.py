from vehicle import vehicle_info

def test_vehicle_info():
    expected_output = (
        "Vehicle Number: KA27EJ0147\n"
        "Owner Name: Nandan\n"
        "Vehicle Type: Car\n"
        "Year of Manufacture: 2021"
    )

    result = vehicle_info("KA27EJ0147", "N", "Car", 2020)
    assert result == expected_output
