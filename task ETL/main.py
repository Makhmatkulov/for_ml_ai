import pandas as pd
import pyodbc
import os

DB_SERVER = 'WINDOWS-A8SDO0H\\SQLEXPRESS'
DB_DRIVER = 'ODBC Driver 17 for SQL Server'
DB_NAME = 'TaskETL'
DATABASE_OUTPUT_DIR = './task ETL/databases'  # Directory to save the database files

def connect_to_sql(server, driver, db_name):
    conn_str = f"DRIVER={{{driver}}};SERVER={server};DATABASE={db_name};Trusted_Connection=Yes;TrustServerCertificate=Yes"
    return pyodbc.connect(conn_str, autocommit=True)

def create_table_from_csv(cursor, table_name, df):
    columns = ", ".join([f"[{col}] NVARCHAR(MAX)" if df[col].dtype == 'object' else f"[{col}] FLOAT" for col in df.columns])
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    cursor.execute(f"CREATE TABLE {table_name} ({columns})")

def clean_float_value(value):
    try:
        if pd.isna(value) or value == "":
            return None
        return float(value)
    except ValueError:
        return None

def insert_data_from_csv(cursor, table_name, df):
    for _, row in df.iterrows():
        cleaned_row = [clean_float_value(row[col]) if isinstance(row[col], (int, float)) else row[col] for col in df.columns]
        columns = ", ".join(f"[{col}]" for col in df.columns)
        values = ", ".join("?" for _ in df.columns)
        cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})", tuple(cleaned_row))

def export_table_to_csv(cursor, table_name, output_dir):
    query = f"SELECT * FROM {table_name}"
    try:
        df = pd.read_sql(query, cursor.connection)
        os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
        output_file = os.path.join(output_dir, f"{table_name}.csv")
        df.to_csv(output_file, index=False)
        print(f"Exported {table_name} to {output_file}")
    except Exception as e:
        print(f"Error exporting {table_name}: {e}")

def process_csv_files(source_folder, conn):
    cursor = conn.cursor()
    for file_name in os.listdir(source_folder):
        if file_name.endswith('.csv'):
            print(f"Processing: {file_name}")
            file_path = os.path.join(source_folder, file_name)
            table_name = os.path.splitext(file_name)[0]
            try:
                df = pd.read_csv(file_path)
                print(f"Loaded {file_name} with {df.shape[0]} rows and {df.shape[1]} columns.")
                create_table_from_csv(cursor, table_name, df)
                insert_data_from_csv(cursor, table_name, df)
                export_table_to_csv(cursor, table_name, DATABASE_OUTPUT_DIR)  # Export table to CSV
                print(f"Successfully processed and exported: {file_name}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
    cursor.close()

def main():
    source_folder = './task ETL/source'
    try:
        conn = connect_to_sql(DB_SERVER, DB_DRIVER, DB_NAME)
        process_csv_files(source_folder, conn)
        conn.close()
        print("All files processed and exported successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
