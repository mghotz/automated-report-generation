# src/visualizer.py
import os
import matplotlib.pyplot as plt

def create_histogram(data, column, table_name):
    # Create the output directory if it does not exist
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    column_data = [row[column] for row in data]
    plt.hist(column_data, bins=10, alpha=0.7, color='blue')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column} in {table_name}')
    
    file_path = os.path.join(output_dir, f'{table_name}_{column}_histogram.png')
    plt.savefig(file_path)
    plt.close()
