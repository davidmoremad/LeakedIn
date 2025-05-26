import csv
import os
import json
from datetime import datetime

class CSVExporter:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def export_data(self, data, filename=None):
        """Export data to CSV file"""
        if not data:
            return None
            
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"phantombuster_export_{timestamp}.csv"
        
        filepath = os.path.join(self.output_dir, filename)
        
        # Handle different data formats
        if isinstance(data, list) and len(data) > 0:
            # If list of dictionaries, write to CSV
            if isinstance(data[0], dict):
                with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = list(data[0].keys())
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    
                    writer.writeheader()
                    writer.writerows(data)
            # If list of lists, write to CSV
            elif isinstance(data[0], list):
                with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(data)
        # If JSON string, convert to Python objects first
        elif isinstance(data, str):
            try:
                parsed_data = json.loads(data)
                if isinstance(parsed_data, list) and len(parsed_data) > 0:
                    return self.export_data(parsed_data, filename)
            except json.JSONDecodeError:
                # Not valid JSON, write as raw text
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(data)
        
        return filepath