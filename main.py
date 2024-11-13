import csv
import time
import psutil


# Load data from CSV
def load_data(file_path):
    data = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(
                {
                    "account_name": row["account_name"],
                    "age": int(row["age"]),
                    "city": row["city"],
                }
            )
    return data


# Filter data and calculate average age above threshold
def filter_and_average_age(data, age_threshold):
    filtered_ages = [row["age"] for row in data if row["age"] > age_threshold]
    if len(filtered_ages) == 0:
        return 0
    average_age = sum(filtered_ages) / len(filtered_ages)
    return average_age


# Generate performance report with memory usage
def generate_performance_report(exec_time, mem_usage, average_age):
    exec_time_ms = exec_time * 1000
    mem_usage_kb = mem_usage * 1024
    with open("python_performance_report.md", "w", encoding="utf-8") as file:
        file.write("# Python Performance Report\n")
        file.write("## Operation: Filter and Aggregate\n")
        file.write(
            "Filter all records where age is above a threshold, then compute the average age of this subset.\n\n"
        )
        file.write("| Metric            | Python                |\n")
        file.write("|-------------------|-----------------------|\n")
        file.write(f"| Execution Time    | {exec_time_ms:.2f} ms               |\n")
        file.write(f"| Memory Usage      | {mem_usage_kb:.2f} KB             |\n")
        file.write(f"| Average Age       | {average_age:.2f}               |\n")


if __name__ == "__main__":
    file_path = "data/account_name_data.csv"
    age_threshold = 30

    # Start timing and resource measurement
    start_time = time.time()
    process = psutil.Process()
    memory_before = process.memory_info().rss / 1024

    # Load data and process
    data = load_data(file_path)
    average_age = filter_and_average_age(data, age_threshold)

    # End timing and resource measurement
    end_time = time.time()
    memory_after = process.memory_info().rss / 1024

    # Calculate performance metrics
    exec_time = end_time - start_time
    mem_usage = memory_after - memory_before

    # Generate the performance report
    generate_performance_report(exec_time, mem_usage, average_age)
