from main import load_data_from_csv, filter_and_average_age


def test_load_data():
    file_path = "data/account_name_data.csv"
    data = load_data_from_csv(file_path)
    assert isinstance(data, list), "Data should be loaded as a list"
    assert len(data) > 0, "Data should not be empty"
    assert all(
        "account_name" in row and "age" in row and "city" in row for row in data
    ), "Each row should contain account_name, age, and city"


def test_filter_and_average_age():
    data = [
        {"account_name": "John Doe", "age": 35, "city": "CityA"},
        {"account_name": "Jane Smith", "age": 25, "city": "CityB"},
        {"account_name": "Alice Johnson", "age": 40, "city": "CityC"},
    ]
    threshold_age = 30
    avg_age = filter_and_average_age(data, threshold_age)
    assert avg_age == 37.5, f"Expected average age to be 37.5, got {avg_age}"
