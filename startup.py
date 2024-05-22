
import json
import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.workatastartup.com/companies"

data = []

def get_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find_all('a', class_='font-bold captialize mr-5')
    company = soup.find_all('span', class_="company-name text-2xl font-bold")
    salary = soup.find_all('span')  
    job_type = soup.find_all('div', class_='border-r border-gray-300 px-2 first-of-type:pl-0 last-of-type:border-none last-of-type:pr-0')
    location = soup.find_all('p', class_="job-details my-auto break-normal")  
    application_href = [i ['href'] for i in soup.find_all('a', class_="inline-flex items-center px-2.5 py-1.5 border border-transparent text-lg font-medium rounded shadow-sm text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500", href=True )]
    link = "".join(application_href)
    
    data.append({
      "title" : title,
      "location" : location,
      "salary" : salary,
      "job_type" : job_type,        
    })
    
    for title in title:
        print(f'\n', title.text)
    for location in location:   
        print(location.text)
    for salary in salary:    
        print(salary.text)
    for company in company:
        print(f'\n', company.text)
    for link in link:
        link = "".join(application_href)
        print(link) 
def save_jobs_to_csv(data, filename='jobs.csv'):        
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys.values)
            dict_writer.writeheader()
            dict_writer.writerows(jobs)
        print(save_jobs_to_csv)
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
            data.append(jobs.text.strip())
            return job
    job_data = get_jobs(url)
    json_file = 'top_deals.json'
    with open(json_file, mode='w') as file:
        json.dump(deals_data, file, indent=4)
    print(f"Data has been stored in {json_file}")
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
        
get_jobs(url) 

print(f"\n") 

# import requests
# from bs4 import BeautifulSoup
# import json
# url = "https://www.jumia.co.ke/catalog/productratingsreviews/sku/NI534ST0DQQMYNAFAMZ/"
# def top_deals(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     products = soup.find_all("p", class_="-pvs")
#     deals = []
#     for product in products:
#         deals.append(product.text.strip())
#     return deals
# deals_data = top_deals(url)
# json_file = 'top_deals.json'
# with open(json_file, mode='w') as file:
#     json.dump(deals_data, file, indent=4)
# print(f"Data has been stored in {json_file}")

 