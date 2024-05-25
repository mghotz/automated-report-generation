import sys
import os
import pandas as pd
from dotenv import load_dotenv
from config import INTEGRATION_TYPE, DATABASE_URL, CSV_FILE_PATH
from database.db_config import init_db, get_db_info
from database.db_utils import get_table_data
from summarizer import summarize_data
from visualizer import create_histogram
from report_generator import generate_report

load_dotenv()  # Load environment variables from .env file

def get_user_input(available_columns):
    columns_input = input("Enter column names separated by commas (or * for all columns): ")
    if columns_input.strip() == "*":
        return available_columns
    columns = [col.strip() for col in columns_input.split(',')]
    invalid_columns = [col for col in columns if col not in available_columns]
    if invalid_columns:
        print(f"Invalid columns: {', '.join(invalid_columns)}")
        sys.exit(1)
    return columns

def handle_database_integration():
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    engine, session = init_db()
    db_info = get_db_info()

    table = input("Enter the table name: ")

    if table not in db_info:
        print(f"Table '{table}' does not exist in the database.")
        return

    available_columns = db_info[table].keys()
    columns = get_user_input(available_columns)

    data, _ = get_table_data(session, table)
    print("Original data:", data)  # Debug print

    filtered_data = [{col: row[col] for col in columns if col in row.keys()} for row in data]
    print("Filtered data:", filtered_data)  # Debug print

    summary = summarize_data(filtered_data, columns)
    visual_paths = []

    for column in columns:
        if column in db_info[table]:
            path = create_histogram(filtered_data, column, table)
            if path:
                visual_paths.append(path)

    generate_report({table: summary}, {table: visual_paths})
    print("Report generated successfully!")

def handle_csv_integration():
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    csv_file = CSV_FILE_PATH
    df = pd.read_csv(csv_file)
    available_columns = df.columns.tolist()
    columns = get_user_input(available_columns)

    data = df.to_dict(orient='records')
    print("Original data:", data)  # Debug print

    filtered_data = [{col: row[col] for col in columns if col in row.keys()} for row in data]
    print("Filtered data:", filtered_data)  # Debug print

    summary = summarize_data(filtered_data, columns)
    visual_paths = []

    for column in columns:
        path = create_histogram(filtered_data, column, 'CSV_Data')
        if path:
            visual_paths.append(path)

    generate_report({'CSV_Data': summary}, {'CSV_Data': visual_paths})
    print("Report generated successfully!")

def main():
    if INTEGRATION_TYPE == 'database':
        try:
            handle_database_integration()
        except Exception as e:
            print(f"Error: {e}")

    elif INTEGRATION_TYPE == 'csv':
        try:
            handle_csv_integration()
        except Exception as e:
            print(f"Error: {e}")

    elif INTEGRATION_TYPE == 'api':
        print("API support will be added in future versions.")

    else:
        print("Invalid integration type. Please check your configuration.")

if __name__ == "__main__":
    main()
