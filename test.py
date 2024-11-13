import os
from main import load_data, filter_and_average_age, generate_performance_report

# Set up paths and mock data
file_path = "data/account_name_data.csv"
report_path = "python_performance_report.md"
sample_data = [
    {"account_name": "Alice", "age": 25, "city": "New York"},
    {"account_name": "Bob", "age": 35, "city": "Los Angeles"},
    {"account_name": "Charlie", "age": 40, "city": "Chicago"},
    {"account_name": "David", "age": 29, "city": "Houston"},
]

# Test load_data function
data = load_data(file_path)
assert len(data) > 0, "Data should be loaded from the CSV file"
assert (
    "account_name" in data[0] and "age" in data[0] and "city" in data[0]
), "Each record should contain 'account_name', 'age', and 'city' fields"
print("load_data function passed.")

# Test filter_and_average_age with data above threshold
age_threshold = 30
average_age = filter_and_average_age(sample_data, age_threshold)
assert (
    abs(average_age - 37.5) < 0.1
), "Average age should be approximately 37.5 for ages above threshold"
print("filter_and_average_age (above threshold) function passed.")

# Test filter_and_average_age with no data above threshold
age_threshold = 50
average_age = filter_and_average_age(sample_data, age_threshold)
assert average_age == 0, "Average age should be 0 when no data meets the threshold"
print("filter_and_average_age (no data above threshold) function passed.")

# Test generate_performance_report function
generate_performance_report(exec_time=0.5, mem_usage=50, average_age=35.0)
assert os.path.exists(report_path), "Performance report file should be created"
print("generate_performance_report function passed.")

if os.path.exists(report_path):
    os.remove(report_path)

print("All tests passed.")
