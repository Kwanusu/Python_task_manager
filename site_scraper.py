import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.ycombinator.com/jobs"

def get_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find_all('a', class_='font-semibold text-linkColor')
    company = soup.find_all('div', class_='text-[12px] font-bold text-[#e96f37]')
    salary = soup.find_all('div','strong')  
    job_type = soup.find_all('div', class_='border-r border-gray-300 px-2 first-of-type:pl-0 last-of-type:border-none last-of-type:pr-0')
    location = soup.find_all('div',  class_="border-r border-gray-300 px-2 first-of-type:pl-0 last-of-type:border-none last-of-type:pr-0")  
    application_href = soup.find_all('a', class_="ycdc-btn ycdc-btn-sm border-brand-200 hover:bg-brand-600")
    link = "".join(application_href)
    
    for title in title:
        print(f'\n', title.text)
    for location in location:   
        print(location.text)
    for salary in salary:    
        print(salary.text)
    for company in company:
        print(f'\n', company.text)
    # for link in link:
    #     print(link)    
def save_jobs_to_csv(jobs, filename='my_jobs.csv'):        
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys.value)
            dict_writer.writeheader()
            dict_writer.writerows(jobs)
        print(f"Jobs have been saved to {filename}")
        
get_jobs(url) 

print(f"\n")       
    