# VE3-CSVAnalysis
# Django CSV Data Analysis

This is a Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Setup Instructions


1. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

5. **Access the application:**
    Open a browser and navigate to `http://127.0.0.1:8000/upload/`.

## Features

- Upload CSV files for analysis.
- Display the first few rows of the data.
- Calculate summary statistics (mean, median, standard deviation) for numerical columns.
- Identify and handle missing values.
- Generate basic plots (histograms) for numerical columns and display them on the web page.

## Sample CSV File

A sample CSV file (`sample.csv`) is included for testing purposes.

## License

This project is licensed under the MIT License.
