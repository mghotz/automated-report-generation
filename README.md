# Automated Report Generation

## Description
The Automated Report Generation project provides a flexible and efficient way to generate data reports. Users can choose to source data from a database or a CSV file, allowing for broad applicability across different use cases. This project includes capabilities to summarize data, visualize it with histograms, and generate comprehensive PDF reports.

## Setup and Usage

### Prerequisites
- Python 3.6+
- `pip` (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mghotz/automated-report-generation
   cd report-ai
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and configure it as needed:
   ```dotenv
   INTEGRATION_TYPE=csv  # Options: 'database' or 'csv'
   DATABASE_URL=postgresql+psycopg2://user:password@localhost/dbname  # Only if using database integration
   CSV_FILE_PATH=/path/to/your/csvfile.csv  # Only if using CSV integration
   ```

### Running the Application
To generate a report, run the main script with the desired integration type specified in the `.env` file:
```bash
python3 src/main.py
```

### Example Usage
- For CSV integration, specify the path to your CSV file in the `.env` file.
- For database integration, provide the appropriate database URL in the `.env` file.

The script will prompt you to enter the table name and columns you wish to include in the report. If using a database, ensure the specified table exists.

### Error Handling
- Ensure that all required fields in the `.env` file are correctly filled.
- The script will handle invalid columns and other input errors, providing clear messages for corrective actions.

## Contribution
API integration is not ready yet. We welcome contributions to this feature and others. Feel free to fork the repository and submit pull requests.

## Author
This project is authored by Mahammad Salimov. Connect with me on [LinkedIn](https://www.linkedin.com/in/mahammad-salimov-91089060/).

---

This project is designed to be user-friendly and highly customizable. Your feedback and contributions are invaluable in making this tool more robust and versatile. Happy reporting!