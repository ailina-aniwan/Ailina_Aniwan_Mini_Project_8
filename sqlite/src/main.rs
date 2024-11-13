use rusqlite::{Connection, Result};
use std::fs::File;
use csv::ReaderBuilder;
use std::io::Write; 
use std::time::Instant;
use sysinfo::{System, SystemExt, ProcessExt};

// Function to create table
fn create_table(conn: &Connection, table: &str) -> Result<()> {
    let create_query = format!("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, account_name TEXT, age INTEGER, city TEXT)", table);
    conn.execute(&create_query, [])?;
    println!("Table '{}' created successfully.", table);
    Ok(())
}

// Function to load data from CSV
fn load_data(conn: &Connection, table: &str, file_path: &str) -> Result<(), Box<dyn std::error::Error>> {
    let mut reader = ReaderBuilder::new().from_reader(File::open(file_path)?);
    for record in reader.records() {
        let record = record?;
        conn.execute(
            &format!("INSERT INTO {} (account_name, age, city) VALUES (?1, ?2, ?3)", table),
            &[&record[0], &record[1], &record[2]],
        )?;
    }
    println!("Data loaded successfully into table '{}'.", table);
    Ok(())
}

// Function for filtering and averaging age
fn filter_and_average_age(conn: &Connection, age_threshold: i32) -> Result<f64> {
    let mut stmt = conn.prepare("SELECT age FROM my_table WHERE age > ?1")?;
    let age_iter = stmt.query_map([age_threshold], |row| row.get::<_, i32>(0))?;
    
    let mut sum = 0;
    let mut count = 0;
    for age in age_iter {
        sum += age?;
        count += 1;
    }
    let average_age = sum as f64 / count as f64;
    Ok(average_age)
}

// Function to generate performance report
fn generate_performance_report(exec_time: f64, memory_usage: u64, average_age: f64) -> std::io::Result<()> {
    let mut file = File::create("../rust_performance_report.md")?;
    writeln!(file, "# Rust Performance Report")?;
    writeln!(file, "## Operation: Filter and Aggregate")?;
    writeln!(file, "Filter all records where age is above a threshold, then compute the average age of this subset.")?;
    writeln!(file, "| Metric            | Rust                  |")?;
    writeln!(file, "|-------------------|-----------------------|")?;
    writeln!(file, "| Execution Time    | {:.2} ms               |", exec_time)?;
    writeln!(file, "| Memory Usage      | {} KB                |", memory_usage)?;
    writeln!(file, "| Average Age       | {:.2}                 |", average_age)?;
    Ok(())
}

fn main() -> Result<()> {
    let conn = Connection::open("my_database.db")?;
    create_table(&conn, "my_table").expect("Failed to create table");

    // Load data
    let file_path = "../data/account_name_data.csv";
    load_data(&conn, "my_table", file_path).expect("Failed to load data");

    // Initialize system and fetch process-specific memory
    let mut sys = System::new_all(); 
    sys.refresh_all();
    let pid = sysinfo::get_current_pid().expect("Unable to get PID");
    let initial_memory = sys.process(pid).map_or(0, |p| p.memory());

    let start = Instant::now();
    let average_age = filter_and_average_age(&conn, 30)?;
    let duration = start.elapsed();
    let exec_time = duration.as_secs_f64() * 1000.0;  // Convert to milliseconds

    // Refresh system and process-specific memory after operation
    sys.refresh_all();
    let final_memory = sys.process(pid).map_or(0, |p| p.memory());
    let memory_usage = final_memory.saturating_sub(initial_memory);

    // Generate performance report
    generate_performance_report(exec_time, memory_usage, average_age).expect("Failed to generate report");

    Ok(())
}

