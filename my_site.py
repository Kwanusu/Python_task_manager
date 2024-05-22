
    
import csv

import requests
import json
from bs4 import BeautifulSoup

params = {
    "q": "python"
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
}

html = requests.get("https://wuzzuf.net/search/jobs/", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.content, "html.parser")

data = []

for result in soup.select(".css-1gatmva"):                            
    title = result.select_one(".css-m604qf .css-o171kl").text         
    company_name = result.select_one(".css-17s97q8").text             
    adding_time = result.select_one(".css-4c4ojb, .css-do6t5g").text  
    location = result.select_one(".css-5wys0k").text                  
    employment = result.select_one(".css-1lh32fc").text               
    snippet = result.select_one(".css-1lh32fc+ div").text             

    data.append({
      "title" : title,
      "company_name" : company_name,
      "adding_time" : adding_time,
      "location" : location,
      "employment" : employment,
      "snippet" : snippet    
    })

# Print all job listings after the loop
print(json.dumps(data, indent=2))

def append_to_csv(data, file_path):
    """
    Append job data to a CSV file.
    
    Args:
        data (list of dict): List of dictionaries containing job data.
        file_path (str): Path to the CSV file.
    """
    # Define the field names
    fieldnames = ["title", "company_name", "adding_time", "location", "employment", "snippet"]

    # Open the CSV file in append mode
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
 
        # Write data to the CSV file
        for job in data:
            writer.writerow(job)
append_to_csv(data, "jobs.csv")

def append_to_csv(data, file_path):
    """
    Append job data to a CSV file.
    
    Args:
        data (list of dict): List of dictionaries containing job data.
        file_path (str): Path to the CSV file.
    """
    # Define the field names
    fieldnames = ["title", "company_name", "adding_time", "location", "employment", "snippet"]

    # Open the CSV file in append mode
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write data to the CSV file
        for job in data:
            writer.writerow(job)

    
     
