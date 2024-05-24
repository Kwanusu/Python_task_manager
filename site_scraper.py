import requests
from bs4 import BeautifulSoup
import json
import csv
import re
from datetime import datetime
import os
import time
import random

# Define the URL of the jobs website
url = "https://www.workatastartup.com/companies"

# Set up a list of user agents to rotate
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) Trident/7.0; AS; rv:11.0) like Gecko',
]

# Define a function to make requests with a random user agent
def get_page(url):
    headers = {
        'User-Agent': random.choice(user_agents),
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    return response.content

def get_jobs(url):
    content = get_page(url)
    soup = BeautifulSoup(content, "html.parser")

    titles = soup.find_all('a', class_='font-bold captialize mr-5')
    companies = soup.find_all('span', class_="company-name text-2xl font-bold")
    salaries = soup.find_all('span', string=re.compile(r'\$\d+'))
    locations = soup.find_all('p', class_="job-details my-auto break-normal")
    dates_posted = soup.find_all('span', class_="text-gray-300 text-sm block sm:inline ml-0 sm:ml-2 mt-1 sm:mt-0")
    application_hrefs = [a['href'] for a in soup.find_all('a', class_="inline-flex items-center px-2.5 py-1.5 border border-transparent text-lg font-medium rounded shadow-sm text-white bg-orange-500 hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500", href=True)]

    job_list = []

    for i in range(len(titles)):
        title = titles[i].text.strip()
        company = companies[i].text.strip() if i < len(companies) else ''
        salary = salaries[i].text.strip() if i < len(salaries) else ''
        salary = re.sub(r'[^\d]', '', salary)  # Remove non-numeric characters
        location = locations[i].text.strip() if i < len(locations) else ''
        date_posted = dates_posted[i].text.strip() if i < len(dates_posted) else ''
        application_href = application_hrefs[i] if i < len(application_hrefs) else ''

        # Only include internships
        if 'intern' in title.lower():
            job_list.append({
                'title': title,
                'company': company,
                'salary_scale': salary,
                'location': location,
                'date_posted': date_posted,
                'application_href': application_href,
                'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        # Add a delay between requests to avoid getting blocked
        time.sleep(random.uniform(1, 3))

    return job_list

def clean_string(s):
    # Remove non-alphanumeric characters and convert to lowercase
    return re.sub(r'\W+', '', s).lower()

def update_json_file(file_path, job_list):
    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_jobs = json.load(file)
    else:
        existing_jobs = []

    # Create a set of existing job identifiers (title + company)
    existing_jobs_set = set((clean_string(job['title']), clean_string(job['company'])) for job in existing_jobs)

    # Append new jobs to the existing jobs list
    for job in job_list:
        job_id = (clean_string(job['title']), clean_string(job['company']))
        if job_id not in existing_jobs_set:
            existing_jobs.append(job)
            existing_jobs_set.add(job_id)

    # Save updated job list to the JSON file
    with open(file_path, 'w') as file:
        json.dump(existing_jobs, file, indent=4)

def update_csv_file(file_path, job_list):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)

    # Create a set of existing job identifiers (title + company)
    existing_jobs_set = set()
    if file_exists:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_jobs_set.add((clean_string(row['title']), clean_string(row['company'])))

    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'company', 'salary_scale', 'location', 'date_posted', 'application_href', 'scraped_at'])

        # Write header if the file does not exist
        if not file_exists:
            writer.writeheader()

        # Write job data as dictionaries
        for job in job_list:
            job_id = (clean_string(job['title']), clean_string(job['company']))
            if job_id not in existing_jobs_set:
                writer.writerow(job)
                existing_jobs_set.add(job_id)

def main():
    job_list = get_jobs(url)

    json_file_path = 'internships.json'
    csv_file_path = 'internships.csv'

    # Ensure JSON file creation if not exists
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as file:
            json.dump([], file)

    update_json_file(json_file_path, job_list)
    update_csv_file(csv_file_path, job_list)

if __name__ == "__main__":
    main()
