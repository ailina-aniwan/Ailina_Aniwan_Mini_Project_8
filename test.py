from main import filter_and_average_age_streaming


def test_filter_and_average_age_streaming():
    file_path = "data/account_name_data.csv"
    threshold_age = 30
    avg_age = filter_and_average_age_streaming(file_path, threshold_age)

    assert isinstance(avg_age, float), "Average age should be a float"
    assert avg_age > 0, f"Expected average age to be greater than 0, got {avg_age}"


def test_filter_and_average_age_with_mock_data():
    import csv
    import tempfile

    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, newline="", suffix=".csv"
    ) as tmpfile:
        fieldnames = ["account_name", "age", "city"]
        writer = csv.DictWriter(tmpfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(
            [
                {"account_name": "John Doe", "age": 35, "city": "CityA"},
                {"account_name": "Jane Smith", "age": 25, "city": "CityB"},
                {"account_name": "Alice Johnson", "age": 40, "city": "CityC"},
            ]
        )
        tmpfile_name = tmpfile.name

    threshold_age = 30
    avg_age = filter_and_average_age_streaming(tmpfile_name, threshold_age)

    assert isinstance(avg_age, float), "Average age should be a float"
    expected_avg_age = (35 + 40) / 2
    assert (
        avg_age == expected_avg_age
    ), f"Expected average age to be {expected_avg_age}, got {avg_age}"

    import os

    os.remove(tmpfile_name)


if __name__ == "__main__":
    test_filter_and_average_age_streaming()
    test_filter_and_average_age_with_mock_data()
    print("All tests passed!")
