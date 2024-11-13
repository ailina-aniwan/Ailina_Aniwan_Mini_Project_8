import csv
import time
import psutil


# Load data from CSV
def load_data(file_path):
    loaded_data = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            loaded_data.append(
                {
                    "account_name": row["account_name"],
                    "age": int(row["age"]),
                    "city": row["city"],
                }
            )
    return loaded_data


# Filter data and calculate average age above threshold
def filter_and_average_age(data, threshold):
    filtered_ages = [row["age"] for row in data if row["age"] > threshold]
    if len(filtered_ages) == 0:
        return 0
    avg_age = sum(filtered_ages) / len(filtered_ages)
    return avg_age


# Generate performance report with memory usage
def generate_performance_report(execution_time, memory_usage, avg_age):
    execution_time_ms = execution_time * 1000
    memory_usage_kb = memory_usage * 1024
    with open("python_performance_report.md", "w", encoding="utf-8") as file:
        file.write("# Python CLI Performance Report\n")
        file.write("## Operation: Filter and Aggregate\n")
        file.write(
            "Filter all records where age is above a threshold, then compute the average age of this subset.\n\n"
        )
        file.write("| Metric            | Python                |\n")
        file.write("|-------------------|-----------------------|\n")
        file.write(
            f"| Execution Time    | {execution_time_ms:.2f} ms               |\n"
        )
        file.write(f"| Memory Usage      | {memory_usage_kb:.2f} KB             |\n")
        file.write(f"| Average Age       | {avg_age:.2f}               |\n")


if __name__ == "__main__":
    # Set up path and threshold
    path_to_file = "data/account_name_data.csv"
    age_threshold_value = 30

    # Start timing and resource measurement
    start_time = time.time()
    process_instance = psutil.Process()
    memory_before_use = process_instance.memory_info().rss / 1024

    # Load data and process
    loaded_data = load_data(path_to_file)
    avg_age_result = filter_and_average_age(loaded_data, age_threshold_value)

    # End timing and resource measurement
    end_time = time.time()
    memory_after_use = process_instance.memory_info().rss / 1024

    # Calculate performance metrics
    exec_time_total = end_time - start_time
    memory_usage_total = memory_after_use - memory_before_use

    # Generate the performance report
    generate_performance_report(exec_time_total, memory_usage_total, avg_age_result)
