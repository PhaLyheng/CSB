import pandas as pd
import csv
from custom_exceptions import DatabaseConnectionError

class DataProcessor:
    def __init__(self):
        self.data = pd.DataFrame()

    def process_file(self, file_path):
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)
            elif file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(content)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except pd.errors.ParserError as e:
            print(f"Error parsing file: {e}")

    def transfer_data(self, criteria, source_file, destination_file):
        try:
            if '>' in criteria:
                column, value = criteria.split('>')
                value = float(value)
                filtered_data = self.data[self.data[column.strip()] > value]
            else:
                filtered_data = self.data

            filtered_data.to_csv(destination_file, index=False)
        except KeyError as e:
            print(f"Error in criteria: {e}")
        except DatabaseConnectionError as e:
            raise e

    def add_data(self, new_data):
        # Convert new_data dict to DataFrame and append to self.data
        new_row = pd.DataFrame([new_data])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        print(f"Added data for {new_data['Student']} successfully.")
