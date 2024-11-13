import csv
import time
import psutil


# Load data from CSV
def load_data_from_csv(file_path):
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
def filter_and_average_age(data, threshold_age):
    ages_above_threshold = [row["age"] for row in data if row["age"] > threshold_age]
    if len(ages_above_threshold) == 0:
        return 0
    avg_age = sum(ages_above_threshold) / len(ages_above_threshold)
    return avg_age


# Generate performance report with memory usage in KB
def generate_performance_report(exec_time, mem_usage, avg_age):
    exec_time_ms = exec_time * 1000  # Convert seconds to milliseconds
    mem_usage_kb = mem_usage * 1024  # Convert MB to KB
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
        file.write(f"| Average Age       | {avg_age:.2f}               |\n")


if __name__ == "__main__":
    # Set up path and threshold
    file_path = "data/account_name_data.csv"
    threshold_age = 30

    # Start timing and resource measurement
    start_time = time.time()
    process = psutil.Process()
    initial_memory = process.memory_info().rss / 1024  # Memory in KB

    # Load data and process
    data = load_data_from_csv(file_path)
    average_age = filter_and_average_age(data, threshold_age)

    # End timing and resource measurement
    end_time = time.time()
    final_memory = process.memory_info().rss / 1024  # Memory in KB

    # Calculate performance metrics
    execution_time = end_time - start_time  # Execution time in seconds
    memory_usage = final_memory - initial_memory

    # Generate the performance report
    generate_performance_report(execution_time, memory_usage, average_age)
