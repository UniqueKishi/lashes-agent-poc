import csv
import json
from datetime import datetime

SOURCE_FILE = 'clients.csv'   
OUTPUT_FILE = 'clients.json'
DATE_FORMAT = '%Y-%m-%d' # %m = Month, %d = Day, %Y = Year (4 digits)

def calculate_days_ago(date_string):
    if not date_string:
        return 0    #for empty rows
    try:
        appt_date = datetime.strptime (date_string, DATE_FORMAT) #string to actual date format
        today = datetime.now() # today's date
        diff = today - appt_date  #delta is diff
        return diff.days
    except ValueError:
        print(f"Warning: Something is wrong'{date_string}'") #why the f??
        return 0

def run_etl():
    clean_data = [] #is this the start of a dictionary???
    
    # encoding='utf-8-sig' handles weird characters sometimes found in Excel CSVs
    with open(SOURCE_FILE, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            client = {}

            # --- TRANSFORMATION 1: Combine Names ---
            # We grab "First Name" and "Surname" and join them with a space
            first = row.get("First Name", "").strip()
            last = row.get("Surname", "").strip()
            full_name = f"{first} {last}"
            client["name"] = full_name

            # --- TRANSFORMATION 2: Calculate Days ---
            date_str = row.get("Last Visit", "").strip()
            client["last_visit_days"] = calculate_days_ago(date_str)

            # Add to our list
            clean_data.append(client)


    # Save to JSON
    with open(OUTPUT_FILE, mode='w') as f:
        json.dump(clean_data, f, indent=4)
        
    print(f"Success! Converted {len(clean_data)} clients. Saved to {OUTPUT_FILE}.")

if __name__ == "__main__":
    run_etl()

    


