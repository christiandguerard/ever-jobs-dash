import csv
import os

def clean_data():
    fields_to_keep = ['site', 'title', 'companyName', 'location', 'jobUrl', 'datePosted']
    input_file = 'temp.csv'
    output_file = 'daily_jobs.csv'
    
    if not os.path.exists(input_file):
        return

    # Check if we need to write the header (only for the very first site)
    file_exists = os.path.isfile(output_file)
    
    with open(input_file, 'r', encoding='utf-8') as f_in:
        reader = csv.DictReader(f_in)
        with open(output_file, 'a', encoding='utf-8', newline='') as f_out:
            writer = csv.writer(f_out)
            
            # Write a clean header only if the file is new
            if not file_exists:
                writer.writerow(['Site', 'Title', 'Company', 'Location', 'URL', 'Date'])
            
            for row in reader:
                # Extract clean data and strip any messy whitespace
                writer.writerow([row.get(f, '').strip() for f in fields_to_keep])

if __name__ == "__main__":
    clean_data()
