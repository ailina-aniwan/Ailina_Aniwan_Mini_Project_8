use rusqlite::{Connection, Result};
use sqlite::{create_table, load_data, execute_query, delete_table};

fn setup_test_db() -> Result<Connection> {
    let conn = Connection::open_in_memory()?; // Creates an in-memory database for testing
    Ok(conn)
}

#[test]
fn test_create_table() {
    let conn = setup_test_db().expect("Failed to set up test database");
    let result = create_table(&conn, "test_table");
    assert!(result.is_ok(), "Failed to create table");
}

#[test]
fn test_load_data() {
    let conn = setup_test_db().expect("Failed to set up test database");
    create_table(&conn, "test_table").expect("Failed to create table");

    let result = load_data(&conn, "test_table", "../data/sample_data.csv");
    assert!(result.is_ok(), "Failed to load data into table");
}

#[test]
fn test_execute_query() {
    let conn = setup_test_db().expect("Failed to set up test database");
    create_table(&conn, "test_table").expect("Failed to create table");
    load_data(&conn, "test_table", "../data/sample_data.csv").expect("Failed to load data");

    let result = execute_query(&conn, "SELECT * FROM test_table LIMIT 2");
    assert!(result.is_ok(), "Query execution failed");
}

#[test]
fn test_delete_table() {
    let conn = setup_test_db().expect("Failed to set up test database");
    create_table(&conn, "test_table").expect("Failed to create table");

    let result = delete_table(&conn, "test_table");
    assert!(result.is_ok(), "Failed to delete table");
}

