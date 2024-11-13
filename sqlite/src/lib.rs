use rusqlite::{Connection, Result};
use std::fs::File;
use csv::ReaderBuilder;

pub fn create_table(conn: &Connection, table: &str) -> Result<()> {
    let create_query = format!("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)", table);
    conn.execute(&create_query, [])?;
    println!("Table '{}' created successfully.", table);
    Ok(())
}

pub fn load_data(conn: &Connection, table: &str, file_path: &str) -> Result<(), Box<dyn std::error::Error>> {
    let mut reader = ReaderBuilder::new().from_reader(File::open(file_path)?);

    for record in reader.records() {
        let record = record?;
        conn.execute(
            &format!("INSERT INTO {} (name, age) VALUES (?1, ?2)", table),
            &[&record[0], &record[1]],
        )?;
    }

    println!("Data loaded successfully into table '{}'.", table);
    Ok(())
}

pub fn execute_query(conn: &Connection, query: &str) -> Result<()> {
    let mut stmt = conn.prepare(query)?;
    let rows = stmt.query_map([], |row| {
        let id: i32 = row.get(0)?;
        let name: String = row.get(1)?;
        let age: i32 = row.get(2)?;
        Ok((id, name, age))
    })?;

    for row in rows {
        let (id, name, age) = row?;
        println!("ID: {}, Name: {}, Age: {}", id, name, age);
    }
    Ok(())
}

pub fn delete_table(conn: &Connection, table: &str) -> Result<()> {
    let delete_query = format!("DROP TABLE IF EXISTS {}", table);
    conn.execute(&delete_query, [])?;
    println!("Table '{}' dropped successfully.", table);
    Ok(())
}
