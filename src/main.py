import sys
import os
sys.path.append('..')  # Ensure the parent directory is in the Python path

from config import INTEGRATION_TYPE, DATABASE_URL
from database.db_config import init_db, get_db_info
from database.db_utils import get_table_data
from summarizer import summarize_data
from visualizer import create_histogram
from report_generator import generate_report

def main():
    if INTEGRATION_TYPE == 'database':
        try:
            engine, session = init_db()
            db_info = get_db_info()

            table_summaries = {}
            visual_paths = {}

            for table in db_info.keys():
                data, columns = get_table_data(session, table)
                summary = summarize_data(data, columns)
                table_summaries[table] = summary

                visual_paths[table] = []
                for column in columns:
                    path = f'output/{table}_{column}_histogram.png'
                    create_histogram(data, column, table)
                    visual_paths[table].append(path)
            
            if not os.path.exists('output'):
                os.makedirs('output')
                
            generate_report(table_summaries, visual_paths)
            print("Report generated successfully!")
        
        except Exception as e:
            print(f"Error: {e}")
    
    elif INTEGRATION_TYPE == 'csv':
        print("CSV support will be added in future versions.")
    
    elif INTEGRATION_TYPE == 'api':
        print("API support will be added in future versions.")
    
    else:
        print("Invalid integration type. Please check your configuration.")

if __name__ == "__main__":
    main()
