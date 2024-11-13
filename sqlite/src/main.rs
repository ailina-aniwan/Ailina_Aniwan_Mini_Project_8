use clap::{Parser, Subcommand};
use rusqlite::{Connection, Result};
use sqlite::*; // Import the functions from lib.rs

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Debug, Subcommand)]
enum Commands {
    /// Create a table
    #[command(alias = "c", short_flag = 'c')]
    Create { table_name: String },

    /// Execute a query
    #[command(alias = "q", short_flag = 'q')]
    Query { query: String },

    /// Delete a table
    #[command(alias = "d", short_flag = 'd')]
    Delete { table_name: String },

    /// Load data from a CSV file into a table
    #[command(alias = "l", short_flag = 'l')]
    Load {
        table_name: String,
        file_path: String,
    },
}

fn main() -> Result<()> {
    let args = Cli::parse();
    let conn = Connection::open("my_database.db")?;

    match args.command {
        Commands::Create { table_name } => {
            println!("Creating Table {}", table_name);
            create_table(&conn, &table_name).expect("Failed to create table");
        }
        Commands::Query { query } => {
            println!("Executing Query: {}", query);
            execute_query(&conn, &query).expect("Failed to execute query");
        }
        Commands::Delete { table_name } => {
            println!("Deleting Table {}", table_name);
            delete_table(&conn, &table_name).expect("Failed to delete table");
        }
        Commands::Load {
            table_name,
            file_path,
        } => {
            println!("Loading data into table '{}' from '{}'", table_name, file_path);
            load_data(&conn, &table_name, &file_path).expect("Failed to load data");
        }
    }
    Ok(())
}
