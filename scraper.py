from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_jobs(pages=2):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    company_names = []
    job_titles = []

    for page in range(1, pages + 1):
        url = f"https://jobs.stationf.co/search?page={page}"
        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        job_listings = soup.select("a.jobs-item-link")
        for listing in job_listings:
            title_elem = listing.select_one("h4.job-title")
            job_title = title_elem.get_text(strip=True) if title_elem else 'N/A'

            company_elem = listing.select_one("li.job-company")
            company_name = company_elem.get_text(strip=True) if company_elem else 'N/A'

            job_titles.append(job_title)
            company_names.append(company_name)

    driver.quit()
    return pd.DataFrame({'Company': company_names, 'Job Title': job_titles})
