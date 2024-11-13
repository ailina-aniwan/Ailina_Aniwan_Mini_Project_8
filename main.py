import csv
import time
import psutil


# Load data from CSV
def load_data_from_csv(file_path):
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
def filter_and_average_age(data_records, min_age):
    ages_above_threshold = [row["age"] for row in data_records if row["age"] > min_age]
    if len(ages_above_threshold) == 0:
        return 0
    avg_age = sum(ages_above_threshold) / len(ages_above_threshold)
    return avg_age


# Generate performance report with memory usage in KB
def generate_performance_report(exec_time_s, memory_usage_kb, avg_age):
    exec_time_ms = exec_time_s * 1000  # Convert seconds to milliseconds
    with open("python_performance_report.md", "w", encoding="utf-8") as file:
        file.write("# Python CLI Performance Report\n")
        file.write("## Operation: Filter and Aggregate\n")
        file.write(
            "Filter all records where age is above a threshold, then compute the average age of this subset.\n\n"
        )
        file.write("| Metric            | Python                |\n")
        file.write("|-------------------|-----------------------|\n")
        file.write(f"| Execution Time    | {exec_time_ms:.2f} ms               |\n")
        file.write(f"| Memory Usage      | {memory_usage_kb:.2f} KB             |\n")
        file.write(f"| Average Age       | {avg_age:.2f}               |\n")


if __name__ == "__main__":
    # Define file path and age threshold
    path_to_csv = "data/account_name_data.csv"
    age_threshold = 30

    # Start timing and memory tracking
    start_time = time.time()
    process = psutil.Process()
    initial_memory = process.memory_info().rss / 1024  # Memory in KB

    # Load data and perform filtering
    records = load_data_from_csv(path_to_csv)
    calculated_avg_age = filter_and_average_age(records, age_threshold)

    # End timing and memory tracking
    end_time = time.time()
    final_memory = process.memory_info().rss / 1024  # Memory in KB

    # Calculate performance metrics
    execution_time = end_time - start_time  # Execution time in seconds
    memory_usage = final_memory - initial_memory

    # Generate the performance report
    generate_performance_report(execution_time, memory_usage, calculated_avg_age)
