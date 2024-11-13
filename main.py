import csv
import time
from memory_profiler import memory_usage


def filter_and_average_age_streaming(file_path, min_age):
    count = 0
    age_sum = 0
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            age = int(row["age"])
            if age > min_age:
                age_sum += age
                count += 1
    return age_sum / count if count > 0 else 0


def generate_performance_report(exec_time_s, memory_usage_kb, avg_age):
    exec_time_ms = exec_time_s * 1000
    with open("python_performance_report.md", "w", encoding="utf-8") as file:
        file.write("# Python Performance Report\n")
        file.write("## Operation: Filter and Aggregate\n")
        file.write("| Metric            | Python                |\n")
        file.write("|-------------------|-----------------------|\n")
        file.write(f"| Execution Time    | {exec_time_ms:.2f} ms               |\n")
        file.write(f"| Memory Usage      | {int(memory_usage_kb)} KB             |\n")
        file.write(f"| Average Age       | {avg_age:.2f}               |\n")


if __name__ == "__main__":
    path_to_csv = "data/account_name_data.csv"
    age_threshold = 30

    peak_memory_usage = max(
        memory_usage((filter_and_average_age_streaming, (path_to_csv, age_threshold)))
    )
    memory_usage_kb = peak_memory_usage * 1024

    start_time = time.time()
    calculated_avg_age = filter_and_average_age_streaming(path_to_csv, age_threshold)
    end_time = time.time()
    execution_time = end_time - start_time

    generate_performance_report(execution_time, memory_usage_kb, calculated_avg_age)
