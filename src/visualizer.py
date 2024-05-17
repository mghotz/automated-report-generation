# src/visualizer.py
import os
import matplotlib.pyplot as plt
from uuid import UUID

def create_histogram(data, column, table_name):
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    column_data = [row[column] for row in data if row[column] is not None and not isinstance(row[column], UUID)]
    if not column_data:
        return None

    first_elem = column_data[0]
    if isinstance(first_elem, bool):
        true_count = sum(column_data)
        false_count = len(column_data) - true_count
        plt.bar(['True', 'False'], [true_count, false_count], color=['blue', 'orange'])
    else:
        plt.hist(column_data, bins=10, alpha=0.7, color='blue')

    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column} in {table_name}')

    file_path = os.path.join(output_dir, f'{table_name}_{column}_histogram.png')
    plt.savefig(file_path)
    plt.close()
    return file_path
