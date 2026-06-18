import csv
import os
import json
from datetime import datetime

class DataProcessor:
    """
    A robust system for handling file operations and data processing.
    Focuses on CSV and Text file management as per Project 3 requirements.
    """
    
    def __init__(self, input_file="sales_data.csv", output_file="summary_report.csv"):
        self.input_file = input_file
        self.output_file = output_file
        self.data = []

    def generate_sample_data(self):
        """Generates a sample CSV file for demonstration purposes."""
        headers = ["Date", "Product", "Category", "Quantity", "Price"]
        sample_rows = [
            ["2024-01-01", "Laptop", "Electronics", 5, 1200],
            ["2024-01-02", "Desk Chair", "Furniture", 10, 150],
            ["2024-01-03", "Mouse", "Electronics", 25, 25],
            ["2024-01-04", "Monitor", "Electronics", 8, 300],
            ["2024-01-05", "Bookshelf", "Furniture", 3, 200],
            ["2024-01-06", "Headphones", "Electronics", 15, 80],
        ]
        
        try:
            with open(self.input_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(sample_rows)
            print(f"[INFO] Sample data generated: {self.input_file}")
        except Exception as e:
            print(f"[ERROR] Failed to generate sample data: {e}")

    def read_csv(self):
        """Reads data from the CSV file with error handling."""
        if not os.path.exists(self.input_file):
            print(f"[ERROR] File '{self.input_file}' not found.")
            return False
        
        try:
            with open(self.input_file, mode='r') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
            print(f"[SUCCESS] Loaded {len(self.data)} records from {self.input_file}")
            return True
        except PermissionError:
            print(f"[ERROR] Permission denied when reading {self.input_file}")
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")
        return False

    def process_data(self):
        """Performs filtering, sorting, and summarization."""
        if not self.data:
            print("[WARNING] No data to process.")
            return None

        # 1. Summarization: Calculate total revenue per category
        summary = {}
        for row in self.data:
            cat = row['Category']
            qty = int(row['Quantity'])
            price = float(row['Price'])
            revenue = qty * price
            
            if cat not in summary:
                summary[cat] = {"Total_Qty": 0, "Total_Revenue": 0.0}
            
            summary[cat]["Total_Qty"] += qty
            summary[cat]["Total_Revenue"] += revenue

        # 2. Sorting: Sort the original data by Price (Descending)
        self.data.sort(key=lambda x: float(x['Price']), reverse=True)
        
        return summary

    def export_summary(self, summary):
        """Exports the processed summary to a new CSV file."""
        if not summary:
            return
        
        try:
            headers = ["Category", "Total_Quantity", "Total_Revenue"]
            with open(self.output_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                for cat, values in summary.items():
                    writer.writerow([cat, values['Total_Qty'], f"${values['Total_Revenue']:.2f}"])
            print(f"[SUCCESS] Summary report exported to: {self.output_file}")
        except Exception as e:
            print(f"[ERROR] Failed to export summary: {e}")

    def display_report(self, summary):
        """Prints a clean tabular report to the console."""
        print("\n" + "="*50)
        print(f"{'CATEGORY':<20} | {'QTY':<10} | {'REVENUE':<15}")
        print("-" * 50)
        for cat, values in summary.items():
            print(f"{cat:<20} | {values['Total_Qty']:<10} | ${values['Total_Revenue']:,.2f}")
        print("="*50 + "\n")

def main():
    # Initialize the system
    processor = DataProcessor()
    
    # 1. Ensure input file exists (Generate if missing)
    if not os.path.exists(processor.input_file):
        processor.generate_sample_data()
    
    # 2. Read the file
    if processor.read_csv():
        # 3. Process the data
        summary_results = processor.process_data()
        
        # 4. Display the results
        if summary_results:
            processor.display_report(summary_results)
            
            # 5. Export the findings
            processor.export_summary(summary_results)

if __name__ == "__main__":
    main()
